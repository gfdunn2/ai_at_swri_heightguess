"""The price of being wrong: you pay one dollar per inch of error."""
import numpy as np


def dollars_lost(guess, heights):
    """Average dollars lost per person when we always guess `guess`."""
    heights = np.asarray(heights, dtype=float)
    return float(np.mean(np.abs(heights - guess)))
