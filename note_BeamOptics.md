---
title: Influence of Emitter Surface Roughness and Emission inhomogeneity
---

## Key components of Gyrotron

- investigate the influence of the quality of the emitter on the quality of electron beam nad gyrotron efficiency
- KIT in house code
  - ESRAY
  - ESPIC
- The nuemerical surface roughness model can be
  - used to simulate the influence of the surface roughness
  - on beam quality, gyrotron efficiency, and mode competition
  - calculated using the surface roughness model
- The emission inhomogeneity information can be
  - evaluated from the measured Current Voltage Characteristics CVCs
  - three methodss to evaluate the emission inhomogeneity from CVC
  - give the new definition of emission inhomogeneity
- Vacuum Electron Device VED
- Electron Beam Optics System EBOS
  - consisit of the MIG and beam tunnels of gyrotron
  - generate a hollow electron beaqm for the cavity with sufficient traverse volicity $v_{T}$

## MIG

MiG type
| Diode                             | Triode                             |
| --------------------------------- | ---------------------------------- |
| ![pic](img/Diagram-Diode-MIG.png) | ![pic](img/Diagram-Triode-MIG.png) |

- MIG ususally, impognated dispenser emitter are used in high power gyrotron
  - Impregnated dispenser emitters are made of porous tungsten impregnated with metal oxides.
  - porous tangsten matrix acts as a reservoir
    - from which the emitting material
    - can diffuse to the surface
    - maintain an active layer
    - provide a low work function for thermionic emission of electrons.
  - B-type / S-type / M-type
- The thermonic emiter will first work under the space charge limited region
  - and the works in saturation region or temperature limited region
  - Under the space charged limited region
    - the current density of parallelplate diode
    - can be described using Child-Languir-eq

$$ \begin{aligned}
    J_{C-L} &= \frac{4\epsilon_0}{9} \sqrt{\frac{2e}{m_e}} \frac{V_0^{3/2}}{d^2} \\
    &= A_{C-L} V_0^{3/2}
\end{aligned} $$

- Dispenser emitter are desighned to work under temperature limited region
- The current density of thermionic emitter unde temperature limited region
  - can be described using Richardson-Dushman-eq with Schottky modification

$$ \begin{aligned}
    J_S &= A_g T^2 e^{ -\frac{W - \Delta W}{k_B T}} \\
    \Delta W &= \frac{e^3 E}{4\pi\epsilon_0}
\end{aligned} $$

- $k_B$ is Boltsmann constant
- $A_g = \lambda_R A_0 A_0$ is universal constant $=1.20173 10^6 Am-2K-2$
- $\lambda_R$ is a material-specific correction effect is typically 0.5
- When to set $\Delta W = 0$,
  - if Schottky effect is not taken into account
  - which means the influence of electric field in neglacted
