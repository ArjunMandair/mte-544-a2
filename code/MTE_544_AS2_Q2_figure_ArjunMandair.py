"""
MTE 544 Assignment 2 - Q2b: figure for the report.

Helper script only. It runs ransac_ellipse from the Q2 file with a fixed seed, so
the figure and the numbers in the report come from the same run, and it draws
the ellipse directly from the fitted Q and b.

Run:  python MTE_544_AS2_Q2_figure_ArjunMandair.py
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')  # save to a file without opening a window
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from MTE_544_AS2_Q2_ArjunMandair import ransac_ellipse

SEED = 0
N = 500
THRESHOLD = 0.2  # same as the default in ransac_ellipse

HERE = Path(__file__).resolve().parent


def ellipse_curve(Q, b, scale=1.0):
    """Points on (p-b)^T Q (p-b) = scale^2. Semi-axes are 1/sqrt(eigenvalue of Q)."""
    eigvals, eigvecs = np.linalg.eigh(Q)
    t = np.linspace(0, 2 * np.pi, 300)
    circle = np.vstack([np.cos(t), np.sin(t)])
    return b[:, None] + scale * eigvecs @ np.diag(1 / np.sqrt(eigvals)) @ circle


if __name__ == "__main__":
    # Same steps as the main block of the Q2 file, with a seed added
    np.random.seed(SEED)
    all_data = pd.read_csv(HERE / 'data_x_y.csv').to_numpy()
    dataset = all_data[np.random.choice(all_data.shape[0], N, replace=False), :]
    Q, b, inliers = ransac_ellipse(dataset)
    print(f"inliers: {len(inliers)} of {N}, b = {b}")

    # Split the points so inliers and outliers can be drawn differently
    is_inlier = np.isin(dataset[:, 0], inliers[:, 0])
    outliers = dataset[~is_inlier]

    fig, ax = plt.subplots(figsize=(6.5, 4.6))
    ax.scatter(inliers[:, 0], inliers[:, 1], s=16, color='#2a78d6', linewidths=0,
               label=f'Inliers ({len(inliers)})', zorder=2)
    ax.scatter(outliers[:, 0], outliers[:, 1], s=22, color='#eb6834', marker='x',
               linewidths=1.2, label=f'Outliers ({len(outliers)})', zorder=2)

    # The inlier test is |sqrt(r) - 1| <= eps, so the band edges are the ellipse scaled by 1 +/- eps
    curve = ellipse_curve(Q, b)
    ax.plot(curve[0], curve[1], color='#0b0b0b', lw=2, label='Fitted ellipse', zorder=3)
    for i, scale in enumerate((1 - THRESHOLD, 1 + THRESHOLD)):
        band = ellipse_curve(Q, b, scale)
        ax.plot(band[0], band[1], color='#52514e', lw=1.2, ls='--', zorder=3,
                label=f'Inlier band (ε = {THRESHOLD})' if i == 0 else None)
    ax.plot(b[0], b[1], color='#0b0b0b', marker='+', ms=11, mew=2, ls='none',
            label='Centre b', zorder=4)

    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('x (unitless)')
    ax.set_ylabel('y (unitless)')
    ax.grid(True, color='#e5e4df', lw=0.7, zorder=0)
    ax.set_axisbelow(True)
    for side in ('top', 'right'):
        ax.spines[side].set_visible(False)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.16), ncol=3, frameon=False)

    fig_dir = HERE.parent / 'report' / 'figures'
    fig_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(fig_dir / 'q2_ransac_ellipse.png', dpi=200, bbox_inches='tight')
