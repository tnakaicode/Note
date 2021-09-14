---
title: Meep
---

## 1. Meep

Meep implements the finite-difference time-domain (FDTD) method for computational electromagnetics. This is a widely used technique in which space is divided into a discrete grid and the fields are evolved in time using discrete time steps — as the grid and the time steps are made finer and finer, this becomes a closer and closer approximation for the true continuous equations, and one can simulate many practical problems essentially exactly.

This section introduces the equations and the electromagnetic units employed by Meep, the FDTD method, and Meep's approach to FDTD. Also, FDTD is only one of several useful methods in computational electromagnetics, each of which has their own special uses — a few of the other methods are mentioned, and some hints are provided as to which applications FDTD is well suited for and when you should potentially consider a different method.

This introduction does not describe the Python Interface with which you set up simulations. Instead, the focus here is on the physics and numerical methods. For tutorial examples which demonstrate core functionality, see Tutorial/Basics and the Simpetus projects page.

Since only a finite region of space can be simulated, the simulation must always be terminated with some boundary conditions. Three basic types of terminations are supported in Meep: Bloch-periodic boundaries, metallic walls, and PML absorbing layers. Also, one can exploit symmetries of a problem to further reduce the computational requirements.

With ordinary periodic boundaries in a cell of size L, the field components satisfy f(x+L)=f(x). Bloch periodicity is a generalization where f(x+L)=eikxLf(x) for some Bloch wavevector k. This can be used to solve for the modes of waveguides, gratings, and so on, much like in MPB. See Chapter 3 of Photonic Crystals: Molding the Flow of Light (second edition).

An even simpler boundary condition is a metallic wall, where the fields are simply forced to be zero on the boundaries, as if the cell were surrounded by a perfect metal (zero absorption, zero skin depth). More generally, you can place perfect metal materials anywhere you want in the computational cell, e.g. to simulate metallic cavities of an arbitrary shape.

To simulate open boundary conditions, one would like the boundaries to absorb all waves incident on them, with no reflections. This is implemented with something called perfectly matched layers (PML). PML is, strictly speaking, not a boundary condition — rather, it is a special absorbing material placed adjacent to the boundaries. PML is actually a fictitious (non-physical) material, designed to have zero reflections at its interface. Although PML is reflectionless in the theoretical continuous system, in the actual discretized system it has some small reflections which make it imperfect. For this reason, one always gives the PML some finite thickness in which the absorption gradually turns on. For more information, see Perfectly Matched Layer.

Another way in which the computational cell is reduced in size is by symmetry. For example, if you know that your system has a mirror symmetry plane (both in the structure and in the current sources), then you can save a factor of two by only simulating half of the structure and obtaining the other half by mirror reflection. Meep can exploit several kinds of mirror and rotational symmetries — it is designed so that the symmetry is purely an optimization, and other than specifying the symmetry your computation is set up in exactly the same way. See Exploiting Symmetry.

FDTD methods divide space and time into a finite rectangular grid. As described in the next section, Meep tries to hide this discreteness from the user as much as possible, but there are a few consequences of discretization that it is good to be familiar with.

Perhaps the most important thing you need to know is this: if the grid has some spatial resolution Δx, then our discrete time-step Δt is given by Δt=SΔx, where S is the Courant factor and must satisfy S<nmin/#dimensions−−−−−−−−−−√, where nmin is the minimum refractive index (usually 1), in order for the method to be stable (not diverge). In Meep, S=0.5 by default (which is sufficient for 1 to 3 dimensions), but can be changed by the user. This means that when you double the grid resolution, the number of time steps doubles as well (for the same simulation period). Thus, in three dimensions, if you double the resolution, then the amount of memory increases by 8 and the amount of computational time increases by (at least) 2.

The second most important thing you should know is that, in order to discretize the equations with second-order accuracy, FDTD methods store different field components at different grid locations. This discretization is known as a Yee lattice. As a consequence, Meep must interpolate the field components to a common point whenever you want to combine, compare, or output the field components (e.g. in computing energy density or flux). Most of the time, you don't need to worry too much about this interpolation since it is automatic. However, because it is a simple linear interpolation, while E and D may be discontinuous across dielectric boundaries, it means that the interpolated E and D fields may be less accurate than you might expect right around dielectric interfaces.

Many references are available on FDTD methods for computational electromagnetics. See, for example:

A. Taflove and S.C. Hagness, Computational Electrodynamics: The Finite-Difference Time-Domain Method, Artech: Norwood, MA, 2005.

A. Taflove, A. Oskooi, and S.G. Johnson, Advances in FDTD Computational Electrodynamics: Photonics and Nanotechnology, Artech: Norwood, MA, 2013.

The Illusion of Continuity
Although FDTD inherently uses discretized space and time, as much as possible Meep attempts to maintain the illusion that you are using a continuous system. At the beginning of the simulation, you specify the spatial resolution, but from that point onwards you generally work in continuous coordinates in your chosen units. See Units in Meep, above.

For example, you specify the dielectric function as a function ε(x) of continuous x, or as a set of solid geometric objects such as a Sphere, Cylinder, etcetera, and Meep is responsible for figuring out how they are to be represented on a discrete grid. Or if you want to specify a point Source, you simply specify the point x where you want the source to reside — Meep will figure out the closest grid points to x and add currents to those points, weighted according to their distance from x. If you change x continuously, the current in Meep will also change continuously by changing the weights. If you ask for the Poynting flux through a certain rectangle, then Meep will linearly interpolate the field values from the grid onto that rectangle. Array slices of the fields and materials are continuously interpolated as the slice position is moved.

