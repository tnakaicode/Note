# note

- <http://www002.upp.so-net.ne.jp/latex/greece.html>
- WSL2
  - <https://docs.microsoft.com/ja-jp/windows/wsl/wsl2-install>
  - Windows 10 18917
  - no serial support
  - <http://matsuneko22.hateblo.jp/entry/2017/12/09/144803>

WSL2 command as admin

```bash
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

![iruka0](./img/2020-02-25-21-47-48.png)
![iruka1](./img/2020-02-25-21-46-56.png)
![iruka2](./img/2020-02-25-21-47-13.png)
![iruka3](./img/2020-02-25-21-47-24.png)

Restart PC

WSL2

```bash
wsl -l
wsl --set-version <Distro> 2
```

Docker Pull

```bash
docker pull plass/mdtopdf
```

Docker CentOS

```bash
docker pull centos
time docker run centos /bin/echo "hello world"
```

Git Config

```bash
git config --global user.email "tnakaicode@gmail.com"
git config --global user.name "TNakai"
```

SSH Keygen

```bash
cd ~/.ssh
ssh-keygen -t rsa -f id_rsa_git
clip < id_rsa_git
scp id_rsa_git \\wsl$\Ubuntu-18.04\home\<username>\.ssh
```

Proxy setting on WSL (/etc/apt/apt.conf)

```bash
Acquire::http::proxy "http://id:pass@proxysrv:port/";
Acquire::https::proxy "https://id:pass@proxysrv:port/";
```

Proxy setting for Git, conda and pip

```bash
git config --global http.proxy http://proxy.example.com:8080
git config --global https.proxy http://proxy.example.com:8080

# .condarc
proxy_servers:
    http: http://USER:PASSWORD@PROXYSERVER:PORT
    https: https://USER:PASSWORD@PROXYSERVER:PORT

pip install <name> --proxy http://proxy.example.com:8080
```

```PowerShell
# install_Ubuntu.ps1
# You need to Execute this command and reboot in advance.
# Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

# Password Setting
$secPasswd=ConvertTo-SecureString <ProxyPassword> -AsPlainText -Force
# User and Credential Setting
$myCreds=New-Object System.Management.Automation.PSCredential -ArgumentList <ProxyUsername>,$secPasswd

# Download Image
Invoke-WebRequest -Uri https://aka.ms/wsl-ubuntu-1804 -OutFile $home/Ubuntu.appx -Proxy <ProxyServerName> -proxyCredential $myCreds

# Unzip File
Rename-Item $home\Ubuntu.appx $home\Ubuntu.zip
Expand-Archive $home\Ubuntu.zip $home\Ubuntu

# Create Shortcut in Desktop
cd $home\Ubuntu
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$Home\Desktop\ubuntu1804.lnk")
$Shortcut.TargetPath = "$home\Ubuntu\ubuntu1804.exe"
$Shortcut.Save()
```

```bash
#!/bin/bash

# setting http proxy
cat <<'EOF' >> ~/.bashrc

# http proxy setting
export HTTP_PROXY_USER=id
export HTTP_PROXY_PASS=pass
export HTTP_PROXY=http://${HTTP_PROXY_USER}:${HTTP_PROXY_PASS}@proxysrv:port/
export HTTPS_PROXY=${HTTP_PROXY}

# git proxy setting
git config --global http.proxy ${HTTP_PROXY}
git config --global https.proxy ${HTTPS_PROXY}
git config --global url."https://".insteadOf git://
EOF

# setting apt proxy
echo <suPassword> | sudo tee /etc/apt/apt.conf <<EOF > /dev/null
Acquire::http::proxy "http://id:pass@proxysrv:port/";
Acquire::https::proxy "https://id:pass@proxysrv:port/";
EOF


# setting wget proxy
echo <suPassword> | sudo tee -a /etc/wgetrc <<EOF > /dev/null

