# ♜ Personal Chess Coach

A Flask-based chess analysis web application that helps players understand their games by analyzing PGN files and providing insights powered by Stockfish.

## Features

### ✅ PGN Analysis

* Paste any valid PGN directly into the web interface.
* Extracts game metadata including:

  * White player
  * Black player
  * Game result
  * White Elo
  * Black Elo
  * Event
  * Date
  * ECO (Opening Code)
  * Total moves played

### ✅ Stockfish Integration

* Uses the Stockfish chess engine for position evaluation.
* Generates move-by-move evaluations throughout the game.

### ✅ Blunder Detection

* Detects significant evaluation drops.
* Highlights moves that may have cost material or positional advantage.

### ✅ Web Interface

* Built using Flask and Bootstrap.
* Simple interface for submitting PGNs and viewing analysis results.

## Tech Stack

### Backend

* Python
* Flask
* python-chess
* Stockfish

### Frontend

* HTML
* CSS
* Bootstrap 5

## Project Structure

```text
Personal-chess-coach/
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
│
├── templates/
│   ├── index.html
│   ├── results.html
│   └── EasterEgg.html
│
├── app.py
├── README.md
└── .gitignore
```

## Installation

### Clone the repository

```bash
git clone https://github.com/AnirudhGhatty/Personal-chess-coach.git
cd Personal-chess-coach
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install flask
pip install python-chess
pip install stockfish
```

### Download Stockfish

Download Stockfish from the official website and place the executable inside:

```text
stockfish/
└── stockfish.exe
```

> Note: The Stockfish executable is intentionally excluded from GitHub because it exceeds GitHub's file size limits.

## Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

in your browser.

## Example Workflow

1. Copy a PGN from Chess.com or Lichess.
2. Paste it into the analysis box.
3. Submit the game.
4. View:

   * Player information
   * Elo ratings
   * Result
   * Move count
   * Engine evaluations
   * Blunder analysis

## Current Development Status

### Completed

* [x] Flask application setup
* [x] PGN parsing
* [x] Metadata extraction
* [x] Move counting
* [x] Stockfish integration
* [x] Basic blunder detection
* [x] GitHub project setup

### Planned Features

* [ ] Evaluation graph
* [ ] Improved analysis UI
* [ ] Move-by-move review
* [ ] Tactical mistake explanations
* [ ] Playstyle analysis
* [ ] Personalized coaching recommendations

## Author

**Anirudh Ghatty**