In general, the philosophy of the Meep interface is pervasive interpolation, so that if you change any input continuously then the response of the Meep simulation will change continuously as well, so that it will converge as rapidly and as smoothly as possible to the continuous solution as you increase the spatial resolution.

For example, the ε function used internally by Meep is not simply a discretely sampled version of the ε(x) specified by the user. Rather, each grid point is a kind of average of the ε in the surrounding pixel. Meep's subpixel smoothing is specially designed in order to minimize the "staircasing" and other errors caused by sharp interfaces.

Other Numerical Methods in Computational Electromagnetics
FDTD is, of course, not the only numerical method in computational electromagnetics, nor is it always the most suitable one. In general, it is worthwhile having several tools in your toolbox, and selecting the most convenient one for each task. See Appendix D of Photonic Crystals: Molding the Flow of Light (second edition).

For example, although FDTD can be used to compute electromagnetic eigenmodes (below), in lossless structures it is often quicker, easier, and more reliable to use a specialized eigenmode solver such as MPB. See also the frequency vs. time domain discussion in the MPB manual and the resonant modes discussion below.

For computing the field pattern or response of a structure at a single frequency, it may be more efficient to directly solve the corresponding linear equation rather than iterating in time. Indeed, this can be done directly in Meep (i.e. a finite-difference frequency-domain solver) — see Tutorial/Frequency-Domain Solver. However, especially in cases where there are large differences in scale (e.g. with metals with a shallow skin depth), it may be better to use a method that allows a variable resolution in different spatial regions, such as a finite-element or boundary-element method. Boundary-element methods are especially powerful when you have a large volume-to-surface ratio, such as for scattering calculations over small objects in a large (i.e., infinite-sized) volume.

A strength of time-domain methods is their ability to obtain the entire frequency spectrum of responses (or eigenfrequencies) in a single simulation, by Fourier-transforming the response to a short pulse or using more sophisticated signal-processing methods such as Harminv. Finite-element methods can also be used for time-evolving fields, but they suffer a serious disadvantage compared to finite-difference methods: finite-element methods, for stability, must typically use some form of implicit time-stepping, where they must invert a matrix (solve a linear system) at every time step.

Finally, in systems that are composed of a small number of easily-analyzed pieces, such as a sequence of constant-cross-section waveguides, a collection of cylinders, or a multi-layer film, transfer-matrix/scattering-matrix methods may be especially attractive. These methods treat the individual simple elements in some analytic or semi-analytic fashion, enabling the entire structure to be simulated with great speed and accuracy. There are too many such techniques to easily summarize here.

Transmittance/Reflectance Spectra
Perhaps the most common task to which FDTD is applied is that of computing the transmittance or scattering spectra from some finite structure, such as a resonant cavity, in response to some stimulus. One could, of course, compute the fields (and thus the transmitted flux) at each frequency ω separately, as described above. However, it is much more efficient to compute a broadband response via a single computation by Fourier-transforming the response to a short pulse.

For example, suppose we want the transmitted power through some structure. For fields at a given frequency ω, this is the integral of the Poynting vector (in the normal n^ direction) over a plane on the far side of the structure:

P(ω)=Ren^⋅∫Eω(x)∗×Hω(x)d2x
Now, if we input a short pulse, it is tempting to compute the integral P(t) of the Poynting vector at each time, and then Fourier-transform this to find P(ω). That is incorrect, however, because what we want is the flux of the Fourier-transformed fields E and H, which is not the same as the transform of the time-domain flux. The flux is not a linear function of the fields.

Instead, what one does is to accumulate the Fourier transforms Eω(x) and Hω(x) for every point in the flux plane via summation over the discrete time steps n:

f~(ω)=12π−−√∑neiωnΔtf(nΔt)Δt≈12π−−√∫eiωtf(t)dt
and then, at the end of the time-stepping, computing P(ω) by the fluxes of these Fourier-transformed fields. Meep takes care of all of this for you automatically, of course — you simply specify the regions over which you want to integrate the flux, and the frequencies that you want to compute.

There are other possible methods of time-series analysis, of course. One method that is sometimes very effective is to construct a Padé approximant of the time series of field values at some point, from which one can often extrapolate a very accurate discrete-time Fourier transform (see IEEE Microwave and Wireless Components Letters, Vol. 11, pp. 223-5, 2001), including sharp peaks and other resonant features, from a relatively short time series. Meep does not provide a Padé computation for you, but of course you can output the fields at a point over time, ideally in a single-mode waveguide for transmittance spectra via a single point, and compute the Padé approximant yourself by standard methods.

The power P(ω) by itself is not very useful — one needs to normalize, dividing by the incident power at each frequency, to get the transmittance spectrum. Typically, this is done by running the simulation twice: once with only the incident wave and no scattering structure, and once with the scattering structure, where the first calculation is used for normalization.

