# Stateパターン
```
Stateパターンでは、オブジェクトの内部状態が変化した際にオブジェクトがその振る舞いを変更できます。
オブジェクトはそのクラスを変更したように見えます。
```
## 使い所
- 内部状態によって振る舞いを変化させたいオブジェクトを実装する場合

## 実装方法
``` plantuml
@startuml
State <|-- ConcreteState1
State <|-- ConcreteState2
Context o- State
@enduml
```

## HeadFirst
### if文の実装の問題点
1. 状態がif文の構造に隠れて明確ではなくなる。
2. 1つの状態の変更が他の全ての状態に影響を与えてる。

### 改善するためには
1. 影響範囲をカプセル化するために各状態をクラス化する。
2. 各状態の振る舞いは各状態のオブジェクトに委譲する。

``` plantuml
@startuml
interface IState{
    insertQuarter()
    ejectQuarter()
    turnCrank()
    dispense()
}

Context -> IState
IState <|-- SoldState
IState <|-- SoldOutState
IState <|-- NoQuarterState
IState <|-- HasQuarterState
@enduml
```

### 気になること
1. クラス図ほどきれいな依存関係ではない。
    - `Context`は`IState`の具象クラスに依存している。
    - `IState`の具象クラス同士も依存している。(ハードコーディングは避けれてはいる)
    - `開放閉鎖の原則`を破ることになりパターン

2. 本当に多くの具象クラスがある場合は、遷移の判定を別のクラスに委譲してもいいかも。
    - `Context`のコンストラクタでも状態遷移の判定をしている。
    - `IState`の具象クラスが`Context`の状態を見る必要が有る。
        - 実質循環参照になっている。


## デザインパターン
### 関連しているパターン
|パターン|内容|
|---|---|
|Singletonパターン|ConcreteStateは、Singletonで実装されることが多い|
|Flyweightパターン|ConcreteStateは、インスタンス変数を持たない場合、Flyweightで実装することができる。|

``` plantuml
@startuml
class Stateパターン {}
Stateパターン - 併用
併用 - Singletonパターン
併用 - Flyweightパターン
Singletonパターン --[hidden] Flyweightパターン
@enduml
```

