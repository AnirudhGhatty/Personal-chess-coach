from flask import Flask , render_template , request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/analyze" , methods = ["GET" , "POST"])
def analyze():
    pgn = request.form.get("pgn_text")
    print("Received PGN : " , pgn)
    results = {
        "Blunders" : 5 ,
        "Style" : "Positional" ,
        "Patterns" : "Theoretical"
    }
    return render_template("results.html" , results = results)

@app.route("/dev_mode")
def devmode():
    return render_template("EasterEgg.html")

if __name__ == "__main__":
    app.run(debug=True)