It gets more complicated if one wants to compute the reflectance spectrum as well as the transmittance. You can't simply compute the flux in the backwards direction, because this would give you the sum of the reflected and the incident power. You also can't simply subtract the incident power from backwards flux to get the transmitted power, because in general there will be interference effects (between incident and reflected waves) that are not subtracted. Rather, you have to subtract the Fourier-transformed incident fields E(0)ω(x) and H(0)ω(x) to get the reflected/scattered power:

Pr(ω)=Ren^⋅∫[Eω(x)−E(0)ω(x)]∗×[Hω(x)−H(0)ω(x)]d2x
Again, you can do this easily in practice by running the simulation twice, once without and once with the scatterer, and telling Meep to subtract the Fourier transforms in the reflected plane before computing the flux. And again, after computing the reflected power you will normalize by the incident power to get the reflectance spectrum.

(Note that you should not subtract the incident fields when computing the transmitted fields, because on the "output side" of a scattering problem there are only outgoing fields, whereas on the "input side" there are both incoming (incident) and outgoing (reflected) fields and you must separate the two before computing the Poynting flux.)

Meep is designed to make these kinds of calculations easy, as long as you have some idea of what is going on. For examples, see Tutorial/Basics/Transmittance Spectrum of a Waveguide Bend.

Resonant Modes
Another common task in FDTD is to compute resonant modes or eigenmodes of a given structure. For example, suppose you have a diffraction grating, photonic crystal (periodic dielectric structure), or a waveguide and you want to know its harmonic (definite-ω) modes at a given wavevector k. Or, suppose you have a resonant cavity that traps light in a small region for a long time, and you want to know the resonant frequency ω and the decay lifetime (quality factor) Q. And, of course, you may want the field patterns of these modes along with how a given mode is decomposed into a linear superposition of its basis modes.

In order to extract the frequencies and lifetimes (which may be infinite in a lossless system) with FDTD, the basic strategy is simple. You set up the structure with Bloch-periodic and/or absorbing boundaries, depending on whether it is a periodic or open system. Then you excite the mode(s) with a short pulse (broad bandwidth) from a current placed directly inside the cavity/waveguide/whatever. Finally, once the current source is turned off, you have some fields bouncing around inside the system, and you analyze them to extract the frequencies and decay rates.

The simplest form of harmonic analysis would be to compute the Fourier transform of the fields at some point — harmonic modes will yield sharp peaks in the spectrum. This method has serious drawbacks, however, in that high frequency resolution requires a very long running time, and moreover the problem of extracting the decay rates leads to a poorly-conditioned nonlinear fitting problem. Instead, Meep allows you to perform a more sophisticated signal processing algorithm borrowed from NMR spectroscopy — the algorithm is called filter diagonalization and is implemented by Harminv package. Harminv extracts all of the frequencies and their decay rates (and amplitudes) within a short time to high accuracy; for example, we have used it to find lifetimes Q of 109 periods in a computational run of only a few hundred periods.

Once you know the frequencies of the modes, if you want the field patterns you will need to run the simulation again with a narrow-bandwidth (long-time) pulse to excite only the mode in question. Unless you want the longest-lifetime mode, in which case you can just run long enough for the other modes to decay away. Given the field patterns, you can then perform other analyses (e.g. decomposing the Q into decay rates into different directions via flux computations, finding modal volumes, etcetera). For an example, see Tutorial/Resonant Modes and Transmission in a Waveguide Cavity.

Why should you use Meep instead of MPB to compute the modes? Unlike MPB, Meep supports metallic and absorbing materials, can compute lossy resonant modes, can quickly compute large numbers of ω's at once by a single short pulse, and can efficiently extract modes in the interior of the spectrum (e.g. in a band gap). Why should you ever use MPB, then? MPB is quicker at computing the lowest-ω modes than Meep, gives you both the ω and the fields at once, and has no problem resolving closely-spaced frequencies. Moreover, computing modes in time domain is somewhat subtle and requires care — for example, one will occasionally miss a mode if the source happens to be nearly orthogonal to it or if it is too close to another mode; conversely, the signal processing will sometimes accidentally identify spurious peak frequencies. Also, studying periodic systems with non-rectangular unit cells is more subtle in Meep than in MPB. MPB is much more straightforward and reliable, albeit more limited in some ways.

Meepは、計算電磁気学のためのFDTD（Finite-Difference Time-Domain）法を実装しています。FDTD法とは、空間を離散的なグリッドに分割し、離散的な時間ステップで時間的に磁場を展開する手法で、グリッドと時間ステップを細かくすることで、真の連続方程式に近い近似式となり、多くの実用的な問題をほぼ正確にシミュレートすることができます。

ここでは、Meepが採用している方程式と電磁ユニット、FDTD法、およびMeepのFDTDへの取り組みについて紹介します。また、FDTDは計算電磁気学におけるいくつかの有用な手法のうちの1つに過ぎず、それぞれが特別な用途を持っています。

このイントロダクションでは、シミュレーションをセットアップするためのPythonインターフェイスについては説明しません。その代わりに、物理学と数値計算法に焦点を当てています。基本的な機能を示すチュートリアル例については、Tutorial/BasicsおよびSimpetusプロジェクトページを参照してください。

空間の限られた領域しかシミュレーションできないため、シミュレーションは常に何らかの境界条件で終了させる必要があります。Meepでは、3種類の基本的な境界条件がサポートされています。Meepでは、ブロッホ周期的境界、金属壁、PML吸収層の3つの基本的な終端条件がサポートされています。また、問題の対称性を利用することで、計算量をさらに減らすことができます。

