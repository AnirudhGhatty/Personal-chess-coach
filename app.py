from flask import Flask , render_template , request
from analysis.pgn_parser import parse_pgn
from analysis.stockfish_analysis import analyze_with_blunders

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/analyze" , methods = ["GET" , "POST"])
def analyze():
    pgn = request.form.get("pgn_text")

    if not pgn:
        return render_template("results.html" , results = {"report" : ["No pgn provided!"]})
    
    analysis = analyze_with_blunders(pgn)
    
    parsed_data = parse_pgn(pgn)
    results = {
        "White" : parsed_data["white"] ,
        "Black" : parsed_data["black"] ,
        "Result" : parsed_data["result"] ,
        "WhiteElo" : parsed_data["white_elo"] ,
        "BlackElo" : parsed_data["black_elo"] ,
        "ECO" : parsed_data["eco"] ,
        "Date" : parsed_data["date"] ,
        "Event" : parsed_data["event"] ,
        "Moves" : parsed_data["moves"] ,

        "Evaluations" : analysis["evaluations"] ,
        "Blunders" : analysis["blunders"] ,
        "Report" : analysis["report"] , 

        "MoveReviews" : analysis["move_reviews"]
    }
    return render_template("results.html" , results = results)

@app.route("/dev_mode")
def devmode():
    return render_template("EasterEgg.html")

if __name__ == "__main__":
    app.run(debug=True)