
フェーリング液:
  cn: 斐林试剂
  formula: Cu2+ -> Cu2O #アルデヒド -> カルボン酸
  desc: 斐林试剂（Fehling's reagent）用来区分水溶性的醛及酮官能基，也可以用来测定单糖。

アルコール:
  価数: OH数量
  級: R数量
  αβ炭: OH相连的是α 远一个位置的是β => C(β)-C(α)-OH
  inspection: 2R-OH +2Na ->  2R-OHNa + H2
  equation:
    脱水:
      CH3CH2OH:
         catalyst: 濃H2SO4
         130~140: CH3CH2OCH2CH3
         160~170: CH2=CH2

  property:
    - 易溶於水
    - 不電離 -> 中性
  メタノール:
    - 無色
    - 毒性 -> ギ酸
  エターナル:
    - 葡萄糖发酵
    - 消毒剂

  エーテル:
    property:
      - 易燃易爆
      - 麻醉性
      - 不与Na反应

  カルボニル基:
    アルデヒド:
      production: 一级アルコール酸化
      反応:
        - 銀鏡反応: R-CHO 1:2 || H-CHO 1:4
        - フェーリング液: Cu2O 赤色沉淀
      ホルムアルデヒド:
        - 37% -> ホルマリン
      アセトアルデヒド:
        - 無色刺激臭
        - 悪酔い
    ケトン:
      production: 二级アルコール酸化
      アセント:
        production: クメン法副產物
    ヨードホルム反応:
      desc: I2 + NaOH aq -> CHI3
      note: 特殊臭气 黄色沉淀 检出CH3CRHOH or CH3COR