サイズLのセル内の通常の周期的境界では、フィールド成分はf(x+L)=f(x)を満たします。ブロッホ周期性は、f(x+L)=eikxLf(x)をあるブロッホ波数kで表す一般化したものです。これは、MPBのように、導波路やグレーティングなどのモードを解くのに使用できます。Photonic Crystalsの第3章をご覧ください。Photonic Crystals: Molding the Flow of Light」（第2版）の第3章を参照してください。

さらに単純な境界条件として、金属の壁があります。この場合、セルが完全な金属に囲まれているかのように、境界上ではフィールドがゼロになるように強制されます（吸収ゼロ、皮膚深さゼロ）。より一般的には、計算セル内の好きな場所に完全金属材料を配置することができ、例えば、任意の形状の金属キャビティをシミュレートすることができます。

開放境界条件をシミュレートするためには、境界に入射するすべての波を吸収し、反射しないようにする必要があります。これを実現するのが、完全整合層（PML）です。PMLは厳密に言うと境界条件ではなく、境界に隣接して配置された特殊な吸収材です。PMLは実際には架空の（非物理的な）材料で、その界面での反射がゼロになるように設計されています。理論的な連続系ではPMLは無反射ですが、実際の離散系では小さな反射があり、不完全なものとなります。このため、PMLには必ず有限の厚さを与え、その中で徐々に吸収を開始するようにしています。詳しくは、Perfectly Matched Layerをご覧ください。

計算セルのサイズを小さくするもう一つの方法は、対称性です。たとえば、システムに鏡面対称の面があることがわかっている場合、構造の半分だけをシミュレーションして、残りの半分を鏡面反射で得ることで、2分の1に減らすことができます。Meepでは、いくつかの種類の鏡面対称性や回転対称性を利用することができます。対称性は純粋に最適化されたものであり、対称性を指定する以外は、まったく同じ方法で計算が行われます。対称性を利用する」を参照してください。

FDTD法は、空間と時間を有限の長方形のグリッドに分割します。次のセクションで説明するように、Meepはこの離散性をできるだけユーザーに見せないようにしていますが、離散化の結果として、知っておくとよいことがいくつかあります。

グリッドがある程度の空間分解能Δxを持つ場合、離散的な時間ステップΔtはΔt=SΔxで与えられます。ここでSはクーラント係数であり、メソッドを安定させる(発散させない)ためには、S<nmin/#dimensions----------√を満たす必要があります。Meepでは、デフォルトではS=0.5（1～3次元ではこれで十分）ですが、ユーザーが変更することもできます。これは、グリッドの解像度を2倍にすると、時間ステップ数も2倍になることを意味します（同じシミュレーション期間の場合）。つまり、3次元の場合、解像度を2倍にすると、メモリ量は8倍になり、計算時間は（少なくとも）2倍になるということです。

次に重要なことは、FDTD法では方程式を2次精度で離散化するために、異なるグリッド位置に異なるフィールド成分を格納するということです。この離散化はYee格子として知られています。その結果、フィールド成分を組み合わせたり、比較したり、出力したりする場合（エネルギー密度や磁束の計算など）、Meepはフィールド成分を共通の点に補間しなければなりません。ほとんどの場合、この補間は自動的に行われるため、あまり気にする必要はありません。しかし、これは単純な線形補間であるため、EとDは誘電体の境界では不連続である可能性があり、補間されたEとDのフィールドは、誘電体の境界付近では期待したよりも正確ではない可能性があることを意味しています。

計算電磁気学のFDTD法については、多くの文献があります。例えば、以下のようなものがあります。

A. A. Taflove and S.C. Hagness, Computational Electrodynamics: A. Taflove and S.C. Hagness, Computational Electrodynamics: The Finite-Difference Time-Domain Method, Artech: Norwood, MA, 2005.

A. Taflove, A. Oskooi, and S.G. Johnson, Advances in FDTD Computational Electrodynamics: Photonics and Nanotechnology, Artech: Norwood, MA, 2013.

連続性の錯覚
FDTDは本質的に離散化された空間と時間を使用しますが、Meepは可能な限り連続したシステムを使用しているかのような錯覚を与えます。シミュレーションの開始時には空間分解能を指定しますが、それ以降は通常、選択した単位の連続座標系で作業を行います。前述の「Meepの単位」を参照してください。

例えば、誘電関数を連続したxの関数ε(x)として指定したり、球や円柱などの固体の幾何学的なオブジェクトの集合として指定したりすると、Meepはそれらを離散的なグリッド上でどのように表現するかを考えてくれます。Meepはxに最も近い格子点を探し出し、xからの距離に応じて重みをつけてそれらの点に電流を加えます。xを連続的に変化させれば、Meepの電流も重みの変化によって連続的に変化します。ある矩形を通過するポインティングフラックスを求めれば、Meepはグリッドからのフィールド値をその矩形に線形補間します。磁場と物質の配列スライスは、スライスの位置を移動させることで連続的に補間されます。

一般的に、Meepインターフェースの哲学は広義の補間であり、入力を連続的に変化させれば、Meepシミュレーションの応答も連続的に変化し、空間解像度を上げても連続解にできるだけ迅速かつスムーズに収束します。

