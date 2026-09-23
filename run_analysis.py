"""Guess the height: tune the dial on real data and report how we did."""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).parent / "src"))
from heightguess import dollars_lost, load_heights, tune_dial  # noqa: E402

OUT = Path(__file__).parent / "outputs"


def main():
    df = load_heights()
    heights = df["height_in"]

    guess = tune_dial(heights)
    cost = dollars_lost(guess, heights)

    print("Guess the height")
    print("----------------")
    print(f"Participants:            {len(df)}")
    print(f"Shortest person:         {heights.min():.1f} in")
    print(f"Tallest person:          {heights.max():.1f} in")
    print(f"Converted from cm:       {df['converted_from_cm'].sum()} heights")
    print(f"Dial setting (our guess): {guess:.2f} in")
    print(f"Average dollars lost:    ${cost:.2f} per guess")

    # Sanity check: a working dial always ends up somewhere between the
    # shortest and tallest person. If not, something is wrong with it.
    if not heights.min() <= guess <= heights.max():
        print("WARNING: dial setting is outside the range of the data; the dial may be broken.")

    OUT.mkdir(exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(heights, bins=np.arange(np.floor(heights.min()), np.ceil(heights.max()) + 1, 1.0))
    ax.axvline(guess, color="crimson", lw=2, label=f"our guess ({guess:.1f} in)")
    ax.set_xlabel("Height (in)")
    ax.set_ylabel("Number of people")
    ax.set_title("Adult heights and our best single guess")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "heights_histogram.png", dpi=120)
    print(f"Histogram saved to:      {OUT / 'heights_histogram.png'}")


if __name__ == "__main__":
    main()
