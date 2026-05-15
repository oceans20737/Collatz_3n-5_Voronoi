# **Geometric Visualization of the 3n+5 Problem**

**Voronoi Tessellation and Six Stable Basins of Attraction in Binary Logarithmic Spiral Space**  

Hiroshi Harada — May 15, 2026

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20208731.svg)](https://doi.org/10.5281/zenodo.20208731)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Document: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This repository is a project to map the orbital structure of the $3n+5$ dynamical system into a **Binary Logarithmic Spiral Space** and visualize it using **Voronoi tessellation**. This study geometrically visualizes the orbital structures observed through actual computational analysis.

---

## **Overview**

In the $3n+5$ map, modifying the addition term of the Collatz conjecture ($3n+1$) to 5 introduces interference between 2-adic and 3-adic properties due to the "+5" at odd steps. This causes the orbits to branch into six distinct attractor cycles.

By mapping natural numbers (1 to 2000) to the following polar coordinates and applying Voronoi tessellation, the boundaries of the **six stable basins of attraction** emerge geometrically.

$r=\log_2(n), \theta = 2\pi(r\bmod 1)$ 

---

## **Key Findings**

- **Six attractor cycles:** Orbits ultimately converge to one of the following loops, tiling the entire space in six colors.
  
  **1, 5, 19, 23, 187, 347**  
  
- **Geometric Skeletons:**  
  In the 19-series and 23-series, the phase difference of $\log_2(n)$ is approximately 120°, revealing triangular structures such as **19-31-49** and **23-29-37**.

- **Higher-Order Loops:**  
  In the 187-series and 347-series, **17-step subcycles** are observed, forming fractal-like local networks.

---

## **Included Scripts**

- **code_01_3n+5_mandala** — 3n+5 Mandala (Visualization of the global map)  
- **code_02_3n+5_loop** — Loop Overlay (Neon visualization of specific attractor loops)

---

## **Requirements**

- Python 3.x  
- NumPy  
- Matplotlib  
- SciPy (`scipy.spatial.Voronoi`)

---

## **Usage**

```bash
# Clone the repository
git clone [https://github.com/oceans20737/Collatz_3n+5_Voronoi.git](https://github.com/oceans20737/Collatz_3n+5_Voronoi.git)
cd Collatz_3n+5_Voronoi

# Run the visualization script
python code_01_3n+5_mandala.py

```

---

## **License**

* **Research Document / Images:** CC BY 4.0
* **Source Code:** MIT License

© 2026 Hiroshi Harada.

---