例えば、Meepが内部で使用しているε関数は、ユーザーが指定したε(x)を単に離散的にサンプリングしたものではありません。むしろ、各格子点は、周囲のピクセルのεの平均値のようなものです。Meepのサブピクセル・スムージングは、シャープなインターフェイスに起因する「階段状」やその他のエラーを最小限に抑えるために特別に設計されています。

計算電磁気学におけるその他の数値計算法
FDTDは、計算電磁気学における唯一の数値手法ではありませんし、常に最適な手法というわけでもありません。一般的には、ツールボックスにいくつかのツールを用意しておき、それぞれのタスクに応じて最も便利なものを選択するのが良いでしょう。フォトニック・クリスタル」の付録Dを参照。Photonic Crystals: Molding the Flow of Light」（第2版）の付録Dを参照してください。

例えば、FDTDは電磁界の固有モードの計算に使用できますが（下記）、ロスレス構造ではMPBのような固有モードに特化したソルバーを使用した方が早く、簡単で、信頼性が高い場合が多いです。MPBのマニュアルにある周波数対時間領域の説明や、下記の共振モードの説明も参照してください。

単一の周波数における構造物のフィールドパターンや応答を計算する場合、時間的に反復するのではなく、対応する線形方程式を直接解いた方が効率的な場合があります。実際、これはMeep（有限差分周波数領域ソルバー）で直接行うことができます（チュートリアル/周波数領域ソルバーを参照）。しかし、特にスケールの違いが大きい場合（例：表皮の深さが浅い金属）には、有限要素法や境界要素法など、異なる空間領域で解像度を変化させることができる手法を使用した方がよい場合があります。境界要素法は、体積と表面の比率が大きい場合に特に威力を発揮します。例えば、大きな（つまり無限の大きさの）体積の中にある小さな物体の散乱計算などに適しています。

時間領域法の強みは、短いパルスに対する応答をフーリエ変換したり、Harminvなどの高度な信号処理法を使用することで、1回のシミュレーションで応答の全周波数スペクトル（または固有周波数）を得ることができることです。有限要素法は時間発展するフィールドにも使用できますが、有限差分法に比べて重大な欠点があります。有限要素法は安定性を確保するために、通常、暗黙的な時間ステップを使用しなければならず、時間ステップごとに行列を反転させる（連立方程式を解く）必要があります。

最後に，定断面導波管の列，円柱の集まり，多層膜など，解析が容易な少数の要素で構成される系では，伝達行列/散乱行列法が特に魅力的に映ります．これらの手法は、個々の単純な要素を解析的または半解析的に扱うため、構造全体を非常に高速かつ正確にシミュレーションすることができます。このような手法はあまりにも多く、ここでは簡単にまとめられません。

透過率・反射率スペクトル
FDTDを応用した最も一般的な課題は、共振空洞などの有限構造物が何らかの刺激に反応したときの、透過または散乱スペクトルを計算することでしょう。もちろん、上述したように、各周波数ωにおける場（したがって透過光束）を個別に計算することもできます。しかし，短いパルスに対する応答をフーリエ変換することで，1回の計算で広帯域の応答を計算する方がはるかに効率的です。

例えば，ある構造物の透過電力を求めるとします。与えられた周波数ωの場では、これは構造物の反対側の平面上の（法線n^方向の）ポインティングベクトルの積分です。

P(ω)=Ren^・∫Eω(x)∗×Hω(x)d2x
さて、短いパルスを入力すると、各時刻のポインティングベクトルの積分P(t)を計算し、これをフーリエ変換してP(ω)を求めたくなります。なぜなら、私たちが求めているのは、フーリエ変換されたフィールドEとHのフラックスであり、時間領域のフラックスの変換とは異なるからです。フラックスはフィールドの線形関数ではありません。

その代わり、フラックス平面上のすべての点のフーリエ変換Eω(x)とHω(x)を、離散的な時間ステップnに対する総和を介して蓄積することになります。

f~(ω)=12π--√ΣneiωnΔtf(nΔt)Δt≈12π--√∫eiωtf(t)dt
そして、時間ステップの最後に、これらのフーリエ変換されたフィールドのフラックスによってP(ω)を計算します。もちろん、Meepはこれらすべてを自動的に処理してくれます。フラックスを積分したい領域と、計算したい周波数を指定するだけです。

もちろん、時系列解析の方法は他にもあります。比較的短い時系列から、鋭いピークやその他の共振特徴を含む、非常に正確な離散時間フーリエ変換（IEEE Microwave and Wireless Components Letters, Vol.11, pp.223-5, 2001参照）を推定することができ、非常に有効な方法です。Meepはパデ計算をしてくれるわけではありませんが、もちろん、経時的にある点でのフィールドを出力し、理想的にはシングルモード導波管で1点を経由した透過スペクトルを得て、標準的な方法で自分でパデ近似を計算することができます。

透過率スペクトルを得るためには、各周波数の入射パワーで割って正規化する必要があります。通常、この作業はシミュレーションを2回行います。1回目は入射波のみで散乱構造がない場合、2回目は散乱構造がある場合で、最初の計算は正規化に使用されます。

