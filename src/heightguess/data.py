"""Loading the height data."""
from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "heights.csv"


def load_heights(path=DATA_FILE):
    """Load the adult height table.

    Columns: participant_id, sex, age, height_in, survey_weight.
    """
    return pd.read_csv(path)
