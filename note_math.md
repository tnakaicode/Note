---
title: Math
---

- [1. Symbol Perturbation method](#1-symbol-perturbation-method)
- [2. Generalized error analysis of regenerating kernel Hilbert space Gaussian process regression](#2-generalized-error-analysis-of-regenerating-kernel-hilbert-space-gaussian-process-regression)
- [3. Table](#3-table)
- [4. Numerical integration](#4-numerical-integration)

$$ k_{\preceq}, k_{\parallel} $$

$$ \int_0 ^\infty \frac{1}{1 + x^2} \frac{1}{1 + x^N} dx $$

$$\begin{aligned}
  I
  &=& \int_0^\infty \frac{u^N}{(1+u^2)(1+u^N)} du \\
  &=& \int_0^\infty \frac{1 - 1 +u^N}{(1+u^2)(1+u^N)} du \\
  &=& - I + \int_0^\infty \frac{1}{(1+u^2)} du \\
  &=& - I + \frac{\pi}{2}
\end{aligned}$$

Maxwell-eq
$$\begin{aligned}
  \nabla \cdot u &= 0 \\
  \mathrm{rot} \vec{E} &= - \frac{1}{c} \frac{\partial \vec{B}}{\partial t} \\
  \mathrm{div} \vec{B} &= 0 \\
  \mathrm{rot} \vec{B} &= \frac{1}{c} \frac{\partial \vec{E}}{\partial t} + \frac{4\pi}{c} \vec{j} \\
  \mathrm{div} \vec{E} &= 4 \pi \rho_{\varepsilon }
\end{aligned}$$

Rotation
$$\begin{aligned}
  \mathrm{rot}{\bm H}({\bm r},t)
  &= \nabla \times {\bm H}({\bm r},t), \\
  &=\begin{vmatrix}
    {\bm e}_{x} & {\bm e}_{y} & {\bm e}_{z}\\
    \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{partial}{\partial z}\\
    H_{x}({\bm r},t) & H_{y}({\bm r},t) & H_{z}({\bm r},t)
  \end{vmatrix}
\end{aligned}$$

Laplacian
$$\begin{aligned}
  \bigtriangleup
  &\equiv \left( \frac{\partial^2}{\partial x^2} +\frac{\partial^2}{\partial y^2} +\frac{\partial^2}{\partial z^2}\right) \\
  &= \nabla^2 \\
  &= \mathrm{div}\cdot\mathrm{grad}.
\end{aligned} $$

$$ z = x+\mathrm{i}y = r\mathrm{e}^{+\mathrm{i}\theta} = r\left(\cos(\theta) + \mathrm{i}\sin(\theta)\right)$$
$$ \bar z = x - \mathrm{i}y = r\mathrm{e}^{-\mathrm{i}\theta} = r\left(\cos(\theta) - \mathrm{i}\sin(\theta)\right)$$
$$ \mathrm{e}^{\mathrm{i}\theta} = \cos(\theta) + \mathrm{i}\sin(\theta)$$
$$ \cos(\theta) = \frac{\mathrm{e}^{\mathrm{i}\theta} + \mathrm{e}^{-\mathrm{i}\theta}}{2}$$
$$ \sin(\theta) = \frac{\mathrm{e}^{\mathrm{i}\theta} - \mathrm{e}^{-\mathrm{i}\theta}}{2\mathrm{i}}$$
$$\mathrm{e}^{x} = \cosh(x)+\sinh(x)$$
$$\mathrm{e}^{-x} = \cosh(x)-\sinh(x)$$
$$\cosh(x) = \dfrac{\mathrm{e}^{x}+\mathrm{e}^{-x}}{2}$$
$$\sinh(x) = \dfrac{\mathrm{e}^{x}-\mathrm{e}^{-x}}{2}$$
$$\tanh(x) = \dfrac{\sinh(x)}{\cosh(x)} = \dfrac{\mathrm{e}^{x} - \mathrm{e}^{-x}}{\mathrm{e}^{x} + \mathrm{e}^{-x}}$$

## 1. Symbol Perturbation method

It is determined how many points are required to define a single curve. The case where more points than the number are on the curve is called degeneration.  
It is natural to think that the input includes degeneration. In particular, if all the input points are grid points, many points will be on a straight line.  
Basically, the algorithm is designed in consideration of the degeneration, but when the degeneration is considered, the division is complicated, and it becomes more difficult to verify the validity of the algorithm. There is a perturbation method as a method for solving this.  
It is good to move all the points to eliminate the shrinkage in order to eliminate the shrinkage. However, if the points are moved too much, the set of points has a different topology from the original set of points.  
In addition, even if the user can move without changing the topology, another degeneration may occur.  
Further, it is important to make the moving distance minute, but if it is made too small, another problem is caused due to calculation errors.  
If a calculation time overhead is allowed, there is a calculation method having the same effect as effectively moving by a minute distance. (Symbol perturbation method)  

1つの曲線を定義するのに必要な点の数を決める。その数より多くの点が曲線上にある場合をディジェネレーションと呼ぶ。  
入力に縮退が含まれていると考えるのは自然である。特に、入力点がすべて格子点であれば、直線上にある点が多くなる。  
基本的には縮退を考慮してアルゴリズムを設計するが、縮退を考慮すると分割が複雑になり、アルゴリズムの妥当性を検証するのが難しくなる。これを解決する方法として摂動法がある。  
縮退を解消するためには全ての点を移動させるのが良い。しかし、点を移動させすぎると、元の点集合とは異なるトポロジーを持つ点集合になってしまう。  
また、トポロジーを変えずに移動できたとしても、別の縮退が発生する可能性がある。  
さらに、移動距離を微小にすることが重要であるが、微小にしすぎると計算誤差による別の問題が発生する。  
計算時間のオーバーヘッドが許されるのであれば、実質的に微小距離の移動と同じ効果を持つ計算方法がある。(記号摂動法）  

Consider a symbol perturbation method to avoid the degeneracy that three points are arranged on the same straight line.  
Given n points $p_1(x_1,y_1),p_2(x_2,y_2),...,p_n(x_n,y_n)$, each point $p_i(x_i,y_i)$ is converted to Move to $p_i^*$.  
  
$$ p_i^* (x_i + \epsilon^{M^i}, y_i + \epsilon^{M^i}) $$
  
Here, $M$ is a sufficiently large positive integer.  

## 2. Generalized error analysis of regenerating kernel Hilbert space Gaussian process regression

Let the topological space $\Chi = \mathbb{R}^d$ be the input space. The normal distribution with mean $\mu\in\mathbb{R}$ and variance $\sigma^2\ge0$ on R is given by the density function $p(x)$.
$$ p (x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp(-\frac{(x-\mu)^2}{2\sigma^2}) $$
When $\sigma = 0$, it is a Dirac measure on the order of $\mu$.

## 3. Table

| Symbol            |                 |                    |                  |
| ----------------- | --------------- | ------------------ | ---------------- |
| $\pm$             | \pm             | $\mp$              | \mp              |
| $\leq$            | \leq            | $\geq$             | \geq             |
| $\sim$            | \sim            | $\simeq$           | \simeq           |
| $\approx$         | \approx         |                    |                  |
| $\neq$            | \neq            | $\equiv$           | \equiv           |
| $\propto$         | \propto         | $\infty$           | \infty           |
| $\partial$        | \partial        | $\nabla$           | \nabla           |
| $\perp$           | \perp           | $\parallel$        | \parallel        |
| $\times$          | \times          | $\div$             | \div             |
| $\cdot$           | \cdot           |                    |                  |
| $\star$           | \star           | $\ast$             | \ast             |
| $\circ$           | \circ           | $\bullet$          | \bullet          |
| $\diamond$        | \diamond        |                    |                  |
| $\triangle$       | \triangle       | $\triangledown$    | \triangledown    |
| $\bigtriangleup$  | \bigtriangleup  | $\bigtriangledown$ | \bigtriangledown |
| $\square$         | \square         | $\bigcirc$         | \bigcirc         |
| $\leftarrow$      | \leftarrow      | $\rightarrow$      | \rightarrow      |
| $\Leftarrow$      | \Leftarrow      | $\Rightarrow$      | \Rightarrow      |
| $\leftrightarrow$ | \leftrightarrow | $\Leftrightarrow$  | \Leftrightarrow  |
| $\longleftarrow$  | \longleftarrow  | $\longrightarrow$  | \longrightarrow  |
| $\Longleftarrow$  | \Longleftarrow  | $\Longrightarrow$  | \Longrightarrow  |
| $\uparrow$        | \uparrow        | $\downarrow$       | \downarrow       |
| $\Uparrow$        | \Uparrow        | $\Downarrow$       | \Downarrow       |
| $\updownarrow$    | \updownarrow    | $\Updownarrow$     | \Updownarrow     |
| $\nearrow$        | \nearrow        | $\searrow$         | \searrow         |
| $\swarrow$        | \swarrow        | $\nwarrow$         | \nwarrow         |
| $\angle$          | \angle          |                    |                  |
| $\flat$           | \flat           |                    |                  |
| $\natural$        | \natural        | $\sharp$           | \sharp           |
| $\backslash$      | \backslash      |                    |                  |
| $\clubsuit$       | \clubsuit       | $\diamondsuit$     | \diamondsuit     |
| $\heartsuit$      | \heartsuit      | $\spadesuit$       | \spadesuit       |
| $\dagger$         | \dagger         |

## 4. Numerical integration

- 積分
  - 分子積分
    - QCC-on-QCs
    - 古典コンピュータでは事前計算
    - 量子コンピュータで高速計算
    - FC法
  - ガウス型関数
    - 多中心積分に公式が使える
    - 精度を上げるためにDZ, TZ, QZ,と基底関数を増やす
    - 原点で微分が0
      - 原子核の可スプ条件を満たさない
    - 台形公式
    - Logメッシュ(実空間の場合)
  - 6次シンプレクティック積分器