透過率だけでなく、反射率スペクトルも計算したい場合は、さらに複雑になります。単純に逆方向の光束を計算することはできません。なぜなら、これでは反射光と入射光の合計になってしまうからです。また、単純に逆方向の光束から入射光を引いて透過光を求めることもできません。なぜなら、一般的に（入射波と反射波の）干渉効果があるため、引かれないからです。むしろ、フーリエ変換された入射場E(0)ω(x)とH(0)ω(x)を減算しないと、反射／散乱電力は得られません。

Pr(ω)=Ren^・∫[Eω(x)-E(0)ω(x)]∗×[Hω(x)-H(0)ω(x)]d2x
繰り返しになりますが、実際には、シミュレーションを散乱体なしと散乱体ありの2回行い、Meepに反射面のフーリエ変換を差し引いてからフラックスを計算するように指示することで、簡単に行うことができます。また、反射電力を計算した後、入射電力で正規化して反射率スペクトルを求めます。

なぜなら、散乱問題の「出力側」には出て行く場しかないのに対し、「入力側」には入ってくる場（入射）と出て行く場（反射）の両方があり、ポインティング・フラックスを計算する前にこの2つを分けなければならないからです）。

Meepは、何が起こっているのかをある程度理解していれば、このような計算が簡単にできるように設計されています。例としては、チュートリアル/基本/導波管曲がりのトランスミタンススペクトルを参照してください。

Resonant Modes
FDTDのもう一つの一般的なタスクは、与えられた構造体の共振モードや固有モードを計算することです。例えば、回折格子、フォトニック結晶（周期的な誘電体構造）、導波路などがあり、ある波動ベクトルkにおける高調波（definite-ω）モードを知りたいとします。もちろん、これらのモードのフィールドパターンや、あるモードがその基底モードの線形重畳にどのように分解されるかを知りたい場合もあります。

FDTDで周波数と寿命（ロスレスシステムでは無限大）を抽出するには、基本的な方法があります。まず、構造体が周期系か開放系かに応じて、ブロッホ周期境界や吸収境界を設定します。次に、空洞や導波管などの内部に直接電流を流し、短いパルス（広帯域）でモードを励起します。最後に、電流源をオフにすると、システム内で跳ね回っているいくつかのフィールドがあるので、それを分析して周波数と減衰率を抽出します。

高調波解析の最も単純な方法は、ある時点でのフィールドのフーリエ変換を計算することです。高調波モードは、スペクトルに鋭いピークをもたらします。しかし、この方法には大きな欠点があります。高い周波数分解能を得るためには非常に長い実行時間が必要であり、さらに減衰率を抽出する問題は、条件の悪い非線形フィッティング問題につながります。Meepでは、NMRスペクトロスコピーから受け継いだ、より洗練された信号処理アルゴリズムを実行することができます。このアルゴリズムはフィルタ対角化と呼ばれ、Harminvパッケージで実装されています。Harminvは、すべての周波数とその減衰率（および振幅）を短時間で高精度に抽出します。例えば、わずか数百周期の計算で、109周期の寿命Qを求めることができました。

モードの周波数がわかったら、フィールドパターンを知りたければ、問題のモードだけを励起する狭帯域（長時間）のパルスを用いてシミュレーションを再度実行する必要があります。最も寿命の長いモードが欲しい場合は別ですが、その場合は他のモードが減衰するのに十分な時間をかけて実行すればよいのです。フィールドパターンが得られれば、他の解析を行うことができます（例えば、フラックス計算によってQを異なる方向への減衰率に分解したり、モーダルボリュームを求めたりするなど）。例として、チュートリアル/Resonant Modes and Transmission in a Waveguide Cavityを参照してください。

なぜMPBではなくMeepを使ってモードを計算する必要があるのですか？MeepはMPBと異なり、金属や吸収体に対応していること、損失を伴う共振モードを計算できること、1回の短いパルスで一度に大量のωを高速に計算できること、スペクトルの内部（例えばバンドギャップ内）のモードを効率的に抽出できることなどが挙げられます。では、なぜMPBを使う必要があるのでしょうか？MPBはMeepよりも低域ωモードの計算が早く、ωとフィールドの両方を一度に得ることができ、間隔の狭い周波数の解決にも問題がありません。さらに、時間領域でのモードの計算はやや微妙で、注意が必要です。例えば、音源がたまたまそのモードとほぼ直交していたり、他のモードに近すぎたりすると、そのモードを見逃してしまうことがありますし、逆に、信号処理で誤ってスプリアスなピーク周波数を特定してしまうこともあります。また、非長方形のユニットセルを持つ周期系の研究は、MPBよりもMeepの方がより繊細です。MPBは、いくつかの点で制限されているものの、より分かりやすく、信頼性の高いものです。

## 2. MPB

<http://ab-initio.mit.edu/book/photonic-crystals-book.pdf>

MPB is a software package to compute definite-frequency eigenstates of Maxwell's equations in periodic dielectric structures. It can compute optical dispersion relations and eigenstates for structures such as strip waveguides and optical fibers. MPB is well suited for the study of photonic crystals: periodic dielectric structures exhibiting a band gap in their optical modes, prohibiting propagation of light in that frequency range.

This manual assumes that the reader is familiar with concepts from solid-state physics such as eigenstates, band structures, and Bloch's theorem. We also do not attempt to instruct the reader on photonic crystals or other optical applications for which this code might be useful. For an excellent introduction to all of these topics in the context of photonic crystals, see the book Photonic Crystals: Molding the Flow of Light, by J. D. Joannopoulos, S. G. Johnson, R. D. Meade, and J. N. Winn (Princeton, 2008).

