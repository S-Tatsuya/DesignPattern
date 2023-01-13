# Template

## 概要
`Template Method pattern` は共通のアルゴリズムを持つが、  
一部の詳細な処理が異なる場合に利用できるデザインパターン

 抽象クラスが処理の全体像を定義して、サブクラスはその**特化**(サブクラスごとの差異)のみを実装する。  
-> **何に特化**しているのかをサブクラスを見るだけで把握できる。

- Hook(フック)メソッド: デフォルトの処理があるが、必要であればサブクラスで実装できるメソッド
    - 抽象メソッドのように処理の実装を強制しない
    - final メソッドのように処理の実装を禁止しない

- Hookを使うことで抽象クラスに対する判断を行う能力をサブクラスに与えることができる

## 使い所
共通のアルゴリズムを持ち、詳細のみ異なるクラスを定義することができる。


## 0.1 実装方法
``` plantuml
@startuml
AbstractClass <|-- ConcreteClassA
AbstractClass <|-- ConcreteClassB

abstract AbstractClass {
    template_method()
}
@enduml
```
## HeadFirst

### CoffeeとTeaのリファクタリング

0. 前提
``` plantuml
@startuml
class Coffee {
    <color:blue>prepare_recipe()</color>
    <color:blue>boil_water()</color>
    brew_coffee_grinds()
    <color:blue>pour_in_cup()</color>
    add_sugar_and_milk()
}

class Tea {
    <color:blue>prepare_recipe()</color>
    <color:blue>boil_water()</color>
    steep_tea_bag()
    <color:blue>add_lemon()</color>
    pour_in_cup()
}
@enduml
```

1. 共通の処理(前提の青字)を抽象クラスに抜き出す
``` plantuml
@startuml
abstract CaffeineBeverage {
    <color:blue>{abstract} prepare_recipe()</color>
    boil_water()
    pour_in_cup()
}

class Coffee {
    <color:blue>prepare_recipe()</color>
    brew_coffee_grinds()
    add_sugar_and_milk()
}

class Tea {
    <color:blue>prepare_recipe()</color>
    steep_tea_bag()
    add_lemon()
}

CaffeineBeverage <|-- Coffee
CaffeineBeverage <|-- Tea
@enduml
```

2. 共通のアルゴリズムのメソッド(1. の青字)を抽象化する
``` plantuml
@startuml
abstract CaffeineBeverage {
    prepare_recipe()
    boil_water()
    {abstract} berw()
    pour_in_cup()
    {abstract} add_condiments()
}

class Coffee {
    berw()
    addCondiments()
}

class Tea {
    berw()
    add_condiments()
}

CaffeineBeverage <|-- Coffee
CaffeineBeverage <|-- Tea
@enduml
```

3. Hook(下図の青字)を使ってCoffeeのサブクラスだけ処理を変更
``` plantuml
@startuml
abstract CaffeineBeverage {
    prepare_recipe()
    boil_water()
    {abstract} berw()
    pour_in_cup()
    {abstract} add_condiments()
    <color:blue>customer_wants_condiments()</color>
}

class Coffee {
    berw()
    addCondiments()
    <color:blue>customer_wants_condiments()</color>
}

class Tea {
    berw()
    add_condiments()
}

CaffeineBeverage <|-- Coffee
CaffeineBeverage <|-- Tea
@enduml
```

4. Teaにも`3.`と同様の対応を行う
``` plantuml
@startuml
abstract CaffeineBeverage {
    prepare_recipe()
    boil_water()
    {abstract} berw()
    pour_in_cup()
    {abstract} add_condiments()
    <color:blue>customer_wants_condiments()</color>
}

class Coffee {
    berw()
    addCondiments()
    <color:blue>customer_wants_condiments()</color>
}

class Tea {
    berw()
    add_condiments()
    <color:blue>customer_wants_condiments()</color>
}

CaffeineBeverage <|-- Coffee
CaffeineBeverage <|-- Tea
@enduml
```

## デザインパターン入門 
### 関連パターン
- 一覧
|name|分類|概要|
|---|---|---|
|Factory Method|応用|Template Methodの応用パターン|
|Stragtegy|類似|Template Methodは**継承**でアルゴリズムの**一部**を切り替える。  Strategyは**委譲**でアルゴリズムの**全て**を切り替える|

- 図
``` plantuml
@startuml
class TemplateMethod {}
TemplateMethod <-- FactoryMethod: 応用
TemplateMethod - Stragtegy: 類似
@enduml
```
