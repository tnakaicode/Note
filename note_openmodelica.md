---
title: OepnModelica Circuite
---

- [1. HVSW](#1-hvsw)

- <https://www.programmersought.com/article/40412970490/>
- <https://www.programmersought.com/article/35352889888/>
- <http://ayumi.cava.jp/audio/pow/node20.html>
- <http://blog.livedoor.jp/qcreate/archives/51955783.html>
- <http://ayumi.cava.jp/audio/ac/node9.html>
- <http://champ.chips.jp/gazou14/tube2.html>

## 1. HVSW

- <https://www.shindengen.co.jp/products/semi/column/basic/mosfet/mosfet.html>
- Diode
  - Electrical.Analog.Semiconductors.Diode
  - The simple diode is an electrical one port, where a heat port is added, which is defined in the Modelica.Thermal library. It consists of the diode itself and a parallel ohmic resistance R. If useTemperatureDependency is set to true, the diode formula is
  - This diode model is an improved version of the simple diode model. It includes a series resistance, parallel conductance, and also models reverse breakdown. The model is divided into three parts:
    - lower half of reversed bias region including breakdown: -Ids·(exp(-(vd+Bv)/(N·Vt)) + 1 - 2·exp(-Bv/(2·N·Vt)))
    - upper half of reverse biased region and forward biased region before conduction: Ids·(exp(vd/(N·Vt)) - 1)
    - forward biased region after conduction: iVdMax + (vd - VdMax)·diVdMax
- Bipolar transistor
  - Electrical.Analog.Semiconductors.NPN
  - Electrical.Analog.Semiconductors.PNP
  - This model is a simple model of a bipolar NPN junction transistor according to Ebers-Moll. A heating port is added for thermal electric simulation. The heating port is defined in the Modelica.Thermal library. A typical parameter set is (the parameter Vt is no longer used):
  - このモデルは，Ebers-MollによるバイポーラNPN接合型トランジスタの簡易モデルです。熱電シミュレーションのために加熱ポートを追加しています。加熱ポートはModelica.Thermalライブラリで定義されています。典型的なパラメータセットは以下の通りです（パラメータVtはもはや使用されていません）。
  - Electrical.Analog.Examples.Utilitis.Transister
  - Since the simple bipolar transistor model does not have base or collector resistances both are added in this component. Additionally, a capacity is added to the base pin. See the schematic for more details. In such a way the transistor model can be enhanced to become more common.
  - 単純なバイポーラトランジスタのモデルではベース抵抗とコレクタ抵抗がないため，この部品では両方を追加しています。また，ベース端子には容量が付加されています。詳しくは回路図をご覧ください。このようにして、トランジスタモデルをより一般的なものにすることができます。
- MOSFET
  - Electrical.Analog.Semiconductors.PMOS NMOS
  - The PMOS model is a simple model of a p-channel metal-oxide semiconductor FET. It differs slightly from the device used in the SPICE simulator. For more details please care for [Spiro1990]. A heating port is added for thermal electric simulation. The heating port is defined in the Modelica.Thermal library. The model does not consider capacitances. A high drain-source resistance RDS is included to avoid numerical difficulties.
  - PMOSモデルは、pチャネルの金属酸化膜半導体FETのシンプルなモデルです。SPICEシミュレータで使用されているデバイスとは若干異なります。詳細は[Spiro1990]を参照してください。熱電シミュレーションのために，加熱ポートを追加しました。この加熱ポートはModelica.Thermalライブラリで定義されています。このモデルではキャパシタンスを考慮していません。数値的な問題を避けるために、高いドレイン-ソース抵抗RDSが含まれています。
- IGBT
  - BipolarとMOSFETの複合デバイス
  - PNP型のBipolar TransisitorとMOSFETのダーリントン接続
- NPN
  - →(Emitter)が出る方
  - EmitterはGround
  - プラスコモン、電源の正極とセンサ出力の間に不可を設置
  - C->B, B->Eに流れる
- PNP
  - →(Emitter)が入る方
  - Emitterは正極
  - マイナスコモン、電源の負極とセンサ出力の間に不可を設置
  - E->C, E->Bに流れる