Some of the main design goals we were thinking about when we developed this package were the following. See also the feature list on the main page.

Fully vectorial, 3d calculations for arbitrary Bloch wavevectors. The only approximation is the spatial discretization, or equivalently the planewave cutoff.
Flexible interface. Readable, extensible, scriptable. See also the libctl design goals.
Parallel. Can run on a single-processor machine, but also supports parallel machines with MPI.
Targeted eigensolver: find modes nearest to a specified frequency, not just the lowest-frequency bands. Used for defect calculations.
Leverage existing software (LAPACK, BLAS, FFTW, HDF, MPI, Guile, Python).
Modularity. The eigensolver, Maxwell's equations, user interface, and so on, should be oblivious to each other as much as possible. This way, they can be debugged separately, combined in various ways, replaced, used in other programs; all the usual benefits of modular design.
Take advantage of inversion symmetry in the dielectric function, but don't require it. This means that we have to handle both real and complex fields.

Frequency-Domain vs. Time-Domain
There are two common computational electromagnetic approaches to studying dielectric structures: frequency-domain and time-domain. We feel that each has its own place in a researcher's toolbox, and each has unique advantages and disadvantages. For a more detailed discussion, see our online textbook, appendix D. MPB is frequency-domain. That is, it does a direct computation of the eigenstates and eigenvalues of Maxwell's equations using a planewave basis. Each field computed has a definite frequency. In contrast, time-domain techniques as in our Meep software iterate Maxwell's equations in time; the computed fields have a definite time at each time step but not a definite frequency per se. It seems worthwhile to say a few words about each method, and to explain why we want a frequency-domain code.

Time-domain methods are well-suited to computing things that involve evolution of the fields, such as transmission and resonance decay-time calculations. They can also be used to calculate band structures and for finding resonant modes, by looking for peaks in the Fourier transform of the system response to some input. The main advantage of this is that you get all the spectral peaks at once from a single calculation. There are several disadvantages to this technique, however. First, it is hard to be confident that you have found all of the states—you may have coupled weakly to some state by accident, or two states may be close in frequency and appear as a single peak. This is especially problematic in higher-order resonant-cavity and waveguide calculations. Second, in the Fourier transform, the frequency resolution is inversely related to the simulation time. To get 10 times the resolution you must run your simulation 10 times as long although matters are improved by using more sophisticated signal-processing methods such as Harminv. Third, the time-step size must be proportional to the spatial-grid size for numerical stability. Thus, if you double the spatial resolution, you must double the number of time steps (the length of your simulation), even if you are looking at states with the same frequency as before. Fourth, you only get the frequencies of the states. To get the eigenstates themselves so that you can see what the modes look like and do calculations with them, you must run the simulation again, once for each state that you want, and for a time inversely proportional to the frequency-spacing between adjacent states (i.e. a long time for closely-spaced states).

In contrast, frequency-domain methods like those in MPB are in many ways better-suited to calculating band structures and eigenstates. Here, we consider the case of an iterative eigensolver like the one in MPB, which iteratively improves approximate eigenstates. Dense solvers, which factorize the matrix directly, are impractical for large problems because of the huge size of the matrix, and because they compute many more eigenvectors than are desired. In iterative methods, the operator is only applied to individual vectors and is never itself computed explicitly. First, you don't have to worry about missing states—even closely-spaced modes will appear as two eigenvalues in the result. Second, the error in the frequency in an iterative eigensolver typically decays exponentially with the number of iterations, so the number of iterations is logarithmic in the desired tolerance. Third, the number of iterations typically remains almost constant even as you increase the resolution. The work for each iteration increases, of course, but that happens in time-domain too. Fourth, you get both the frequencies and the eigenstates at the same time, so you can look at the modes immediately, even closely-spaced ones.

A traditional disadvantage of frequency-domain methods was that you had to compute all of the lowest eigenstates, up to the desired one, even if you didn't care about the lower ones. This was especially problematic in defect calculations, in which a large supercell is used, because in that case the lower bands are "folded" many times in the Brillouin zone. Thus, you often had to compute a large number of bands in order to get to the one you wanted incurring large costs both in time and in storage. These disadvantages disappear to some degree in MPB, however, with the advent of its "targeted" eigensolver—with it, you can solve directly for the localized defect states (i.e the states in the band gap) without computing the lower bands. However, the targeted eigensolver method used in MPB still has poor convergence, so time-domain methods such as Meep still have an advantage here.

MPBは、周期的な誘電体構造におけるマクスウェル方程式の確定周波数固有状態を計算するソフトウェアパッケージです。MPBは、ストリップ導波路や光ファイバなどの構造の光分散関係や固有状態を計算することができます。MPBはフォトニック結晶の研究に適しています。フォトニック結晶とは、光学モードにバンドギャップを持つ周期的な誘電体構造で、その周波数領域での光の伝搬を禁止するものです。

本書は、読者が固有状態、バンド構造、ブロッホの定理などの固体物理学の概念に精通していることを前提としています。また、フォトニック結晶や、このコードが役立つ可能性のあるその他の光学的なアプリケーションについては、指導していません。これらの話題をフォトニック結晶の文脈で紹介した優れた入門書としては、「Photonic Crystals: J. D. Joannopoulos, S. G. Johnson, R. D. Meade, J. N. Winn著（Princeton, 2008）をご参照ください。

