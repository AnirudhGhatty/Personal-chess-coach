# ♜ PawnSense

> **Stop guessing. Start understanding.**

PawnSense is a Flask-based chess analysis web application that helps players review their games using the **Stockfish chess engine**. Simply paste a PGN, and PawnSense provides engine evaluations, move classifications, an interactive replay board, an evaluation bar, and stores previously analyzed games for future reference.

---

# 📸 Screenshots

### 🏠 Home Page
![Home Page](static/screenshots/home.png)

### ♟️ Analysis Page
![Analysis Page](static/screenshots/analysis.png)

### 📚 Game History
![Game History](static/screenshots/history.png)

---

# ✨ Features

### ✅ PGN Analysis

- Paste any valid PGN from Chess.com or Lichess
- Automatically extracts:
  - White player
  - Black player
  - Result
  - White Elo
  - Black Elo
  - Event
  - Date
  - ECO Opening Code
  - Move list

---

### ✅ Stockfish Analysis

- Position evaluation after every move
- Engine-powered analysis using Stockfish
- Displays evaluation in centipawns

---

### ✅ Move Classification

Each move is automatically classified as:

- ✅ OK
- ⚠️ Inaccuracy
- ❌ Mistake
- 🚨 Blunder

---

### ✅ Interactive Game Review

- Replay the game move-by-move
- Navigate using Previous/Next buttons
- Live board updates using Chessboard.js

---

### ✅ Evaluation Bar

- Live evaluation bar updates as you step through the game
- Visual representation of which side is better

---

### ✅ Coach Report

Automatically summarizes major mistakes found during the game.

---

### ✅ Game History

Every analyzed game is automatically stored in a SQLite database.

The history page displays:

- White player
- Black player
- Result
- Opening
- Date analyzed

---

# 🛠 Tech Stack

## Backend

- Python
- Flask
- SQLite
- python-chess
- Stockfish

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Chess.js
- Chessboard.js

---

# 📂 Project Structure

```
PawnSense/
│
├── analysis/
│   ├── pgn_parser.py
│   ├── stockfish_analysis.py
│   └── coach.py
│
├── static/
│   ├── styles.css
│   ├── favicon.png
│   └── screenshots/
│       ├── home.png
│       ├── analysis.png
│       └── history.png
│
├── templates/
│   ├── index.html
│   ├── results.html
│   ├── history.html
│   └── EasterEgg.html
│
├── app.py
├── create_db.py
├── games.db
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/AnirudhGhatty/Personal-chess-coach.git
cd Personal-chess-coach
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install flask
pip install python-chess
```

Download **Stockfish** from the official website and place the executable inside

```
stockfish/
└── stockfish.exe
```

> **Note:** The Stockfish executable is intentionally excluded from GitHub because it exceeds GitHub's file size limit.

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 💡 Example Workflow

1. Copy a PGN from Chess.com or Lichess.
2. Paste it into PawnSense.
3. Submit the game.
4. Review:
   - Game information
   - Engine evaluation
   - Evaluation bar
   - Move classifications
   - Coach report
5. Access the game later through the **Game History** page.

---

# 📌 Project Status

## ✅ Version 1.0 Complete

Current features include:

- PGN parsing
- Stockfish integration
- Interactive move replay
- Evaluation bar
- Move classification
- SQLite game history
- Coach report

Future improvements may be added in later versions.

---

# 👨‍💻 Author

**Anirudh Ghatty**

B.Tech Computer Science Engineering

GitHub: https://github.com/AnirudhGhatty
