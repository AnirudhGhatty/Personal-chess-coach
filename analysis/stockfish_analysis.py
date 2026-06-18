import chess
import chess.pgn
import chess.engine
import io
import os


def get_engine_path():

    env_path = os.getenv("STOCKFISH_PATH")

    if env_path:
        return env_path

    if os.name == "nt":
        return "stockfish/stockfish.exe"

    return "stockfish/stockfish"


def safe_score(info):
    score = info["score"].white().score(mate_score=10000)
    return score if score is not None else 0


def analyze_game(pgn_text, engine_path=None):

    if engine_path is None:
        engine_path = get_engine_path()

    game = chess.pgn.read_game(io.StringIO(pgn_text))

    def classify_move(eval_loss):

        if eval_loss < 50:
            return "OK"

        elif eval_loss < 100:
            return "Inaccuracy"

        elif eval_loss < 300:
            return "Mistake"

        else:
            return "Blunder"

    if game is None:
        return None

    print(f"Using engine: {engine_path}")

    engine = chess.engine.SimpleEngine.popen_uci(engine_path)

    try:
        board = game.board()

        evaluations = []
        move_reviews = []
        move_number = 1

        for move in game.mainline_moves():

            player = "white" if board.turn else "black"
            san_move = board.san(move)

            before_info = engine.analyse(
                board,
                chess.engine.Limit(depth=16)
            )
            before_score = safe_score(before_info)

            board.push(move)

            after_info = engine.analyse(
                board,
                chess.engine.Limit(depth=16)
            )
            after_score = safe_score(after_info)

            loss = abs(after_score - before_score)

            print(
                f"{san_move}: before={before_score}, "
                f"after={after_score}, loss={loss}"
            )

            classification = classify_move(loss)

            move_reviews.append({
                "move_number": move_number,
                "player": player,
                "move": san_move,
                "before_eval": before_score,
                "after_eval": after_score,
                "Classification": classification
            })

            evaluations.append(after_score)

            if player == "black":
                move_number += 1

        return {
            "evaluations": evaluations,
            "move_reviews": move_reviews
        }

    finally:
        engine.quit()


def detect_blunders(evaluations, threshold=200):

    blunders = []

    for i in range(1, len(evaluations)):

        prev_eval = evaluations[i - 1]
        curr_eval = evaluations[i]

        if prev_eval is None or curr_eval is None:
            continue

        drop = prev_eval - curr_eval

        if drop >= threshold:

            move_number = (i // 2) + 1

            blunders.append({
                "move_index": i,
                "move_number": move_number,
                "loss": drop,
                "before": prev_eval,
                "after": curr_eval,
                "message": (
                    f"Move {move_number}: BLUNDER "
                    f"(lost ~{drop/100:.1f} points)"
                )
            })

    return blunders


def analyze_with_blunders(pgn_text, engine_path=None):

    if engine_path is None:
        engine_path = get_engine_path()

    analysis = analyze_game(pgn_text, engine_path)

    if analysis is None:
        return None

    evaluations = analysis["evaluations"]
    move_reviews = analysis["move_reviews"]

    blunders = detect_blunders(evaluations)

    return {
        "evaluations": evaluations,
        "move_reviews": move_reviews,
        "blunders": blunders,
        "report": (
            [b["message"] for b in blunders]
            if blunders
            else ["No major blunders found 👍"]
        )
    }