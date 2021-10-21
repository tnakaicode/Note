---
title: NOTE for MoM
---

## Efficient computation techniques for Galerkin MoM antennadesign

- implementeda FORTRAN programreferredto as Galerkin Method of Moments with Exact Kernel(GEKMoM) to calculate the current distribution
- good agreement between the current computedby using the described numerical scheme (namely\GEKMoM"), the commercial software NEC4:1
- Thenumerical method presented has been implemented in a FORTRAN code referred to as Galerkin Method of Moments for Open Surface(GMoMOS) and used for the evaluation of the surface current distribution of open surfaces
- implemented in a FORTRAN computer code referred to as GEKMoM+ which is able to calculate the current on the perfectly electrically conducting surface(PEC) and along the PEC wire including the case of a wire perpendicularly connected to a planar surface.
  - Severaltestcaseshave beenrunto validatethecode
- in this the sisanecient GalerkinMethod of Moments (MoM)hasbeendescribedto cal-culatetheelectriccurrent distributionalongwireantennasas wellas onplanarsurfacesincludingwire-to-surfacejunctions.Thetheoreticalformulationpresentedhasbeenimple-mentedin a FORTRANcomputerlanguageprogramwhich hasbeensuccessfullyvalidatedwithresultsfromtheliterature.
- Thekeyelements of thiselectromagneticmodelingtool,each onecorrespondingto a FORTRANmodule
  - arbitrarilyorientedloadedwires
  - opensurfaces
  - connectionof wireswithsurfaces

この方程式では、散乱された電界は、未知の電流分布（任意の方向に向けられた線材、表面、あるいは線材と表面の接合部）の関数として記述されます。
次に、ガラーキンモーメント法を用いて大域方程式を離散化し、関連するシステムマトリクス方程式（ZI=F）を導き出しました。
ガラーキン法のおかげで、MoMmatrixZは非対称性を保持しています。
Zの各要素は、"Source "要素と "Observation "要素の間の電流の影響を表しています。
要素とは、線、面開き、線と面の接合部を流れる電流を近似するために必要な基底関数の支持体と読み替える必要があります。
さらに、対角線上にある行列要素、いわゆるedselftermsは、同一線源と観測要素の間の電磁的相互作用を表しています。
このような場合、整数は特異な挙動を示す可能性があり、特に注意が必要です。
まず、直線状の細線に対して、最も重要な2つの細線方程式を定式化しました。
それは、Pocklingtone方程式のhexactとhrucedkernelです。
我々は、特異点抽出とランデントランスフォームを行うことにより、その結果のシステム行列の要素を簡単に計算する方法を議論した。
また、実装された離散化法の精度を調べるために二乗平均平方根(RMS)誤差を測定しましたが、拡張関数の数を増やすと、正確なカーネル変換では安定した計算結果が得られます。
さらに、負荷線にまで解析を広げ、向きの異なる複数の線の間でのエレキ磁気相互作用についても検討した。
一般に、線間のカップリングを検討する場合、2つのアプローチが考えられる。
実は、電源線に流れる電流は、他のすべての観測線を照らす電波を放射しているのです。
最初のケースでは、放射されたエルドを評価するために、ワイヤー軸上に1次元の積分が必要であり（いわゆるシン・ワイヤー・ファー・エルド近似）、この2つのケースでは、ワイヤーマントル上に追加の積分が必要であり、複雑さは2次元に増加します。
さらに、線軸上に放射電流を配置することで発生する平均二乗根誤差は、GEKMo法で発生する離散化誤差よりも小さいことを確認しました。
また，ワイヤの外周に沿って電流を推定するアプローチでは，必要なCPU時間を短縮するために，数値解析可能な補間アルゴリズムを開発しました。
数値解析の結果，提案された補間アルゴリズムは，ワイヤ内の遠距離近似法と比較してCPU時間を短縮できることが実証されました。
結論と推奨事項187数値計算法（GEKMoM）を拡張して，負荷のかかった直線型ワイヤの自然周波数を決定しました。
一般的に、Singularity Expansion Method (SEM)は、負荷のかかった線材の電磁的挙動を固有周波数で特徴付けるための便利な手段を提供します。
自然周波数はシステムマトリクスが特異である複雑な周波数に対応していることから、システムマトリクスのSingularValueDecomposition(SVD)を行うことで、その評価を計算する数値アルゴリズムを提示しました。
SVDは、自然周波数に加えて、時間領域の電流分布を特徴づけるのに有用な多くの情報を生成するため、この方法は、従来の方法に代わる魅力的な手法です。
さらに、抵抗負荷のかかった電線では、負荷の値を増加させたときに極の位置がどのように複雑な計画の中で変化するかを示していますが、マーチング・オン・ローディング法を提示し、その検証に成功しています。
実際、予想されたように、結果は、自然周波数の共役が軸方向に移動し、単一の値になるまで衝突することを示している（つまり、二重極が発生する）。
また、既存の文献[16{19]を参考にして、表面上の電流分布を計算する簡便な数値計算法を示しました。
この場合、MoMmatrix要素の評価には、integrablesingularitiesをintegrandsとする積分の計算が含まれます。
開発された方法では、すべての特異点を抽出し、その結果の積分を閉形式で計算し、数値積分は正則関数にのみ適用されます。
開放面に対して、開発されたソフトウェアはGMoMOSと名付けられました。
また、ワイヤアンテナと開放面の間の電磁結合を解析するための数値計算手法を提案しました。
また、ワイヤーアンテナと表面の間の電磁結合を解析するための数値計算法を提案した。
さらに、ソースポイントとオブザベーションポイントが一致する場合、積分は特異な挙動を示します。
解析的手法を用いて、すべてのintegrablesingularitiesを説明し、4次元の積分を低次元化しました。
この数値的な複雑さの減少は、計算時間の短縮につながります。
コードが十分に最適化されていないにもかかわらず、結果は提案された方法の成功を証明しています。
統合評価のための専用（アドホック）ルーチンを実装することで、提案された数値処理の効率が向上する可能性があります。
また、今回の研究では、さらなる数値処理を行う上で、特殊基底関数が満たすべき条件を明らかにしたことで、アタッチメント・モードへの対応についても経験を深めることができました。
このツールは、海軍の通信機器に使用されているHF-VHFアンテナの合成と設計の出発点となるものです。
そのために、アンテナ解析ソフトウェア（GEKMoM）は、Particle Swarm Optimization（PSO）アルゴリズムに組み込まれています。
この統計的なアルゴリズムは、タスクで定義された望ましいアンテナの性能を満たすアンテナを探索します。
さらに、我々は提案されたGEKMoM/PSOアルゴリズムの行列要素の計算効率を向上させるための調整方法を説明しました。
進化的（確率的）最適化手法と決定論的最適化手法のハイブリッドにより、改善される可能性があります。
また、今後の展開としては、カイトアンテナやホイップアンテナなどの複雑な構造を解析するためには、これらの要素が欠落しているため、ワイヤー間の接続を含めて検討することをお勧めします。
これにより、複雑な環境に設置されたワイヤ ーアンテナの合成・設計に必要な数値計算コードの利便性が 向上します。
また、導電面に設置されるアンテナの設計（船上でのアンテナ性能）を考慮すると、インターポール・アルゴリズムを使用することで、最適化プロセスが効率化され、ワイヤ・サーフェイス・カップリング・マトリクスの計算時間が大幅に短縮される可能性がありますが、その可能性についても研究を進めることができます。
しかし、パラメータの数が多くなると、最適化の時間が長くなってしまいます。
実際、最適化装置が良い解を得るための収束は、解のゲージスペースによって制限されます。
例えば、アンテナの設置位置を少し変更しただけで、ほとんどの相互作用は影響を受けないため、更新する行列要素の数は少なくて済みます。
しかし、この興味深いアイデアは、行列要素のほとんどを変更しないようにしたいという我々の考えをメッシュジェネレータが認識し、それに従って行動する場合にのみ、大幅なCPU削減につながります。

```bash
git clone https://github.com/ljvmiranda921/pyswarms.git
gti clone https://github.com/tnakaicode/for90-mom2.git
```

## Moment of Method in electromagnetics

- <https://github.com/topics/method-of-moments>
  - <https://github.com/steverab/tensor-gmm.git>
  - <https://github.com/RedBlight/EFVIE-MoM.git>
  - <https://github.com/eattardo/efie-2d.git>
  - <https://github.com/michaelprichardson/mom_python.git>
  - <https://github.com/EhsanKA/Mixture_MMSD.git>
- <http://www.lmn.pub.ro/~daniel/ElectromagneticModelingDoctoral/Books/BEM%20MoM/Gibson%20MoM%20in%20Electromagnetics.pdf>
- <https://dev.tvbox.am/meouen/method-of-moments-electromagnetics-python>
- <https://www.matecdev.com/posts/differences-fdtd-fem-mom.html>
- <http://www.e-em.co.jp/index.html>
  - EEM-FDM Ver.5.1
    - 差分法を用いた電磁界シミュレーター
    - 広い周波数(準静電界から光まで)の各種用途に使える汎用ツール
  - EEM-MOM Ver.5.2
    - モーメント法を用いた電磁界シミュレーター
    - 線状・面状アンテナの解析に最適
  - EEM-RTM Ver.5.1
    - レイトレーシング法を用いた電波伝搬シミュレーター
    - 市街地や建物内の広い領域での電界分布の高速計算
  - EEM-STF Ver.5.1
    - 差分法による静電界シミュレーター
    - 電極と誘電体から成る系の電圧と電界分布の計算
  - OpenFDTD Ver.2.6.3 new
    - FDTD法を用いた電磁界シミュレーター
    - 電磁界の各種用途に使える高速汎用ツール
  - OpenTHFD Ver.1.4.3 new
    - 差分法を用いた電磁界シミュレーター
    - 電磁界の広い周波数(準静電界から光まで)の各種用途に使える汎用ツール
  - OpenMOM Ver.1.9.1
    - モーメント法を用いた電磁界シミュレーター
    - 線状・面状アンテナの解析に最適
  - OpenSTF Ver.1.7.1
    - 差分法による静電界シミュレーター
    - 電極と誘電体から成る系の電圧と電界分布の計算

- FDTD    / Differential equation / Volumetric domain / Non-linear, anisotropic
- FEM     / Variational form      / Volumetric domain / Non-linear, anisotropic, multi-physics
- MoM/BEM / Integral equations    / Surface currents  / Linear, piecewise homogeneous

FDTD/FEM/BEM(MoM)
|           |       |                     |                     |                        |                  |
| --------- | ----- | ------------------- | ------------------- | ---------------------- | ---------------- |
| **FDTD**  |       |                     |                     |                        |                  |
| Meep      | GPL   | C++                 | Python, Scheme, C++ |                        | MPI              |
| gprMax    | GPL   | Python+Cython       | Python              |                        | CUDA, MPI        |
| OpenEMS   | GPL   | C++                 | Matlab/Octave       |                        | MPI              |
| **FEM**   |       |                     |                     |                        |                  |
| FEniCS    | LGPL  | C++                 | Python, C++         |                        | MPI              |
| Elmer FEM | LGPL  | Fortran             |                     |                        | MPI              |
| FreeFEM   | LGPL  | C++                 | Own language        |                        | MPI              |
| **MoM**   |       |                     |                     |                        |                  |
| Bempp     | MIT   | Python+OpenCL/Numba | Python, C++         | Gmsh, meshio           | Shared memory    |
| PumaEM    | GPLv3 | Python/C++          | Python              | Gmsh, GiD, Ansys, VRML | MPI              |
| NEC-2     | GPLv2 | C++                 | C/C++/Python/Ruby   | Antenna parameters     | Single-threaded? |
