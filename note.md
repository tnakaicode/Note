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
