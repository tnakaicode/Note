# note

- <http://www002.upp.so-net.ne.jp/latex/greece.html>
- <https://www.fujielectric.co.jp/about/company/jihou_2002/pdf/75-08/07.pdf>
- WSL2
  - <https://docs.microsoft.com/ja-jp/windows/wsl/wsl2-install>
  - Windows 10 18917
  - no serial support
  - <http://matsuneko22.hateblo.jp/entry/2017/12/09/144803>

WSL2 command as admin

```Markdown
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

Restart PC

WSL2

```Markdown
wsl -l
wsl --set-version <Distro> 2
```

Docker Pull

```Markdown
docker pull plass/mdtopdf
```

Docker CentOS

```Markdown
docker pull centos
time docker run centos /bin/echo "hello world"
```

## Liquefaction of helium

ヘリウムの液化に用いられる冷却方法
真空中に急激にヘリウムを押し込み、分子が広がるときに分子間力に引かれて押し込まれ気体分子の速度が減少する。
ジュール‐トムソン効果
ヘリウムの臨界点は5.2Kと特に低い。
いったん液体ができると、ポンプで気体を引いて圧力を下げる。圧力が下がると液体から蒸発が起こり、蒸発熱をまわりから吸収して温度を下げる。

Cooling method used for liquefaction of helium
Helium is suddenly pushed into the vacuum, and when the molecules spread, they are pushed by the intermolecular force and the velocity of the gas molecules decreases.
Joule-Thomson effect
Helium has a particularly low critical point of 5.2K.
Once liquid is formed, pump down the gas and reduce the pressure. When the pressure drops, the liquid evaporates, absorbing the heat of evaporation from the surroundings to lower the temperature.
