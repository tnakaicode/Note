# newFASANT

- [HOME](https://www.fasant.com/)

<https://www.fasant.com/en/products/mom?ref=footer>

3D analysis of complex and on board antennas, electromagnetic compatibility and RCS.

MOM is a parallelized computer tool for the 3D analysis of complex antennas, on board antennas, electromagnetic compatibility and radar cross section (RCS).

It is based on the Moment Method (MM) with FMLMP (Fast Multilevel Multipole) and provides excellent results. Macro basis functions (CBFs) and Domain Decomposition Technique are also included in order to increase the efficiency. Also, provides functionalities to dynamic and parametric simulations.

MOMは、複雑なアンテナ、オンボードアンテナ、電磁適合性、レーダー断面積（RCS）の3D解析のための並列化されたコンピューターツールです。
FMLMP（Fast Multilevel Multipole）を使用したモーメント法（MM）に基づいており、優れた結果を提供します。効率を高めるために、マクロ基底関数（CBF）とドメイン分解手法も含まれています。また、動的およびパラメトリックシミュレーションに機能を提供します。

```markdown
git clone https://github.com/Gjacquenot/Puma-EM.git
git clone https://github.com/hpddm/hpddm.git
```

Macro basis functions CBFs  
<https://www.e-fermat.org/files/articles/1536cfcaaae952.pdf>  
<http://www.ursi.org.tr/2008-EWS/ews_2008.pdf>

<https://www.fasant.com/products/parametrizing-the-geometries>

Parameterize your geometries to define different scenarios over the same original geometry.  
newFASANT allows to parametrize our geometries in order to be able to define different scenarios by assigning several parametric values over the same original geometry.  
ジオメトリをパラメータ化して、同じ元のジオメトリ上で異なるシナリオを定義します。  
newFASANTを使用すると、同じ元のジオメトリに複数のパラメータ値を割り当てることにより、さまざまなシナリオを定義できるようにジオメトリをパラメータ化できます。

The user can set the array of values through three different ways:

- Implicit linear values
- Range of linear values
- Values defined by functions.
- Once the simulation has finished, the user can visualize the results for each step or simulation.

This feature allows to analyze parametric and dynamic simulations, comprising scenarios where some objects and/or antennas can change their position over time. The most important advantages of this functionality are the automatic generation of the different scenarios to launch the corresponding simulations and the ability to compare the results obtained for different parametric values.  
この機能により、パラメトリックおよび動的シミュレーションを分析できます。これには、一部のオブジェクトやアンテナが時間とともに位置を変更できるシナリオが含まれます。この機能の最も重要な利点は、対応するシミュレーションを起動するためのさまざまなシナリオの自動生成と、さまざまなパラメーター値で得られた結果を比較する機能です。
