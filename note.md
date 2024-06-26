---
title: note
---

- [1. Plasma](#1-plasma)
- [2. 大電力直流電圧変換](#2-大電力直流電圧変換)
- [3. 電界数値計算](#3-電界数値計算)
- [4. ヘリウム液化](#4-ヘリウム液化)
- [5. 高圧IGBT直列接続](#5-高圧igbt直列接続)
- [6. テスタを使ったバッテリチェック](#6-テスタを使ったバッテリチェック)
- [7. Markdown to PDF](#7-markdown-to-pdf)
- [8. 2相3相交流](#8-2相3相交流)
- [9. WSL](#9-wsl)
- [10. Design Pattern](#10-design-pattern)
- [11. Memo](#11-memo)

```bash
code --list-extensions
code --list-extensions --show-versions
code --list-extensions --category <category>
code --install-extension <extension-id[@<version>] | path-to-vsix> [--force]
code --uninstall-extension <extension-id>
```

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

Restart PC

WSL2

```bash
wsl -l
wsl --set-version <Distro> 2
```

- WSL
  - \\wsl$\Ubuntu\
  - /mnt/c/

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

- Git
  - ssh key設定
  - ローカルネットワーク上での運用
  - ローカル環境のみで運用
    - <http://blog.atwata.com/tool/2017/10/10/init-local-bare-git-repository.html>
    - git --bare init --shared
  - USB
    - <https://qiita.com/r-ngtm/items/4d92f777c8e3c9fa8083>

```bash
fatal: The remote end hung up unexpectedly
fatal: early EOF
fatal: index-pack failed

git config --global http.postBuffer 1048576000
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

## 1. Plasma

- $m \frac{dv}{dt} = q(E + v\times B)$
- Case1: $v\perp B=i_z$
  - $m \frac{d v_x}{dt} = q v_y B$
  - $m \frac{d v_y}{dt} = -q v_x B$
  - $\frac{d^2 v_x}{dt^2} = -\omega_c^2 v_x$
  - $\frac{d^2 v_y}{dt^2} = -\omega_c^2 v_y$

## 2. 大電力直流電圧変換

設備構成別

|     | Classification                   | Uses                                 |
| --- | -------------------------------- | ------------------------------------ |
| 1   | Cable Link                       | 離島供給・海峡横断・国際連系         |
| 2   | FC - Frequency Converter         |                                      |
| 3   | BTB - Asynchronous Link          |                                      |
| 4   | Long distance / Bulk power trans |                                      |
| 5   | Interconnector                   | 緊急時応援・周波数調整               |
| 6   | RES connectio                    | 洋上風力等再生可能エネルギー送電     |
| 7   | Multi-Terminal: LCC              | 長距離電源送電・中間地点への電力供給 |
| 8   | Multi-Treminal: VSC              | 再エネ電源の連系                     |

変換器種別

|     | 原理   | 変換器種類      | 用途                                   |
| --- | ------ | --------------- | -------------------------------------- |
| 1   | 他励磁 | 水銀整流器      |                                        |
| 2   | 他励磁 | サイリスタ: ETT |                                        |
| 3   | 他励磁 | サイリスタ: LTT | 系統間連系・中規模直流設備             |
| 4   | 自励磁 | 2- / 3-Level    | 弱小系統連系                           |
| 5   | 自励磁 | MMC             | 弱小系統連系・洋上風力・中規模直流設備 |
| 6   | 他励磁 | 電源端: 他励磁  | 大規模電源送電の需要側の相互作用       |
|     | 自励磁 | 受電端: 自励磁  |                                        |

- ETT Electrically Triggered Thyristor
- LTT Light Triggered Thyristor
- MMC Modular Multi-Level Converter

## 3. 電界数値計算

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

- ポテンシャルを最小にする電位分布が静電界
  - 電位$\phi$を一次式で近似
  - 要素内で電界が一定
  - とみなせるほど各要素が十分小さい

$$ \phi = \alpha_1 + \alpha_2 x + \alpha_3 y $$

$$ \begin{aligned}
  \phi_i &= \alpha_1 + \alpha_2 x_i + \alpha_3 y_i \\
  \phi_j &= \alpha_1 + \alpha_2 x_j + \alpha_3 y_j \\
  \phi_m &= \alpha_1 + \alpha_2 x_m + \alpha_3 y_m \\
\end{aligned} $$

$$ \phi = \frac{1}{2\delta} ( (a_i + b_i x + c_i y) \phi_i + (a_j + b_j x + c_j y) \phi_j + (a_m + b_m x + c_m y) \phi_m ) $$

$$\begin{aligned}
  a_i &= x_j y_m - x_m y_i \\
  b_i &= y_j - y_m \\
  c_i &= x_m - x_j \\
\end{aligned}$$

ポテンシャル$X_e$

$$ X_e = \frac{\epsilon}{8 \delta} ((b_i \phi_i + b_j \phi_j + b_m \phi_m)^2 + (c_i \phi_i + c_j \phi_j + c_m \phi_m)^2) $$

- 各要素のポテンシャルは各節点の電位$\phi_i$の二次式になる
  - $\phi_i$を微分することで節点電位にお関する一次式が得られる

- Surface Charge method SCM 表面電荷法
  - 関係する領域内のすべての電荷の大きさと位置が決まれば
  - クーロン式からどの点の電位・電界も与えることができる
  - 境界要素法の一部
  - R. F. Harrington Moment of Method

- Charge Simulation method CSM 電荷重畳法

## 4. ヘリウム液化

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

## 5. 高圧IGBT直列接続

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

## 6. テスタを使ったバッテリチェック

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

## 7. Markdown to PDF

Default template.html

```html
<!DOCTYPE html>
<html>

<head>
  <title>{{{title}}}</title>
  <meta http-equiv="Content-type" content="text/html;charset=UTF-8">
  {{{style}}}
  {{{mermaid}}}
</head>

<body>
  <script>
    mermaid.initialize({
      startOnLoad: true,
      theme: document.body.classList.contains('vscode-dark') || document.body.classList.contains('vscode-high-contrast')
        ? 'dark'
        : 'default'
    });
  </script>
  {{{content}}}
</body>

</html>
```

## 8. 2相3相交流

- 3相交流(RST)を2相交流(RS)に変換する
  - RSTの3本のケーブルのうち、2本だけを繋ぐ(単相き電方式)
  - 3相の電流バランスを崩しやすくなる
  - スコット結線・変形ウッドブリッジ結線・ルーフデルタ結線の変圧器を使う

## 9. WSL

```bash
wsl -l
wsl -t Ubuntu-22.04
wsl --export Ubutnut-22.04 ubuntu-22.04.tar
wsl --unregister Ubuntu-22.04
wsl --import Ubuntu-22.04 Ubuntu-22.04 ubuntu-22.04.tar
wsl -d Ubuntu-22.04 -u root

# etc/wsl.conf
[user]
default=username

# mount
sudo mount -t drvfs '\\nas\share' /mnt/nas/
sudo mount -t drvfs \\\\nas\\share /mnt/nas/
```

## 10. Design Pattern

| Category   | Name                    | Comment                            |
| ---------- | ----------------------- | ---------------------------------- |
| Generation | Abstract Factory        |
|            | Builder                 |
|            | Factory Method          |
|            | Prototype               | Pythonのライブラリ・ビルトイン有り |
|            | Singleton               | Pythonのライブラリ・ビルトイン有り |
| Structure  | Adapter                 |
|            | Bridge                  | Pythonicな書き方有り               |
|            | Composite               |
|            | Decorator               | Pythonビルトイン有り               |
|            | Facade                  |
|            | Flyweight               | Python機能で代用                   |
|            | Proxy                   |
| Behavior   | Chain of Responsibility |
|            | Command                 |
|            | Interpreter             |
|            | Iterator                | Pythonビルトイン有り               |
|            | Mediator                |
|            | Memento                 |
|            | Observer                |
|            | State                   |
|            | Strategy                |
|            | Template Method         |
|            | Visitor                 | Pythonビルトイン有り               |

## 11. Memo

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

- パワースイッチング用半導体デバイス
  - シリコン物性の基礎事項
  - pn接合(junction)とダイオード
    - p型半導体・n型半導体間で電位段差が形成され、キャリアの流れが釣り合ったところでトータルの電流が0になる
    - キャリアが存在しない層を空乏層という
    - わずかではあるが空乏層を拡散あるいはドリフトするキャリアは存在する
    - 印加電圧の極性を逆にすると接触電位差を超えたところで空乏層がなくり外部回路に電流が流れる
    - 陽極をAnode・陰極をCathodeと呼ぶ
  - PINダイオード
    - 順電流容量：数千A、逆耐電圧：数千Vのダイオードでは、順電圧降下が0.7Vでも発熱量が数kWになる
    - 順電流に対しては放熱が問題になる
    - 耐電圧に対しては空乏層の電界強度を弱める必要がある
    - i層半導体をはさんで電界強度を緩和する
  - 少数キャリア蓄積効果
    - S-Off -> S-Onの動作では、順電流が流れていたときに流入したキャリアが逆電流方向に掃き出しを始める
    - 空乏層が形成されるまで端子電圧は順電圧降下のままになる
    - 空乏層が形成される過程で回路中のインダクタンスと空乏層のキャパシタンスでエネルギーの交換が行われる
    - 振動的な電圧変動が起こり、瞬間的に電源電圧を超える電圧が発生する
    - 高速に動作するダイオードは空乏層の形成時間ものとなる
    - しかし、空乏層の形成時間が短い場合、電流の絞り込みが急激に起こるため、より高いPeak電圧を生じる
    - 空乏層の形成速度を緩和するSoft Recovery Diode
  - スナバ回路
    - SWのOn/Off時にインダクタンスにより異常電圧が生じることがある
    - 異常電圧からSWを保護するためスナバ回路(Snuber circuit)を使用する
    - インダクタンスが発生させる電圧を吸収することでSWを保護する
    - 電圧の降下に伴い抵抗値が低下する非線形抵抗を使用することもある
    - 一般的には、コンデンサをSWに並列につなげるスナバ回路を用いる
    - 異常電圧のほとんどはインダクタンスによって生じる
    - GTOサイリスタの電流遮断動作においてはデバイスに特有なスパイク電圧が生じる
    - S-Off時のインダクタンスからのエネルギーをコンデンサで吸収する
    - S-On時にはコンデンサは放電するため、過度な電流がSWに入らないように適切な抵抗を挿入する
- DC-DC変換
- DC-AC変換
- AC-DC変換
- AC-AC変換

![iruka0](./img/2020-02-25-21-47-48.png)
![iruka1](./img/2020-02-25-21-46-56.png)
![iruka2](./img/2020-02-25-21-47-13.png)
![iruka3](./img/2020-02-25-21-47-24.png)

- テフロン
  - 無極性
  - 誘電率・力率共に温度・周波数に関係なく一定できわめて低い
  - 絶縁抵抗や絶縁破壊の強さもプラスチック中最高
  - 高温のなかで、15，000～20，000ボルトの高電圧の下に使用しても高い絶縁抵抗
- <https://www.packing.co.jp/PTFE/ptfe_tokusei1.htm>
- PTFE＝ポリテトラフルオロエチレン(４フッ化)
- PFA＝テトラフルオロエチレン・パーフルオロアルキルビニルエーテル共重合体
- FEP＝テトラフルオロエチレン・ヘキサフルオロプロピレン共重合体(４．６フッ化)
- ETFE＝テトラフルオロエチレン・エチレン共重合体
- PVDF＝ポリビニリデンフルオライド(２フッ化)
- PCTFE＝ポリクロロトリフルオロエチレン(３フッ化)

- P&ID
  - 配管・配線プロセスと他の機器や計測器との相互作用を示すダイアグラム
  - PFD Process Flow Diagram
  - PID Process Instrument Diagram
  - IO: IGE-XAO Electrical Expert
  - Modelica

- C++
  - Handle, Object
  - <https://teratail.com/questions/44526>
    - 何らかのリソースを識別・操作するための識別子
    - <http://www.drdobbs.com/c-made-easier-handles-and-exception-safe/184401551>

- manage on Win10
  - <https://qiita.com/nightyknite/items/b4db8766c0b94764cd3c>
  - <https://qiita.com/tikkss@github/items/4db7bec95a7337ca826d>

  - [enum]::GetNames([Net.SecurityProtocolType])

- RTD Resistance Temperature Detector
  - <https://www.keyence.co.jp/ss/products/recorder/lab/thermometry/resistance_bulb.jsp>
  - PT100/PT1000
    - PT100 (白金 0℃ - 100Ω) JIS-C1604
      - 0.385Ω/1℃
    - PT1000(白金 0℃ - 1000Ω)
  - 2線式/3線式/4線式
    - 2線式 A-B
      - 抵抗素子の両端にそれぞれ1本ずつ導線を接続した結線方式です。
      - 安価ですが、導線抵抗値がそのまま抵抗値として加算されますので、あらかじめ導線抵抗値を調べて補正をする必要があります
      - そのため、実用的ではありません。
    - 3線式 A-BB
      - 最も一般的な結線方式です。抵抗素子の片端に2本、もう片端に1本の導線を接続した結線方式です。
      - 3本の導線の長さ、材質、線経及び電気抵抗が等しい場合、導線抵抗の影響を回避できることが特徴です。
    - 4線式 AA-BB
      - 抵抗素子の両端に2本ずつ導線を接続した結線方式です。
      - 高価ですが、測定原理上、導線抵抗の影響を完全に回避できます。

- TC Thermal Coupler
  - 熱電対
  - 補償導線
    - PVC被覆/ガラス繊維被覆

- 絶縁トランス <https://www.digikey.jp/ja/articles/the-basics-of-isolation-transformers-and-how-to-select-and-use-them>
