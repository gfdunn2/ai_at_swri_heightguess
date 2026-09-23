# Guess the height

What's the best single guess for the height of an adult in the US?

This project turns that question into a tiny statistical model. The rules of the game:

1. You make one guess (a number in inches) for everyone.
2. For every person, you **pay one dollar per inch** you are wrong.
3. You learn by turning a **dial**: each time you guess, you're only told whether you were **too high or too low**, and you nudge the dial accordingly.

A statistical model doesn't give you certainty, only the best bet given the possibilities. Knowing something useful about a person (a "switch" that picks a different dial) can shrink those possibilities.

## Run it

```bash
pip install -r requirements.txt
python run_analysis.py
```

This prints a short report and saves a histogram to `outputs/heights_histogram.png`.

## Project layout

```
data/heights.csv          the data (one row per adult)
src/heightguess/data.py   loading the data
src/heightguess/dial.py   tuning the dial from high/low feedback
src/heightguess/cost.py   dollars lost per guess
run_analysis.py           runs everything and prints the report
```

## The data

Adults (20+) from the CDC's **National Health and Nutrition Examination Survey (NHANES), August 2021 to August 2023**: public-use files `BMX_L` (body measures) and `DEMO_L` (demographics). Heights were converted from centimeters to inches, and columns were renamed for readability.

| Column | Meaning | NHANES source |
|---|---|---|
| `participant_id` | anonymous respondent ID | `SEQN` |
| `sex` | `male` / `female` | `RIAGENDR` |
| `age` | age in years (80 = 80 or older) | `RIDAGEYR` |
| `height_in` | standing height, inches | `BMXHT` / 2.54 |
| `survey_weight` | how many US adults each respondent represents | `WTMEC2YR` |

**This copy has been modified for teaching purposes. Do not use it for research.** For real analyses, download the original files from the CDC.

**A sample is not the population.** NHANES deliberately over-samples some groups; unweighted averages from this file are not US population estimates. That's what `survey_weight` is for.

Created for AI@SwRI, Southwest Research Institute.
