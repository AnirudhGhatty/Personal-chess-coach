import chess.pgn
import io

def parse_pgn(pgn_text):
    game = chess.pgn.read_game(io.StringIO(pgn_text))

    if game == None:
        return None
    
    return{
        "white" : game.headers.get("White" , "Unknown") ,
        "black" : game.headers.get("Black" , "Unknown") ,
        "result" : game.headers.get("Result" , "*")
    }
