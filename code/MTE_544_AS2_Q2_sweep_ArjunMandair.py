"""
MTE 544 Assignment 2 - Q2c: parameter study for the report.

Helper script only. It runs ransac_ellipse from the Q2 file while changing one
setting at a time, over several random seeds, then writes a LaTeX table and a
figure into the report folder.

Run:  python MTE_544_AS2_Q2_sweep_ArjunMandair.py
"""
from pathlib import Path
import time

import matplotlib
matplotlib.use('Agg')  # save to a file without opening a window
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from MTE_544_AS2_Q2_ArjunMandair import ransac_ellipse
from MTE_544_AS2_Q2_figure_ArjunMandair import ellipse_curve

SEEDS = range(10)
BASE_N, BASE_ITERS, BASE_EPS = 500, 1000, 0.2

# Each group changes one setting and keeps the other two at the baseline
GROUPS = [
    ('$N$', 'N', [50, 100, 500, 2000, 4999]),
    ('Iterations', 'iters', [10, 50, 200, 1000, 5000]),
    ('$\\varepsilon$', 'eps', [0.02, 0.05, 0.1, 0.2, 0.5, 1.0]),
]

# The extreme values shown side by side in the figure: (name, value)
PANELS = [('N', 50), ('N', 4999), ('iters', 10), ('iters', 5000), ('eps', 0.02), ('eps', 1.0)]
PANEL_LABEL = {'N': 'N', 'iters': 'Iterations', 'eps': 'ε'}

HERE = Path(__file__).resolve().parent
REPORT = HERE.parent / 'report'


def settings(name, value):
    """Baseline settings with one of them replaced."""
    params = {'N': BASE_N, 'iters': BASE_ITERS, 'eps': BASE_EPS}
    params[name] = value
    return params


def run_once(data, seed, N, iters, eps):
    """Draw N points with this seed and run RANSAC on them."""
    np.random.seed(seed)
    dataset = data[np.random.choice(data.shape[0], N, replace=False), :]
    start = time.perf_counter()
    Q, b, inliers = ransac_ellipse(dataset, num_iterations=iters, threshold=eps)
    return dataset, Q, b, inliers, time.perf_counter() - start


def mean_std(values, decimals):
    """Format a list of numbers as mean +/- standard deviation for LaTeX."""
    if len(values) == 0:
        return '--'
    return f'{np.mean(values):.{decimals}f} $\\pm$ {np.std(values):.{decimals}f}'


def study_setting(data, params):
    """Run one setting over all seeds and return a row of formatted results."""
    percent, bx, by, major, minor, times = [], [], [], [], [], []
    for seed in SEEDS:
        _, Q, b, inliers, elapsed = run_once(data, seed, **params)
        times.append(elapsed)
        if Q is None:  # every sample was rejected, so there is no model
            continue
        semi = 1 / np.sqrt(np.linalg.eigvalsh(Q))
        percent.append(100 * len(inliers) / params['N'])
        bx.append(b[0])
        by.append(b[1])
        major.append(semi.max())
        minor.append(semi.min())
    return [f'{len(percent)}/{len(SEEDS)}', mean_std(percent, 1), mean_std(bx, 2),
            mean_std(by, 2), mean_std(major, 2), mean_std(minor, 2), f'{np.mean(times):.3f}']


def draw_panels(data, path):
    """Plot seed 0 at the extreme value of each setting."""
    fig, axes = plt.subplots(3, 2, figsize=(7.0, 8.4), sharex=True, sharey=True)
    for ax, (name, value) in zip(axes.ravel(), PANELS):
        params = settings(name, value)
        dataset, Q, b, inliers, _ = run_once(data, 0, **params)
        ax.scatter(dataset[:, 0], dataset[:, 1], s=4, color='#eb6834', marker='x',
                   linewidths=0.6, label='Outliers', zorder=2)
        title = f'{PANEL_LABEL[name]} = {value}: no model found'
        if Q is not None:
            ax.scatter(inliers[:, 0], inliers[:, 1], s=5, color='#2a78d6', linewidths=0,
                       label='Inliers', zorder=2)
            curve = ellipse_curve(Q, b)
            ax.plot(curve[0], curve[1], color='#0b0b0b', lw=1.6, label='Fitted ellipse', zorder=3)
            title = f'{PANEL_LABEL[name]} = {value}: {len(inliers)}/{params["N"]} inliers'
        ax.set_title(title, fontsize=10)
        ax.set_aspect('equal', adjustable='box')
        ax.grid(True, color='#e5e4df', lw=0.6, zorder=0)
        ax.set_axisbelow(True)
        for side in ('top', 'right'):
            ax.spines[side].set_visible(False)
    for ax in axes[-1]:
        ax.set_xlabel('x (unitless)')
    for ax in axes[:, 0]:
        ax.set_ylabel('y (unitless)')
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center', ncol=3, frameon=False, markerscale=2.5)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(path, dpi=200, bbox_inches='tight')


if __name__ == "__main__":
    all_data = pd.read_csv(HERE / 'data_x_y.csv').to_numpy()

    # Build the table, one group of rows per setting
    lines = ['\\begin{tabular}{llccccccc}', '\\toprule',
             'Varied & Value & Runs & Inliers (\\%) & $b_x$ & $b_y$ & Major & Minor & Time (s) \\\\',
             '\\midrule']
    for g, (label, name, values) in enumerate(GROUPS):
        if g > 0:
            lines.append('\\midrule')
        for v, value in enumerate(values):
            row = study_setting(all_data, settings(name, value))
            print(label, value, row, flush=True)
            first = label if v == 0 else ''
            lines.append(' & '.join([first, str(value)] + row) + ' \\\\')
    lines += ['\\bottomrule', '\\end{tabular}', '']

    (REPORT / 'figures').mkdir(parents=True, exist_ok=True)
    (REPORT / 'q2c_table.tex').write_text('\n'.join(lines))
    draw_panels(all_data, REPORT / 'figures' / 'q2c_extremes.png')
