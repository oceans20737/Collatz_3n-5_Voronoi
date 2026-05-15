# **3n+5 問題の幾何学的可視化**

**バイナリ対数らせん空間における Voronoi 分割と 6 系統の安定吸引領域**  

Hiroshi Harada — May 15, 2026

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Document: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

本リポジトリは、$3n+5$ 力学系の軌道構造を **バイナリ対数らせん空間（Binary Logarithmic Spiral Space）** に写像し、**Voronoi 分割** を用いて可視化するプロジェクトです。
本研究では、実際の計算により観測された軌道構造を幾何学的に可視化しています。

---

## **概要 (Overview)**

コラッツ予想（$3n+1$）の加算項を 5 に変更した $3n+5$ 写像では、奇数ステップの「+5」によって 2-adic と 3-adic の干渉 が生じ、軌道が 6 系統の attractor cycles に分岐します。

自然数（1～2000）を以下の極座標へ写像し、Voronoi 分割を適用することで、**6 つの安定吸引領域（Basins of Attraction）** の境界が幾何学的に浮かび上がります。

$r=\log_2(n), \theta = 2\pi(r\bmod 1)$ 

---

## **主な発見 (Key Findings)**

- **6つの attractor cycles** 軌道は最終的に次のいずれかのループに収束し、空間全体を 6 色にタイリングします。
 
  **1, 5, 19, 23, 187, 347**  
  
- **幾何学的骨格（Geometric Skeletons）**  
  19 系列・23 系列では、 $log_2(n)$ の位相差が約 120° となり、 **19-31-49** や **23-29-37** の三角形構造が現れます。

- **高次ループ構造（Higher-Order Loops）**  
  187 系列・347 系列では、 **17 ステップのサブサイクル** が観測され、フラクタル的な局所ネットワークを形成します。

---

## **含まれるスクリプト (Included Scripts)**

- **code_01_3n+5_mandala** — 3n+5 Mandala（全体地図の可視化）  
- **code_02_3n+5_loop** — Loop Overlay（特定 attractor のループをネオン表示）

---

## **動作環境 (Requirements)**

- Python 3.x  
- NumPy  
- Matplotlib  
- SciPy（`scipy.spatial.Voronoi`）

---

## **実行方法 (Usage)**

```bash
# リポジトリのクローン
git clone https://github.com/oceans20737/Collatz_3n+5_Voronoi.git
cd Collatz_3n+5_Voronoi

# 可視化スクリプトの実行
python code_01_3n+5_mandala.py
```

---

## **ライセンス (License)**

- **Research Document / Images:** CC BY 4.0  
- **Source Code:** MIT License  
© 2026 Hiroshi Harada.

---
