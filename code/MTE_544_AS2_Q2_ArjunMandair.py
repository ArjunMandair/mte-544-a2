"""
Student Name & Last Name: Arjun Mandair
Origianl Author : Pi Thanacha Choopojcharoen
You must change the name of your file to MTE_544_AS2_Q2_(your full name).py
Do not use jupyter notebook.

*You may want to install the following libraries if you haven't done so.*

pip install numpy matplotlib pandas scipy

"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
import random
import pandas as pd

def plot_ellipse(S, b, ax):
    lambda_var = 9.80665
    eigvals, eigvecs = np.linalg.eigh(lambda_var*S)
    aa, bb = eigvals

    theta = np.linspace(0, 2 * np.pi, 100)
    unit_circle = np.array([np.cos(theta), np.sin(theta)])
    ellipse_param = np.array([aa * unit_circle[0], bb * unit_circle[1]])
    ellipse_points = eigvecs @ ellipse_param + b[:, np.newaxis]

    ax.plot(ellipse_points[0, :], ellipse_points[1, :], 'b-', label='Fitted Ellipse')
    ax.plot(b[0], b[1], 'ro', label='Center')
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend(loc='best')
    ax.grid(True)

def visualize_data(p, ax, inliers, threshold):
    ax.scatter(p[:, 0], p[:, 1], color='red', alpha=0.5, label='Raw Measurements (Ellipse)')
    ax.scatter(inliers[:, 0], inliers[:, 1], color='purple', alpha=0.7, label='Inliers')

    for point in inliers:
        circle = plt.Circle(point, threshold, color='orange', fill=False, linestyle='--', alpha=0.7)
        ax.add_patch(circle)

def is_positive_definite(matrix):
    try:
        np.linalg.cholesky(matrix)
        return True
    except np.linalg.LinAlgError:
        return False

def fit_ellipse_subset(points):
    # Given some number of points (you have to determined this), 
    # construct an ellipse that fits through those points.
    

    ##### ADD your code here : #####
    # Solve for A-E
    M = np.array([[x**2, 2*x*y, y**2, -2*x, -2*y] for x, y in points])
    A, B, C, D, E = np.linalg.solve(M, -np.ones(len(points)))

    # Convert A-E to Q and b formulas
    N = np.array([[A, B], [B, C]])
    DE = np.array([D, E])
    b = np.linalg.solve(N, DE)
    den = DE @ np.linalg.solve(N, DE) - 1
    
    # alpha undefened if denominator is too small
    if abs(den) < 1e-12:
        raise np.linalg.LinAlgError('alpha undefined')
    
    # else return Q and b
    alpha = 1 / den
    Q = alpha * N
    ##### END #####
    return Q, b

def ransac_ellipse(data, num_iterations=1000, threshold=0.2):
    inliers = []
    # Given the data sets, perform RANSAC to find the best Q and b as well as the inliers
    # Hint: You should use fit_ellipse_subset 
    # Hint: in some case, the Q matrix might not be positive defintie, use is_positive_definite to check.

    ##### ADD your code here : #####
    best_count = -1
    Q, b = None, None
    n = data.shape[0]
    lo, hi = data.min(axis=0), data.max(axis=0)
    span = (hi - lo).max()

    for _ in range(num_iterations):
        # 1. pick 5 random points and fit
        idx = np.random.choice(n, 5, replace=False)
        try:
            Q_try, b_try = fit_ellipse_subset(data[idx])
        except np.linalg.LinAlgError:
            continue
        # 2. skip non-ellipses and giant ellipses
        if not is_positive_definite(Q_try):
            continue
        semi_axes = 1 / np.sqrt(np.linalg.eigvalsh(Q_try))
        if np.any(b_try < lo) or np.any(b_try > hi) or semi_axes.max() > span:
            continue
        # 3. inlier test: | sqrt((p-b)^T Q (p-b)) - 1 | <= threshold
        d = data - b_try
        dist = np.abs(np.sqrt(np.einsum('ij,jk,ik->i', d, Q_try, d)) - 1)
        mask = dist <= threshold
        # 4. keep the best
        if mask.sum() > best_count:
            best_count = mask.sum()
            Q, b = Q_try, b_try
            inliers = data[mask]
    ##### END #####
    return Q,b,inliers

if __name__ == "__main__":
    # Load the data from CSV file and select N random points
    N = 500
    all_data = pd.read_csv('data_x_y.csv').to_numpy()
    dataset = all_data[np.random.choice(all_data.shape[0], N, replace=False), :]
    # dataset is p
    
    # NOTE I EDIT THIS FOR THE REPORT, YOU CAN CHANGE IT BACK TO 1000 OR WHATEVER YOU WANT
    Q, b_est, inliers = ransac_ellipse(dataset, num_iterations=1000, threshold=0.2)
    
    # Plot the raw measurements and fitted ellipse
    fig, ax1 = plt.subplots(1, 1, figsize=(16, 8))
    visualize_data(dataset, ax1, inliers, threshold=0.5)
    plot_ellipse(Q, b_est, ax1)
    ax1.set_title("RANSAC Ellipse Fitting with Threshold Visualization")

    plt.show()