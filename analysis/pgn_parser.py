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

if __name__ == "__main__":
    sample_pgn = """
[Event "Live Chess"]
[Site "Chess.com"]
[Date "2026.06.03"]
[Round "?"]
[White "Anitriestoplay1"]
[Black "tawaziwazi"]
[Result "1-0"]
[TimeControl "900+10"]
[WhiteElo "1135"]
[BlackElo "1122"]
[Termination "Anitriestoplay1 won by resignation"]
[ECO "C41"]
[EndTime "6:46:18 GMT+0000"]
[Link "https://www.chess.com/game/live/169635776696?username=anitriestoplay1&move=0"]

1. e4 e5 2. Nf3 d6 3. d4 exd4 4. Qxd4 Nc6 5. Qd1 Nf6 6. Nc3 Bg4 7. h3 Bh5 8. g4
Bg6 9. Bd3 Be7 10. Be3 O-O 11. Qd2 Nb4 12. g5 Nd7 13. h4 f6 14. h5 Bf7 15. gxf6
Bxf6 16. O-O-O Nxd3+ 17. Qxd3 h6 18. Nd5 Bxd5 19. exd5 Re8 20. Rdg1 Rxe3 21.
Qxe3 Ne5 22. Qe4 Nxf3 23. Qxf3 Qf8 24. Kb1 a6 25. Rg6 Re8 26. Rhg1 Qe7 27. a3
Bg5 28. Re6 Qd7 29. Rxe8+ Qxe8 30. Qb3 b6 31. Qc3 Qe7 32. Re1 Qd7 33. Qc6 Qxc6
34. dxc6 Kf7 35. c4 Bh4 36. Re2 a5 37. Kc2 Bf6 38. b3 Bd4 39. Re4 Bc5 40. a4 Bb4
41. Kd3 Bc5 42. Rf4+ Ke7 43. Ke4 Ke8 44. Kd5 Ke7 45. Re4+ Kf7 46. f4 Kf8 47. Ke6
Kg8 48. Kd7 1-0
"""
print(parse_pgn(sample_pgn))
