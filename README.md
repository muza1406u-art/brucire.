# Artemether Chiral Center Analyzer
# Brucine Chiral Compound Website (Python + Flask)

A public educational website that visualizes a simplified 3D stereocenter model for **artemether** and lets learners switch between **R** and **S** configuration.
This project is a public-ready educational website for **Brucine**, implemented in **Python** using Flask.

## Features
It shows:
- number of chiral centers,
- R/S configuration,
- student details,
- Python-generated 2D structure,
- Python-generated 3D structure projection.

- Interactive 3D viewer (rotate + zoom)
- Toggle between R and S configuration
- Visualized substituent priorities (CIP-style learning aid)
- Short explanation of how R/S assignment is determined
## Student details
- **Name:** Nalla Hari Hara Krishna
- **Reg No:** RA2511026050036
- **Dept:** CSE-AIML
- **Section:** A

## Run locally

Because this project uses JavaScript modules, run it with a local static server.

```bash
python3 -m http.server 8000
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open: <http://localhost:8000>
Open: <http://127.0.0.1:5000>

## Publish on GitHub

```bash
git add .
git commit -m "Build Python Brucine chiral analyzer website"
git push
```
