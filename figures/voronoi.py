from scipy.spatial import Voronoi, voronoi_plot_2d

import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.append("/home/callow46/static-aa/figures/")
import params_plot

xlab, figdims = params_plot.fig_initialize(
    latex=False, setsize=True, fraction=1.0, size="reprint"
)
ws = 0.1
fig, axes = plt.subplots(1, 1, figsize=(figdims[0], 0.9 * figdims[0]))

points = np.array([[0.5, 0.5], [1, 0.3], [0.45, 0.9], [1.1, 1.0]])


ax1 = axes

vor = Voronoi(points)

plot_type = "MB"

if plot_type == "MB":
    ax1.plot(
        points[:, 0],
        points[:, 1],
        ".",
        color="r",
        markersize=10,
        # fillstyle="none",
        mfc="red",
    )
    # ax1.plot(vor.vertices[:, 0], vor.vertices[:, 1], "k--")
ax1.set_xlim(0.2, 1.4)
ax1.set_ylim(0.1, 1.3)

for simplex in vor.ridge_vertices:
    simplex = np.asarray(simplex)
    # if np.all(simplex >= 0):
    # ax1.plot(vor.vertices[simplex, 0], vor.vertices[simplex, 1], 'k--')

center = points.mean(axis=0)
for pointidx, simplex in zip(vor.ridge_points, vor.ridge_vertices):
    simplex = np.asarray(simplex)
    if np.any(simplex < 0):
        i = simplex[simplex >= 0][0]  # finite end Voronoi vertex
        t = points[pointidx[1]] - points[pointidx[0]]  # tangent
        t = t / np.linalg.norm(t)
        n = np.array([-t[1], t[0]])  # normal
        midpoint = points[pointidx].mean(axis=0)
        far_point = vor.vertices[i] + np.sign(np.dot(midpoint - center, n)) * n * 100
        # ax1.plot([vor.vertices[i,0], far_point[0]],
        #         [vor.vertices[i,1], far_point[1]], 'k--')

ax1.set_xticks([])
ax1.set_yticks([])

rad = 0.3  # sphere radius

x0 = 0.2 + 0.25 * 1.2
y0 = 0.1 + 0.25 * 1.2
x1 = 0.2 + 0.75 * 1.2
y1 = 0.1 + 0.75 * 1.2
circle0 = plt.Circle((x0, y0), rad, fc="white", ec="k", linestyle="--", fill=False)
circle1 = plt.Circle((x0, y1), rad, fc="white", ec="k", linestyle="--", fill=False)
circle2 = plt.Circle((x1, y0), rad, fc="white", ec="k", linestyle="--", fill=False)
circle3 = plt.Circle((x1, y1), rad, fc="white", ec="k", linestyle="--", fill=False)

points_even = np.array([[x0, y0], [x0, y1], [x1, y0], [x1, y1]])

if plot_type == "AA":
    ax1.plot(
        points_even[:, 0], points_even[:, 1], ".", color="r", markersize=10, mfc="red"
    )

    ax1.add_patch(circle0)
    ax1.add_patch(circle1)
    ax1.add_patch(circle2)
    ax1.add_patch(circle3)


n_arr = 100
x_arr = np.linspace(0.2, 1.4, n_arr)
y_arr = np.linspace(0.1, 1.3, n_arr)

xv, yv = np.meshgrid(x_arr, y_arr)
dens = np.zeros((n_arr, n_arr))
dens_sp = np.zeros((n_arr, n_arr))

alpha = 5
alpha_sp = 5
for i in range(4):
    dens_i = np.exp(
        -alpha * np.sqrt((xv - points[i, 0]) ** 2 + (yv - points[i, 1]) ** 2)
    )
    r_i = np.sqrt((xv - points_even[i, 0]) ** 2 + (yv - points_even[i, 1]) ** 2)
    r_i[r_i > 0.3] = 100
    print(r_i)
    dens_sp_i = np.exp(-alpha_sp * r_i)

    dens = dens + dens_i
    dens_sp = dens_sp + dens_sp_i

if plot_type == "MB":
    ax1.contourf(x_arr, y_arr, dens, alpha=0.5, cmap="Blues")
elif plot_type == "AA":
    ax1.contourf(x_arr, y_arr, dens_sp, alpha=0.5, cmap="Blues")


# fig.subplots_adjust(wspace=ws, top=0.95, bottom=0.05)
fig.subplots_adjust(wspace=ws, right=1.0, left=0.0, top=1.0, bottom=0.0)

plt.savefig(
    "voronoi_" + plot_type + ".svg",
    bbox_layout="tight",
)
# plt.show()