# wget proxy setting
https_proxy = http://id:pass@proxysrv:port/
http_proxy = http://id:pass@proxysrv:port/
ftp_proxy = http://id:pass@proxysrv:port/
EOF
```

## Numerical electric field calculation

- Finite Difference method 差分法
  - 領域を格子で分割しラプラスの式を差分の式に置き換えて
  - 格子点の電位を未知数とする方程式を作る
  - 近接点(格子点)の電位の関係式をもとにした方法
  - $\phi_0$は$(x_0,y_0)$の電位
  - $\phi_2$は$(x_2,y_0)$の電位
  - $\phi_4$は$(x_0,y_4)$の電位

$$ \frac{\partial \phi}{\partial x} = \frac{\phi_0 - \phi_2}{\delta x}, \frac{\phi_3 - \phi_0}{\delta x}, \frac{\phi_3 - \phi_2}{2 \delta x} $$

- Finite Element method 有限要素法
  - 領域を小部分の特性(面積・体積・電位)をベースとする
  - 分割した部分が有限要素
  - 分割した小部分の電位を簡単な関数で近似する
  - 電界が座標の一次式であった場合
    - 要素周辺の適当な点の電位の電位と座標の関数として表現される
    - 領域全体の電位を節点の電位で形式的に表現できる
    - 領域全体のポテンシャルも節点の電位により得られえる
    - ポテンシャルが最小になる各点の電位を得る
  - ラプラスの式がポテンシャル最小原理と等しい

$$ \frac{\partial}{\partial x} {\frac{\partial f}{\partial(\frac{\partial \phi}{\partial x})}} + \frac{\partial}{\partial y} {\frac{\partial f}{\partial(\frac{\partial \phi}{\partial y})}} + \frac{\partial}{\partial z} {\frac{\partial f}{\partial(\frac{\partial \phi}{\partial z})}} - \frac{\partial f}{\partial \phi} = 0 $$

$$ X(\phi) = \int\int\int f(x, y, z, \frac{\partial \phi}{\partial x}, \frac{\partial \phi}{\partial y}, \frac{\partial \phi}{\partial z}) dx dy dz$$

- Surface Charge method SCM 表面電荷法
  - 関係する領域内のすべての電荷の大きさと位置が決まれば
  - クーロン式からどの点の電位・電界も与えることができる
  - 境界要素法の一部
  - R. F. Harrington Moment of Method

- Charge Simulation method CSM 電荷重畳法

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

## High-voltage IGBT multi-series technology

- <https://www.fujielectric.co.jp/about/company/jihou_2002/pdf/75-08/07.pdf>

電力系統，産業プラント，電気鉄道などで適用される電力変換装置は高圧・大容量であるため，以前はサイリスタやGTO（Gate Turn-Off）サイリスタなどのデバイスが主流を占めていた。
一方，汎用インバータなどの比較的中小容量の変換装置にはIGBT（Insulated  Gate  BipolarTransistor）が広く適用されており，高性能化が図られている。

Since power converters used in power systems, industrial plants, electric railways, etc. have high voltage and large capacity, devices such as thyristors and GTO (Gate Turn-Off) thyristors used to dominate before.
On the other hand, IGBTs (Insulated Gate Bipolar Transistors) are widely applied to converters with relatively small and medium capacities, such as general-purpose inverters, to achieve higher performance.

デバイスを直列接続したときの最大の問題点は，各デバイスのスイッチングタイミングに差が生じたとき，各デバイスの素子電圧が不平衡となり，特定のデバイスに過大な電圧責務がかかることである。
IGBTの場合，他の電力用デバイスと比較すると，スイッチング速度が速く，素子電圧の不平衡が大きくなる傾向がある。
特にターンオフ時には，電流遮断時に発生する過渡電圧が主回路電圧に重畳するため，素子破壊を招く可能性が強くなる。
素子電圧の不平衡を抑制することが，IGBTを直列接続する際の最大の課題となる

The biggest problem with connecting devices in series is that when there is a difference in the switching timing of each device, the element voltages of each device become unbalanced, and a particular device takes an excessive voltage responsibility.
In the case of IGBTs, the switching speed tends to be faster and the device voltage unbalance tends to be larger than other power devices.
Particularly at the time of turn-off, a transient voltage generated at the time of current interruption is superimposed on the main circuit voltage, so that the possibility of destruction of the element is increased.
Suppressing device voltage imbalance is the biggest challenge when connecting IGBTs in series

直列接続されているIGBTのゲート線を，コア（以下，ゲートバランスコアという）によって磁気的に結合させ，スイッチング時に流れるゲート電流のタイミングをバランスさせるものである。その結果，素子電圧分担を均等化させることができる。

The gate lines of the IGBTs connected in series are magnetically coupled by a core (hereinafter, referred to as a gate balance core) to balance the timing of the gate current flowing during switching. As a result, element voltage sharing can be equalized.

## Check the battery consumption with a tester

電池に負荷抵抗をつないで調べる。
電池が実際に使われている状態を再現して電流が流れている時の、電池の端子電圧を測定する。
電池の内部抵抗は使えば使うほど大きくなる。
内部抵抗にかかる電圧分が低下した端子電圧になる。負荷をつけずに電流が流れると内部抵抗による電圧降下がないため(?)、負荷をつけないで電圧を測っても電池の消耗度は分からない。

Check by connecting the load resistance to the battery.
Measure the terminal voltage of the battery when the current is flowing, reproducing the state in which the battery is actually used.
The more the battery is used, the greater the internal resistance of the battery.
The voltage applied to the internal resistance becomes the reduced terminal voltage. If the current flows without a load, there is no voltage drop due to the internal resistance (?). Therefore, even if the voltage is measured without a load, the consumption of the battery is not known.

- 赤 - 左手 - 正極
- 黒 - 右手 - 負極

## Memo

- 量子暗号
  - <http://www.scat.or.jp/frontier/frontier75/waseda.pdf>
  - 現代暗号技術
    - ハッシュ関数 SHA-1(160[bit])をSHA-2(256[bit])への変更
    - 公開鍵暗号RSAの鍵長を1024[bit]から2048[bit]へ延ばす
    - システム更新時のサービスの継続性(BCP)に影響する
    - 互換性維持に伴う安全性低下
    - one time pad
  - 量子暗号技術
    - 量子鍵配送
      - one time padでの問題点
      - 安全な鍵の共有が可能
    - SECOQC Secure Communication based on Quantum Cryptography
    - 東京QKDネットワーク
  - 量子複数秘密分散法
    - 参加者の集合P
    - 秘密の量子状態の集合$\{S_1, ..., S_n\}$
    - 各々の秘密$Si$に対して
      - 純粋化に用いた補助系$R_i$
      - アクセス構造を$\Gamma_i$
    - 各$\Gamma_i$に対して$T_i=\{R_1, ..., R_n\} \ \{R_i\}$
    - 任意の$i$に対して以下の条件を満たすものを量子複数秘密分散法と定義する
      - Recoverability $\forall A \in \Gamma_i, I(R_i:T_iA) = I(R_i:S_i)$
      - Secrecy $\forall B \notin \Gamma_i, I(R_i:T_iB) = 0$
  - 光ファイバ帯域の量子通信暗号路の通信容量の評価
    - 50THz Modulatin
      - Phase Shift Keying PSK
      - Quadrature Amplitude Modulation QAM
    - 検出
      - Hetero-Dyne
      - Homo-Dyne
    - Holevo Information
      - SRD Square Root Detection
      - 量子測定
      - 以上から得られる最大の情報量
    - 入力電力　1uW以下
      - BPSK
      - Homo-Dyne
    - 入力電力　1uW以上　1mW以下
      - 多値で変調
      - Hetero-Dyne
