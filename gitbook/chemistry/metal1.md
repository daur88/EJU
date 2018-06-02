
NaOH:
  property: 潮解 溶解发热
  production:
    industry: イオン交換膜

NaCO3:
  property: 風解
  equation:
    - NaCO3·10H20 -> NaCO3·H20
    - NaCO3 + H2O <-> NaHCO3 + NaOH
    - NaCO3 + SiO2 -> NaSiO3 + CO2  ···Na2O·SiO2
    - CaO + SiO2 -> CaSiO3 ···CaO·SiO2

  note: 漫长
  usage: 玻璃、石碱 合成洗剤
  production:
    industry: アンモニアソーダ法　(ソルベー法)
    note: NaHCO3 为止 => ソルベー法

NaHCO3:
  desc: 重曹
  usage: 入浴剤　ふくらし粉(ベーキングパウダー)　胃薬
  equation:
    - 2NaHCO3 -> Na2CO3 + CO2 + H2O
    - NaHCO3 + HCl -> NaCl + CO2 + H2O

アルカリ金属区別:
    Be: &be
      property:
        - 不与水反应
        - 无焰色反应
        - 氧化物不溶于水
        - 硫酸盐溶于水
        - 碳酸盐微溶于水
    Mg: *be
Ca:
  石膏:
    formula: CaSO4·2H2O
  焼き石膏:
    formula: CaSO4·1/2H2O

両性金属:
  desc: Al、Zn、Sn、Pb

錯イオン:
  NH3:
    equation:
      - Zn2+ -> ZnO {白}  -> [Zn(NH3)4]2+ {| 正四面体}
      - Cu2+ {青} -> ZnO {青白}  -> [Cu(NH3)4]2+ {深青 | 平面正方形}
      - Ag+ -> Ag2O {褐色}  -> [Ag(NH3)2]+ { | 直線}
  NaCN:
    equation:
      - Fe2+ -> [Fe(CN)6]4+ {淡黄 | 正八面体}
      - Fe3+ -> [Fe(CN)6]3+ {黄 | 正八面体}

Al:
  usage: 高压电线
  ジュラルミン: Al·Cu·Mg·Mn合金 飞机机体
  テルミット反応: テルミット(Al、Fe混合物)
  ミョウバン:
    alias: 明礬
    formula: AlK(SO4)2・12H2O