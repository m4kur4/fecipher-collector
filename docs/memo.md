# メモ
https://fecipher.jp/

## URL
### カード一覧
https://fecipher.jp/cards_category/{ ブースターパック・スターターデッキ番号 }/  
| 接頭辞 | 意味 |
| -- | -- |
| bt | ブースターパック |
| st | スターターパック |

* 一覧にページングなし

### カード詳細
https://fecipher.jp/cards/{ カード番号 }

## データ構造

| # | column | required | description | example |
| :--:| -- | -- | -- | -- |
| 1 | ID | ○ | 識別ID | 1000 |
| 2 | Title | ○ | 二つ名 | 三竜将の奸将 |
| 3 | Name | ○ | キャラクター名 | ナーシェン |
| 4 | ClassRank | ○ | クラス | 上級職 |
| 5 | ClassName | ○ | 職業 | ドラゴンマスター |
| 6 | EntryCost | ○ | 出撃コスト | 4 |
| 7 | CCCost | ○ | クラスチェンジコスト | 3 |
| 8 | Attack | ○ | 攻撃力 | 60 |
| 9 | Support | ○ | 支援力 | 30 |
| 10 | Range | ○ | 射程 | 1 |
| 11 | UnitType | ○ | 兵種 | 飛行／竜 |
| 12 | SkillName1 | - | スキル名1 | 竜将のルーンソード |
| 13 | SkillType1 | - | スキル種別1 |　起動型／1ターンに1回 |
| 14 | SkillText1 | - | スキル効果1 |【[リバース1]】ターン終了まで、このユニットに<魔法>と射程１−２が追加される。 |
| 15 | SkillName2 | - | スキル名2 | 策士の邪笑 |
| 16 | SkillType2 | - | スキル種別2 | 常時型 |
| 17 | SkillText2 | - | スキル効果2 | このユニットが戦闘している場合、支援スキルを持つ相手の支援カードは敵の支援に失敗する。 |
| 18 | SkillName3 | - | スキル名3 | デルフィの守り |
| 19 | SkillType3 | - | スキル種別3 | 自動型 |
| 20 | SkillText3 | - | スキル効果3 | このユニットが攻撃されるたび、戦闘終了まで、攻撃ユニットは『飛行特効』を失い、新たに得ることもできない。 |
| 21 | SkillName4 | - | スキル名4 |  |
| 22 | SkillType4 | - | スキル種別4 |  |
| 23 | SkillText4 | - | スキル効果4 |  |