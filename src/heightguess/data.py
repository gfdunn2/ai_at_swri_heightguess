"""Loading the height data."""
import warnings
from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "heights.csv"

# Some rows were recorded in centimeters by mistake. Anything taller than
# this many inches can't be a real adult height in inches (90 in = 7 ft 6 in).
MAX_HEIGHT_IN = 90.0

# A value above MAX_HEIGHT_IN is treated as centimeters only if it falls in
# this range of reasonable adult heights in cm (120 cm = 3 ft 11 in,
# 230 cm = 7 ft 7 in).
MIN_HEIGHT_CM = 120.0
MAX_HEIGHT_CM = 230.0

CM_PER_INCH = 2.54


def fix_cm_heights(heights):
    """Convert heights that were recorded in centimeters to inches.

    Returns (fixed_heights, converted), where `converted` is True for each
    height we converted. Values too tall to be inches and outside the
    reasonable cm range become NaN (missing), since we can't trust them.
    """
    too_tall = heights > MAX_HEIGHT_IN
    looks_like_cm = too_tall & heights.between(MIN_HEIGHT_CM, MAX_HEIGHT_CM)

    fixed = heights.copy()
    fixed[looks_like_cm] = heights[looks_like_cm] / CM_PER_INCH
    fixed[too_tall & ~looks_like_cm] = float("nan")
    return fixed, looks_like_cm


def load_heights(path=DATA_FILE):
    """Load the adult height table, with centimeter mistakes fixed.

    Columns: participant_id, sex, age, height_in, survey_weight,
    converted_from_cm (True if that height was converted from cm).
    Rows whose height can't be fixed are dropped with a warning.
    """
    df = pd.read_csv(path)
    df["height_in"], df["converted_from_cm"] = fix_cm_heights(df["height_in"])

    bad = df["height_in"].isna()
    if bad.any():
        warnings.warn(f"Dropping {bad.sum()} rows with unusable heights.")
    return df[~bad].reset_index(drop=True)
