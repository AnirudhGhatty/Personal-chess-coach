import chess
import chess.pgn
import chess.engine
import io


def safe_score(info):
    """Convert Stockfish score to centipawns safely."""
    score = info["score"].white().score(mate_score=10000)
    return score if score is not None else 0


def analyze_game(pgn_text, engine_path="stockfish/stockfish.exe"):
    game = chess.pgn.read_game(io.StringIO(pgn_text))

    if game is None:
        return None

    engine = chess.engine.SimpleEngine.popen_uci(engine_path)
    board = game.board()

    evaluations = []

    for move in game.mainline_moves():
        board.push(move)

        info = engine.analyse(board, chess.engine.Limit(depth=8))
        score = safe_score(info)

        evaluations.append(score)

    engine.quit()

    return evaluations


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
                "message": f"Move {move_number}: BLUNDER (lost ~{drop/100:.1f} pawns)"
            })

    return blunders


def analyze_with_blunders(pgn_text, engine_path="stockfish/stockfish.exe"):

    evaluations = analyze_game(pgn_text, engine_path)
    
    if evaluations is None:
        return None

    blunders = detect_blunders(evaluations)

    return {
        "evaluations": evaluations,
        "blunders": blunders,
        "report": [b["message"] for b in blunders] if blunders else ["No major blunders found 👍"]
    }