---
title: GSMAC-FEM
---

- [1. GSMAC-2D](#1-gsmac-2d)
  - [1.1. Digit](#11-digit)

## 1. GSMAC-2D

### 1.1. Digit

2D-Cartesianでの方程式群

1. $$ \frac{ \tilde{u} - u^n}{\delta t} = - \frac{\partial H^n}{\partial x}  + u^n \omega^n - \frac{1}{Gr}\frac{\partial\omega^n}{\partial y} $$
2. $$ \frac{ \tilde{u} - v^n}{\delta t} = - \frac{\partial H^n}{\partial x}  + v^n \omega^n - \frac{1}{Gr}[ \theta^n + \frac{\partial\omega^n}{\partial x} ] $$
3. $$ \omega^n = \frac{\partial v^n}{\partial x} - \frac{\partial u^n}{\partial y} $$
4. $$ -\frac{1}{\lambda} \frac{\delta\phi}{\delta\tau} = \nabla \cdot \tilde{v} - \nabla^2\phi $$
5. $$ \phi = H^*\delta t $$
6. $$ H^{n+1} = H^n + H^* $$
7. $$ \frac{ u^{n+1} - \tilde{u}}{\delta t} = - \frac{\partial H^*}{\partial x} $$
8. $$ \frac{ v^{n+1} - \tilde{v}}{\delta t} = - \frac{\partial H^*}{\partial y} $$
9. $$ \frac{\theta^{n+1} - \theta^n}{\delta t} + u^{n+1}\frac{\partial\theta^n}{\partial x} + v^{n+1}\frac{\partial\theta^n}{\partial y} = \frac{1}{Ra} [ \frac{\partial^2\theta^n}{\partial x^2} + \frac{\partial^2\theta^n}{\partial y^2} ] $$

u,vは流速ベクトルの成分。$\omega$は渦度。9方程式に対してGalerkin法を用いて有限要素式を導出する。

重み関数として固定境界$\Gamma_1$,$\Gamma_3$において0となるような関数$\delta u$,$\delta v$,$\delta\theta$と要素内一定の関数$\delta\omega$,$\delta\phi$と考える。

1. $$ \int_{\Omega^e} \delta u \frac{ \tilde{u} - u^n}{\delta t} d\Omega^e = \int_{\Omega^e} H^n \frac{\partial(\delta u)}{\partial x} d\Omega^e + \int_{\Omega^e} \delta uv^n\omega^n d\Omega^e + \frac{1}{Gr}\int_{\Omega^e} \omega^n \frac{\partial(\delta u)}{\partial y} d\Omega^e - \int_{\Gamma^{2e}} \delta u (H^nl + \frac{1}{Gr} \omega^nm) d\Gamma^{2e}$$
2. $$ \int_{\Omega^e} \delta v \frac{ \tilde{v} - v^n}{\delta t} d\Omega^e = \int_{\Omega^e} H^n \frac{\partial(\delta v)}{\partial y} d\Omega^e + \int_{\Omega^e} \delta vu^n\omega^n d\Omega^e - \frac{1}{Gr}\int_{\Omega^e} \omega^n \frac{\partial(\delta v)}{\partial x} d\Omega^e - \int_{\Gamma^{4e}} \delta v (H^nm + \frac{1}{Gr} \omega^nl) d\Gamma^{4e} + \frac{1}{Gr} \int_{\Omega^e} \delta v \theta^n d\Omega^e $$
3. $$ \omega^n = \frac{1}{S^e} \int_{\Gamma^e} (v^nl - u^nm) d\Gamma^e $$
4. $$ \phi^{k+1} = \phi^k - \lambda \frac{\delta\tau}{S^e} \int_{\Gamma^e} [ \tilde{v}\cdot n - \frac{\partial\phi^k}{\partial n} ] d\Gamma^e $$
5. $$ \int_{\Omega^e} \delta u \frac{u^{n+1} - \tilde{u}}{\delta t} d\Omega^e = \int_{\Omega^e} H^* \frac{\partial(\delta u)}{\partial x} d\Omega^e $$
6. $$ \int_{\Omega^e} \delta u \frac{v^{n+1} - \tilde{v}}{\delta t} d\Omega^e = \int_{\Omega^e} H^* \frac{\partial(\delta v)}{\partial y} d\Omega^e $$
7. $$ \int_{\Omega^e} \delta\theta \frac{\theta^{n+1} - \theta^n}{\delta t} d\Omega^e + \int_{\Omega^e} \delta\theta u^{n+1}\frac{\partial\theta^n}{\partial x} d\Omega^e + \int_{\Omega^e} \delta\theta v^{n+1}\frac{\partial\theta^n}{\partial y} d\Omega^e = -\frac{1}{Ra} \int_{\Omega^e} [ \frac{\partial(\delta\theta)}{\partial x} \frac{\partial\theta^n}{\partial x} + \frac{\partial(\delta\theta)}{\partial y} \frac{\partial\theta^n}{\partial y} ] d\Omega^e + \frac{1}{Ra} \int_{\Gamma^{6e}} \frac{\partial\theta}{\partial n} \delta\theta d\Gamma^{6e} $$
