# Decorator
```
Decoratorパターンはオブジェクトに付加的な責務を動的に付与します。  
デコレータは、サブクラス化の代替となる、柔軟な機能拡張手段を提供します。
```
- ラッパーを使って、対象をデコレーションする。
- 機能の追加を既存のコードを変更せずに行い、動的に切り替えることもできる。

## 使い所

## 実装方法
``` plantuml
@startuml
Component <|-- ConcreteComponent
Component <|-- Decorator
Component --o Decorator
Decorator <|-- ConcreteDecorator

abstract Component {
    operation()
}
abstract Decorator{}
@enduml
```

- HeadFirstのクラス図
``` plantuml
@startuml
class Component {
    methodA()
    methodB()
}

class Decorator {
    Component
}

class ConcreteDecoratorA {
    newBehavior()
    // other method()
}
class ConcreteDecoratorB {
    Object
    // other member
    newBehavior()
    // other method()
}
Component <|-- ConcreteComponent
Component <|-- Decorator
Component <-- Decorator : has
Decorator <|-- ConcreteDecoratorA
Decorator <|-- ConcreteDecoratorB
@enduml
```

- HeadFirstのスタバのクラス図
``` plantuml
@startuml
Abstract Beverage {
    description
    getDescripition()
    cost()
}

Abstract CondimentDecorator {
    Beverage
    getDescripition()
}

note top of Beverage : "Interfaceでも良い"

Beverage <|-- HouseBlend
Beverage <|-- DarkRoast
Beverage <|-- Espresso
Beverage <|-- Decaf

Beverage <|-- CondimentDecorator
CondimentDecorator <|-- Milk
CondimentDecorator <|-- Mocha
CondimentDecorator <|-- Soy
CondimentDecorator <|-- Whip
@enduml
```

- HeadFirstのスタバのシーケンス図
    - ホイップ付きのダブルモカ、豆乳ラテ
``` plantuml
@startuml
Manager -> Whip : cost()
Whip -> Mocha1 : cost()
Mocha1 -> Mocha2 : cost()
Mocha2 -> Soy : cost()
Soy -> DarkRoast : cost()
Soy <-- DarkRoast : return DarkRoast
Mocha2 <-- Soy : return DarkRoast + Soy
Mocha1 <-- Mocha2 : return DarkRoast + Soy + Mocha2
Whip <-- Mocha1 : return DarkRoast + Soy + Mocha2 + Mocha1
Manager <-- Whip : return DarkRoast + Soy + Mocha2 + Mocha1 + Whip
@enduml
```


## HeadFirst
### 継承の問題点
- 継承を単純に使うとコンパイル時に振る舞いが静的に決定してしまう。
    - 動作の決定を実行時に遅らせることができない
- スーパークラスで定義したすべてのメソッドがサブクラスに継承されてしまう。

### 継承を使う理由
- スーパークラスの振る舞いを取得するため
- スーパークラスと型を一致させるため

### Open/Closedの原則
- 変化する可能性の高い部分に対して**Interface**を導入して実現する。
    - すべてのコードに適用しても複雑性が**無駄に**増してしまう。
- **Open**:新しい機能（振る舞い）の追加をコードを追加することで実現できる。
- **Close**:新しい機能（振る舞い）の追加時に既存のコードを変更させない。

