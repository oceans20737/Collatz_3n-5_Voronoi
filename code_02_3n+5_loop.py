# -*- coding: utf-8 -*-
"""code_02_3n+5_loop.ipynb
"""

# Title: 3n+5 Mandala Visualizer (Loop Overlay Edition)
# Author: Hiroshi Harada
# Date: May 15, 2026
# License: MIT

"""
This script visualizes the attractor loops of the 3n+5 dynamical system
on the binary logarithmic spiral plane, with Voronoi
tessellation as the geometric background.
The overlay highlights the closed orbit (loop) of a chosen attractor
(e.g., 19, 23, 187, 347), rendered as a glowing neon trajectory.
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
MAX_LOOP_STEPS = 20000   # 安全装置

COLORS = {
    1:   "#FF0000",
    5:   "#0000FF",
    19:  "#00FF00",
    23:  "#FF7F00",
    187: "#8B00FF",
    347: "#FFFF00",
    "Other": "#444444"
}

# ============================================
# Utility
# ============================================
def hex_to_rgba(hex_color, alpha=1.0):
    r = int(hex_color[1:3], 16) / 255
    g = int(hex_color[3:5], 16) / 255
    b = int(hex_color[5:7], 16) / 255
    return (r, g, b, alpha)

# ============================================
# Core Engine
# ============================================
def get_spiral_pos(n: int):
    if n <= 0:
        return 0.0, 0.0
    r = np.log2(n)
    theta = 2 * np.pi * (r % 1)
    return r * np.cos(theta), r * np.sin(theta)

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

def compute_voronoi():
    points = np.array([get_spiral_pos(i) for i in range(1, N_VORONOI + 1)])
    max_r = np.log2(N_VORONOI)

    theta = np.linspace(0, 2 * np.pi, DUMMY_POINTS, endpoint=False)
    dummy = np.column_stack((max_r * OUTER_SCALE * np.cos(theta),
                             max_r * OUTER_SCALE * np.sin(theta)))

    all_coords = np.vstack((points, dummy))
    return Voronoi(all_coords, qhull_options="QJ")

# ============================================
# Loop Extraction
# ============================================
def get_loop_orbit(start_n: int):
    """
    Extract the closed orbit starting from start_n.
    Safety limit prevents infinite wandering.
    """
    path = []
    curr = start_n

    for _ in range(MAX_LOOP_STEPS):
        if curr in path:
            path.append(curr)  # close loop
            return path
        path.append(curr)
        curr = curr // 2 if curr % 2 == 0 else 3 * curr + 5

    raise RuntimeError("Loop did not close within MAX_LOOP_STEPS.")

def draw_orbit_overlay(ax, path, base_color):
    coords = [get_spiral_pos(p) for p in path]
    x = [c[0] for c in coords]
    y = [c[1] for c in coords]

    # Glow layers
    ax.plot(x, y, color=base_color, linewidth=12, alpha=0.2, zorder=3)
    ax.plot(x, y, color=base_color, linewidth=6, alpha=0.4, zorder=4)

    # Core line
    ax.plot(x, y, color="white", linewidth=1.5, zorder=5)

    # Nodes
    ax.scatter(x, y, color="white", edgecolor=base_color, s=40, zorder=6)

# ============================================
# Main Visualization
# ============================================
def draw_mandala(target_attractor=None):
    print("Classifying basins...")
    basin_cache = {}

    for i in range(1, N_DRAW + 1):
        get_basin_id(i, basin_cache)

    print("Computing Voronoi...")
    vor = compute_voronoi()

    fig, ax = plt.subplots(figsize=(15, 15), facecolor="black")
    ax.set_aspect("equal")
    ax.set_axis_off()

    polys, facecolors = [], []

    for i in range(N_DRAW):
        n = i + 1
        bid = basin_cache.get(n, "Other")
        region = vor.regions[vor.point_region[i]]

        alpha_val = 0.9 if target_attractor is None or target_attractor == bid else 0.2

        if not region or -1 in region:
            polys.append(np.array([[0, 0]]))
            facecolors.append((0, 0, 0, 1.0))
        else:
            polys.append(vor.vertices[region])
            facecolors.append(hex_to_rgba(COLORS.get(bid, COLORS["Other"]), alpha_val))

    ax.add_collection(PolyCollection(polys, facecolors=facecolors,
                                     edgecolors="black", linewidths=0.1))

    # Overlay loop
    if target_attractor:
        loop_path = get_loop_orbit(target_attractor)
        draw_orbit_overlay(ax, loop_path, COLORS[target_attractor])

    # Label capitals
    for bid in [1, 5, 19, 23, 187, 347]:
        if bid <= N_DRAW:
            x, y = get_spiral_pos(bid)
            ax.text(x, y, str(bid), color="white", fontsize=12,
                    ha="center", va="center", fontweight='bold',
                    bbox=dict(facecolor='black', alpha=0.6, edgecolor='none', pad=1))

    title_suffix = "Full View" if not target_attractor else f"Attractor {target_attractor} Loop"
    plt.title(f"3n+5 Mandala — {title_suffix}", color="white", fontsize=22)
    plt.show()

if __name__ == "__main__":
    # t = 1, 5, 19, 23, 187, or 347
    t = 19
    draw_mandala(target_attractor = t)