このパッケージを開発するにあたり、私たちが考えた主な設計目標は以下の通りです。メインページの機能一覧もご参照ください。

任意のブロッホ波動を完全にベクトル化して3次元計算する。唯一の近似は空間離散化、つまり平面波のカットオフです。
柔軟なインターフェース。読みやすく、拡張性があり、スクリプトが可能です。libctlの設計目標も参照してください。
並列。シングルプロセッサのマシンでも動作しますが，MPIによる並列マシンもサポートしています．
ターゲット固有値ソルバー：最低周波数帯だけでなく、指定した周波数に最も近いモードを見つけます。欠陥計算に使用。
既存のソフトウェア（LAPACK, BLAS, FFTW, HDF, MPI, Guile, Python）を活用。
モジュール化。固有値ソルバー、マクスウェル方程式、ユーザーインターフェースなどは、可能な限りお互いに気づかないようにする。こうすることで、別々にデバッグしたり、様々な方法で組み合わせたり、交換したり、他のプログラムで使用したりすることができ、モジュラーデザインのあらゆる利点が得られます。
誘電関数の反転対称性を利用しますが、必須ではありません。つまり、実数場と複素数場の両方を扱う必要があります。

周波数領域と時間領域の比較
誘電体構造の研究には、周波数領域と時間領域の2つの一般的な計算電磁学的アプローチがあります。それぞれに長所と短所があり、研究者のツールボックスの中ではそれぞれが重要な位置を占めています。より詳細な議論については、オンライン教科書の付録Dを参照してください。MPBは周波数領域です。つまり，マクスウェル方程式の固有状態と固有値を平面波ベースで直接計算します．計算された各フィールドは、明確な周波数を持っています。これに対して、Meepのような時間領域法は、マクスウェル方程式を時間的に反復して計算するもので、計算された場は各時間ステップで一定の時間を持ちますが、それ自体は一定の周波数ではありません。ここで、それぞれの手法について少し触れ、なぜ周波数領域のコードが必要なのかを説明しておきましょう。

時間領域法は、透過時間や共鳴減衰時間の計算など、場の進化を伴う計算に適しています。また、バンド構造の計算や、ある入力に対するシステムの応答のフーリエ変換でピークを探して共振モードを見つけるのにも使用できます。この方法の主な利点は、1回の計算ですべてのスペクトルのピークが得られることです。しかし、この手法にはいくつかのデメリットがあります。偶然、ある状態に弱く結合してしまったり、2つの状態の周波数が近く、1つのピークとして現れることがあるからです。これは、高次の共振器や導波路の計算では特に問題となります。次に、フーリエ変換では、周波数分解能はシミュレーション時間に反比例します。10倍の分解能を得るためには、10倍の時間をかけてシミュレーションを行わなければなりません。ただし、Harminvなどのより高度な信号処理手法を用いれば、問題は改善されます。第三に、数値の安定性のためには、時間ステップのサイズは空間グリッドのサイズに比例しなければなりません。したがって、空間分解能を2倍にすると、時間ステップ数（シミュレーションの長さ）を2倍にしなければなりません。ただし、以前と同じ周波数の状態を見ている場合でもです。4つ目は、状態の周波数しか得られないことです。固有状態を取得してモードの様子を見たり、それを使って計算したりするには、シミュレーションを再度実行する必要があります。

これに対して、MPBのような周波数領域の手法は、バンド構造や固有状態の計算に適している点が多くあります。ここでは、MPBのように反復的に近似固有状態を改善する反復固有ソルバーの場合を考えます。行列を直接因数分解する密行列ソルバーは、行列のサイズが巨大になり、また必要以上に多くの固有ベクトルを計算してしまうため、大規模な問題では実用的ではありません。反復法では，演算子は個々のベクトルに適用されるだけで，それ自体が明示的に計算されることはありません．まず、状態の欠落を心配する必要がありません。間隔の狭いモードであっても、結果として2つの固有値として現れます。第二に，反復型固有値ソルバーにおける周波数の誤差は，一般的に反復回数に応じて指数関数的に減衰するため，反復回数は必要な許容範囲の対数になります．第三に、解像度を上げても反復回数は通常ほぼ一定です。もちろん、各反復の作業は増えますが、これはタイムドメインでも同じです。第4に、周波数と固有状態の両方を同時に取得できるので、間隔が狭いモードでもすぐに確認することができます。

周波数領域法の従来の欠点は、目的の固有状態までのすべての低次の固有状態を、たとえ低次の固有状態に関心がなくても計算しなければならないことでした。これは、大きなスーパーセルを用いる欠陥計算では特に問題となりました。なぜなら、その場合、下位のバンドはブリルアンゾーンで何度も「折りたたまれる」からです。そのため、目的のバンドを得るためには、大量のバンドを計算しなければならないことが多く、時間的にもストレージ的にも大きなコストがかかっていました。MPBでは、このような欠点はある程度解消されていますが、「ターゲット」固有値ソルバーの登場により、下位のバンドを計算することなく、局所的な欠陥状態（バンドギャップ内の状態）を直接解くことができるようになりました。ただし、MPBで使用されているターゲット固有値ソルバー法は収束性が悪いため、Meepのような時間領域法が有利になります。
