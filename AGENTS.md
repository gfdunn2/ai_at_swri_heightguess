# Project guidance for AI coding agents

## What this is
A small teaching project: guess adult heights with a single tunable "dial" and
measure the cost of being wrong (one dollar per inch). Many readers are new to
programming, so clarity beats cleverness.

## How to run
- Install: `pip install -r requirements.txt`
- Run: `python run_analysis.py` (prints a report, writes `outputs/heights_histogram.png`)

## Conventions
- Python 3.10+, standard scientific stack only (numpy, pandas, matplotlib).
  Ask before adding any other dependency.
- Keep functions short and commented in plain language.
- Keep the report lines printed by `run_analysis.py` (you may add lines, but
  don't rename or remove existing ones).
- Put generated files in `outputs/`, never in `data/`.

## When you change something
- Run `python run_analysis.py` after every change and look at the output.
- Explain what you changed and why in plain language a non-programmer can follow.
