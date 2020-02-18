# note

- WSL2
  - <https://docs.microsoft.com/ja-jp/windows/wsl/wsl2-install>
  - Windows 10 18917
  - no serial support
  - <http://matsuneko22.hateblo.jp/entry/2017/12/09/144803>

``` WSL2 command as admin
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

Restart PC

``` WSL2
wsl -l
wsl --set-version <Distro> 2
```

``` Docker Pull
docker pull plass/mdtopdf
```

``` Docker CentOS
docker pull centos

time docker run centos /bin/echo "hello world"
```

## Piezoelectric material

圧電効果はある種の物質(水晶など)に圧力を加えると、物質の表面に圧力に比例する電圧(電荷)が現れる現象
結晶格子の分極によるものと考えられている
力の向きを逆にすると電圧の極性は逆になる  
The piezoelectric effect is a phenomenon in which when pressure is applied to a certain substance (such as quartz), a voltage (charge) proportional to the pressure appears on the surface of the substance.
It is thought to be due to the polarization of the crystal lattice
Reversing the direction of the force reverses the polarity of the voltage

電歪 Electro-Striction
強誘電体の多くは圧力を加えると表面に電圧を生じる。また、電圧を加えるとひずみを表示る。この現象では、電圧の極性を逆にしてもひずみの向きは変わらない。
バイアス電圧を与えておけば、そこを中心としたひずみの変化は圧電と同様の扱いができる  
Many ferroelectrics produce a voltage on their surface when pressure is applied. When a voltage is applied, distortion is displayed. In this phenomenon, the direction of the distortion does not change even if the polarity of the voltage is reversed.
If a bias voltage is applied, the change in strain around it can be treated in the same way as piezoelectric

セラミックス磁器のような多結晶からなる物質で高電圧を印加すると、その方向の分極が残留して圧電性を示すことがある。
多結晶の各ドメインは圧電性を持つが、それらがランダムに分布しているため、そのままでは全体としては圧電性を示さない。
高電圧を加えることで、分極方向がそろい圧電材と同様の圧電性を示すようになると考えられている。  
When a high voltage is applied to a polycrystalline material such as ceramic porcelain, polarization in that direction may remain and exhibit piezoelectricity.
Each domain of the polycrystal has piezoelectricity, but since it is randomly distributed, it does not exhibit piezoelectricity as it is as a whole.
It is considered that application of a high voltage causes the piezoelectric material to exhibit the same piezoelectricity as a piezoelectric material having a uniform polarization direction.

1918 Application of Langevin's Sonar to Transceiver  
Transducer for transmitting and receiving underwater ultrasonic waves of several tens of kHz  
ランジュバン形振動素子
Langevin type vibrating element

厚み振動する水晶板の両面に鋼鉄の平板を接着したサンドイッチ構造
水晶部の厚みが薄くなるため水晶は少量で済み、低い電圧で動作する。両面の鋼平板の厚みを変えれば共振周波数を任意に選ぶことができる。  
Sandwich structure in which a steel plate is bonded to both sides of a vibrating quartz plate
Since the thickness of the crystal part is reduced, only a small amount of crystal is required and the device operates at a low voltage. The resonance frequency can be arbitrarily selected by changing the thickness of the steel plates on both sides.

BaTiO3 チタン酸バリウム
PZT チタン酸ジルコン酸鉛

水晶は温度特性が良好のため、時計・発信機・振動子などで使われている。多くはオークトレーブ法による人工のものである。
結晶の圧電材としては、ADP, CdS, ZnO, LiNiO3などが実用的なものとして知られる
PVDF(ポリフッ化ビニリデン)などの高分子系のやわらかい圧電材も圧電セラミックに劣らない圧電効果もつものが現れている。
生体のなかにも骨などが圧電性を示す。

Magneto-Striction 磁歪
