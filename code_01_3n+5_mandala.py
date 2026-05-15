# -*- coding: utf-8 -*-
"""code_01_3n+5_mandala.ipynb
"""

# Title: 3n+5 Mandala Visualizer
# Author: Hiroshi Harada
# Date: May 15, 2026
# License: MIT

"""
This script visualizes the 3n+5 dynamical system by mapping natural numbers
onto a binary logarithmic spiral plane and applying Voronoi tessellation.
Each natural number is classified into one of six attractor basins:
    {1, 5, 19, 23, 187, 347}
These basins form the "Six Great Kingdoms" of the 3n+5 universe.
The resulting Voronoi diagram reveals the geometric structure of
their territories in Mandala space.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi
from matplotlib.collections import PolyCollection

# ============================================
# CONFIGURATION
# ============================================
N_DRAW = 20000
N_VORONOI = 60000
DUMMY_POINTS = 100
OUTER_SCALE = 1.3

COLORS = {
    1:   "#FF0000",
    5:   "#0000FF",
    19:  "#00FF00",
    23:  "#FF7F00",
    187: "#8B00FF",
    347: "#FFFF00",
    "Other": "#444444"
}

def hex_to_rgba(hex_color, alpha=1.0):
    """Convert HEX color to RGBA tuple."""
    r = int(hex_color[1:3], 16) / 255
    g = int(hex_color[3:5], 16) / 255
    b = int(hex_color[5:7], 16) / 255
    return (r, g, b, alpha)

# ============================================
# 2-adic Logarithmic Spiral Mapping
# ============================================
def get_spiral_pos(n: int):
    if n <= 0:
        return 0.0, 0.0
    r = np.log2(n)
    theta = 2 * np.pi * (r % 1)
    return r * np.cos(theta), r * np.sin(theta)

# ============================================
# Basin Classification for 3n+5 System
# ============================================
def get_basin_id(n: int, cache: dict):
    if n in cache:
        return cache[n]

    path = []
    curr = n

    while curr not in cache and curr not in path:
        path.append(curr)
        curr = curr // 2 if curr % 2 == 0 else 3 * curr + 5

    if curr in path:
        loop_start = path.index(curr)
        basin_id = min(path[loop_start:])
    else:
        basin_id = cache[curr]

    for p in path:
        cache[p] = basin_id

    return basin_id

# ============================================
# Voronoi Construction
# ============================================
def compute_voronoi():
    points = np.array([get_spiral_pos(i) for i in range(1, N_VORONOI + 1)])
    max_r = np.log2(N_VORONOI)

    theta = np.linspace(0, 2 * np.pi, DUMMY_POINTS, endpoint=False)
    dummy = np.column_stack((max_r * OUTER_SCALE * np.cos(theta),
                             max_r * OUTER_SCALE * np.sin(theta)))

    all_coords = np.vstack((points, dummy))
    return Voronoi(all_coords, qhull_options="QJ")

# ============================================
# Main Visualization
# ============================================
def draw_mandala():
    print("System Radar: Classifying basins...")

    basin_cache = {}
    for i in range(1, N_DRAW + 1):
        get_basin_id(i, basin_cache)

    print("System Radar: Computing Voronoi tessellation...")
    vor = compute_voronoi()

    fig, ax = plt.subplots(figsize=(15, 15), facecolor="black")
    ax.set_aspect("equal")
    ax.set_axis_off()

    polys = []
    facecolors = []

    for i in range(N_DRAW):
        n = i + 1
        bid = basin_cache.get(n, "Other")
        region = vor.regions[vor.point_region[i]]

        if not region or -1 in region:
            polys.append(np.array([[0, 0]]))
            facecolors.append((0, 0, 0, 1.0))
        else:
            polys.append(vor.vertices[region])
            facecolors.append(hex_to_rgba(COLORS.get(bid, COLORS["Other"]), 0.9))

    ax.add_collection(
        PolyCollection(polys, facecolors=facecolors,
                       edgecolors="black", linewidths=0.1)
    )

    for bid in [1, 5, 19, 23, 187, 347]:
        if bid <= N_DRAW:
            x, y = get_spiral_pos(bid)
            ax.text(x, y, str(bid), color="white", fontsize=12,
                    ha="center", va="center", fontweight='bold',
                    bbox=dict(facecolor='black', alpha=0.6, edgecolor='none', pad=1))

    plt.title(f"3n+5 Mandala (N={N_DRAW})",
              color="white", fontsize=22)

    for bid in [1, 5, 19, 23, 187, 347]:
        label = f"Kingdom {bid}" if bid in [1, 5, 19] else f"Empire {bid}"
        plt.scatter([], [], c=COLORS[bid], s=100, label=label)

    plt.legend(loc='upper right', facecolor="#111111",
               labelcolor="white", fontsize=12)

    plt.show()

# ============================================
# Entry Point
# ============================================
if __name__ == "__main__":
    draw_mandala()

