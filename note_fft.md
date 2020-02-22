# FFT

## Convolution

## Cross Spectrum

## Hirbert

ノイズを含んだ信号の包絡線  
<https://www.jstage.jst.go.jp/article/safety/41/5/41_302/_pdf/-char/ja>
ノイズのあるデータからの減衰率の測定に関するものである．
このパラメータは，構造物や部材の振動を止め破損を防いだり，制御を行う上で特性を決定するので重要であるが，測定が困難である．
特に，現場試験のようにノイズのある状況下では，精度よく求めることが難しい．この点を克服するために，包絡線の時間変化から減蓑率を求めるヒルベルト変換を用いた手法に着目した。
実験で，従来から用いられている対数減衰率を用いた方法と比較し，ノイズレベルの低い状況で，測定値が一致することを確認し，さらにシミュレ・一ションで，固有振動数，減衰率，ノイズの大きさの影響を調べた。
その結果，従来法に比べ，よい測定値がえられることがわかった，

Damping ratio is a key parameter, which characterizes the vibration behavior of machinery and structures- Small damping ratio allows the sustained oscillation and this leads to fatigue fracture; e_g_ . turbinc brade, main wings in airplane.
For another example, since a bridge. is exposed to wind and excited to oscillation, the damping ratia is also an important factor.
In fact, its damping ratio is measured by field vibration test at its completion. Recently, as a result of trend of lightweighted and dowvn-sizig in machinery, the reduce af its rigidity leads to the easily occurrence of vibration and sustaining.
Therefcre sometimes, the machine ar a part of machinery is due to vibration test for measuring the ratio and for observing the damping behaviar.
However, the logged data in such a test is aiways polluted with a vibrattion from another sources, background vibration, and sensor noise and so an.
Some papers show the methadology to estirnate damping ratio signals

減衰比は重要なパラメータであり、機械と構造の振動挙動を特徴づけます。小さな減衰比は持続的な振動を可能にし、疲労破壊につながります。 e_g_。タービンブレード、飛行機の主翼。
別の例として、橋から。風にさらされ、振動に興奮している場合、減衰率も重要な要素です。
実際、減衰比は、完成時のフィールド振動試験によって測定されます。最近では、機械の軽量化とダウニング効果の傾向の結果として、剛性が低下すると振動が発生しやすくなり、持続しやすくなります。
時々、機械は機械の一部であり、比を測定し、減衰挙動を観察するための振動試験によるものです。
ただし、このようなテストで記録されたデータは、別のソースからの振動、バックグラウンド振動、センサーノイズなどで常に汚染されています。
減衰比信号を推定する方法論を示すいくつかの論文

This method has its bases on Hilbert transform which is usually applied to envelope procedure.
The merit of this method is cansidered to be easily understandable.
Ref3) has shawn its fundarnental methodology and also has shown that the damping ratio can be estimated even under noisy conditions.
But, their paper has not shown the effect of noise to the accuracy because their research interests were on the effect of "window" for truncating signals.
And they examined this approach only by simulation.
After their paper, anyone incluchng Agneni himself, has not reported on this methodology.

このメソッドは、通常はエンベローププロシージャに適用されるヒルベルト変換に基づいています。
この方法のメリットは、簡単に理解できると考えられます。
Ref3）は、基本的な方法論を示し、ノイズの多い条件下でも減衰比を推定できることを示しています。
しかし、彼らの研究の関心は信号を切り捨てるための「窓」の効果にあったため、彼らの論文は精度に対するノイズの影響を示していません。
そして、彼らはシミュレーションによってのみこのアプローチを検討しました。
彼らの論文の後、Agneni自身を含む誰もがこの方法論について報告していません。

$$ m \frac{\partial^2 x(t)}{\partial t^2} + c \frac{\partial x(t)}{\partial t} + k x(t) = 0 $$

damping ratio
$$ \zeta = \frac{c}{c_c} = \frac{1}{2\sqrt{m\cdot k}}$$

angular natural frequency
$$ \omega_0 = \sqrt{\frac{k}{m}} $$

natural frequency
$$ f_0 = \frac{\omega_0}{2 \pi} $$

critical damping coefficient
$$ c_c = 2 \sqrt{m \cdot k} $$

Response from system
$$ \begin{aligned}
    x(t) &= X \exp(-\zeta\omega_0 t)\sin(\sqrt{1-\zeta^2}\omega_0 t + \phi) \\
    &= X \exp(-\zeta\omega_0 t)\sin(\omega + \phi)
\end{aligned}$$
$$ \omega = \sqrt{1 - \zeta^2} \omega_0 $$

Hirbert Transform
$$ \widetilde{x}(t) = \frac{1}{\pi} \int^{\infin}_{-\infin} \frac{x(u)}{t-u} du $$

Analisitic Function
$$ \psi(t) = x(t) + j \widetilde{x}(r) $$

## 2D FFT
