"""
MTE 544 Assignment 2 - Q1b: fit an ellipse through 5 given points.
Run:  python MTE_544_AS2_Q1_ArjunMandair.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
 
np.set_printoptions(precision=8, suppress=True)
 
# The 5 points from the handout
P = np.array([(2.92, -6.01), (3.40, -7.20), (4.99, -7.84), (5.48, -7.04), (4.20, -5.91)])
x, y = P[:, 0], P[:, 1]
 
# build M, one row per point: [x^2, 2xy, y^2, -2x, -2y]
M = np.column_stack([x**2, 2*x*y, y**2, -2*x, -2*y])
print("M =\n", M)
print("rank(M) =", np.linalg.matrix_rank(M))
 
# solve M theta = -1 (vector of -1s)
theta = np.linalg.solve(M, -np.ones(5))
A, B, C, D, E = theta
print("\nA, B, C, D, E =", theta)
 
# convert to quadratic form
N = np.array([[A, B], [B, C]])
d = np.array([D, E])
print("\ndet(N) =", np.linalg.det(N))
N_inv = np.linalg.inv(N)
b = N_inv @ d
s = d @ N_inv @ d
alpha = 1 / (s - 1)
Q = alpha * N
print("N^-1 =\n", N_inv)
print("b =", b)
print("d^T N^-1 d =", s)
print("alpha =", alpha)
print("Q =\n", Q)
 
# checks
eigvals, eigvecs = np.linalg.eigh(Q)
print("\neigenvalues of Q =", eigvals, "-> ellipse" if np.all(eigvals > 0) else "-> NOT an ellipse")
for p in P:
    print(f"point {p}: (p-b)^T Q (p-b) = {(p - b) @ Q @ (p - b):.6f}")
print("Qb =", Q @ b, " alpha*d =", alpha * d)
 
# interpretation semi-axes = 1/sqrt(eigenvalue), major axis along the smaller eigenvalue's eigenvector
semi_axes = 1 / np.sqrt(eigvals)
angle = np.degrees(np.arctan2(eigvecs[1, 0], eigvecs[0, 0]))
print("\nsemi-axes =", semi_axes, " major-axis angle (deg) =", angle)
 
# plot points on the ellipse p = b + R diag(semi_axes) [cos t, sin t]
t = np.linspace(0, 2*np.pi, 200)
curve = b[:, None] + eigvecs @ np.diag(semi_axes) @ np.vstack([np.cos(t), np.sin(t)])
plt.plot(curve[0], curve[1], 'b-', label='Fitted ellipse')
plt.plot(x, y, 'ro', label='Given points')
plt.plot(b[0], b[1], 'k+', markersize=12, label='Centre b')
plt.gca().set_aspect('equal')
plt.grid(True); plt.legend(); plt.xlabel('x (unitless)'); plt.ylabel('y (unitless)')
plt.title('Q1b: ellipse through 5 points')
# save the figure for the report (the folder is created if it doesn't exist)
fig_dir = Path(__file__).resolve().parent.parent / 'report' / 'figures'
fig_dir.mkdir(parents=True, exist_ok=True)
plt.savefig(fig_dir / 'q1b_ellipse.png', dpi=200, bbox_inches='tight')
plt.show()