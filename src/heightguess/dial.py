"""Tuning the dial.

We start with a guess and meet people one at a time. After each guess we are
only told whether we were too high or too low. If we guessed too high, we turn
the dial down; if we guessed too low, we turn it up. The size of each turn
shrinks over time so the dial can settle.
"""
import numpy as np


def tune_dial(heights, start=60.0, first_turn=2.0, passes=3, seed=0):
    """Return the dial setting after listening to high/low feedback.

    heights    : sequence of heights (inches)
    start      : initial dial setting (inches)
    first_turn : size of the first adjustment (inches)
    passes     : how many times we go through everyone
    seed       : controls the order in which we meet people
    """
    heights = np.asarray(heights, dtype=float)
    rng = np.random.default_rng(seed)
    guess = start
    step = 0
    for _ in range(passes):
        for h in rng.permutation(heights):
            step += 1
            turn = first_turn / np.sqrt(step)
            too_high = guess > h
            if too_high:
                guess += turn
            else:
                guess -= turn
    return guess
