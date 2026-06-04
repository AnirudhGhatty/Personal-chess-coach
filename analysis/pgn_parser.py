import chess.pgn
import io

def parse_pgn(pgn_text):
    game = chess.pgn.read_game(io.StringIO(pgn_text))

    move_count = 0
    count = 0

    for move in game.mainline_moves():
        count += 1
    
    move_count = count//2

    if game == None:
        return None
    
    return{
        "white" : game.headers.get("White" , "Unknown") ,
        "black" : game.headers.get("Black" , "Unknown") ,
        "result" : game.headers.get("Result" , "*") ,
        "white_elo" : game.headers.get("WhiteElo" , "?") ,
        "black_elo" : game.headers.get("BlackElo" , "?") ,
        "eco" : game.headers.get("ECO" , "?") , 
        "date" : game.headers.get("Date" , "?") ,
        "event" : game.headers.get("Event" , "?") ,
        "moves" : move_count
    }
