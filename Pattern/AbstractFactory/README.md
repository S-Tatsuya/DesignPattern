# Abstract Factory パターン

## 概要
- `Simple Factoryパターン` を管理するためのパターン
- `Factoryクラス` を差し替え可能にするパターン
    - `Simple Factoryパターン` はコンストラクタのカプセル化が目的だった。
- `Factoryクラス` を組み合わせて一つのシステムで生成するものを切り替えたい場合に有効
    - `Simple Factoryパターン` だけでは生成するインスタンスの判定ロジックが重複する場合に有効。
 
<img src="http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/udaken/class_diagram_of_dotnet_containers/main/class_diagram_of_dotnet_containers.puml](https://raw.githubusercontent.com/S-Tatsuya/DesignPattern/main/Pattern/AbstractFactory/README.md&fmt=svg" />

## C#のデザインパターン
### Simple Factoryのパターン
``` plantuml
@startuml
interface IProduct {
    + GetData();
}

interface IStock {
    + GetStock();
}

class ProductFactory {
    + Create();
}

class StockFactory {
    + Create();
}

Form1 --> Form1ViewModel
Form1 --> ProductFactory
Form1 --> StockFactory

Form1ViewModel --> IProduct
Form1ViewModel --> IStock

IProduct <|-- ProductSqlServer
IProduct <|-- ProductFake
IProduct <|-- ProductMock

IStock <|-- StockSqlServer
IStock <|-- StockFake
IStock <|-- StockMock

ProductSqlServer <-- ProductFactory
ProductFake <-- ProductFactory
ProductMock <-- ProductFactory

StockSqlServer <-- StockFactory
StockFake <-- StockFactory
StockMock <-- StockFactory

note bottom of ProductFactory
ProductFactoryとStockFactoryは同じ条件で
それぞれIProductとIStockのインスタンスを生成している。
end note

note top of Form1
ProductFactoryとStockFactoryを使って生成したインスタンスを
Form1ViewModelに注入している。
end note
@enduml
```
### Abstract Factoryのパターン
``` plantuml
@startuml
interface IProduct {
    + GetData();
}

interface IStock {
    + GetStock();
}

class ProductFactory {
    + Create();
}

class StockFactory {
    + Create();
}

abstract class AbstractFactory {
    + ProductCreate();
    + StockCreate();
}

Form1 --> Form1ViewModel

Form1ViewModel --> IProduct
Form1ViewModel --> IStock
Form1ViewModel --> AbstractFactory

IProduct <|-- ProductSqlServer
IProduct <|-- ProductFake
IProduct <|-- ProductMock

IStock <|-- StockSqlServer
IStock <|-- StockFake
IStock <|-- StockMock

ProductSqlServer <-- SqlFactory
ProductFake <-- FakeFactory
ProductMock <-- MockFactory

StockSqlServer <-- SqlFactory
StockFake <-- FakeFactory
StockMock <-- MockFactory

SqlFactory --|> AbstractFactory
FakeFactory --|> AbstractFactory
MockFactory --|> AbstractFactory

note right of Form1ViewModel
AbstractFactoryクラスを受け取り必要なインスタンスを生成する。
end note

note bottom of SqlFactory
各Factoryが必要なインスタンスを理解して生成する。
Factoryを使う側はSql,Fakc,Mockなどを意識しないで使用できる。
end note

ProductFactory -[hidden] StockFactory
note right of StockFactory
個別のクラスのインスタンス化を
責務とするSimple Factoryは不要になる。
end note
@enduml
```

### Abstract Factoryのパターン：個人的思い
``` plantuml
@startuml
interface IProduct {
    + GetData();
}

interface IStock {
    + GetStock();
}

class ProductFactory {
    + Create();
}

class StockFactory {
    + Create();
}

abstract class AbstractFactory {
    + ProductCreate();
    + StockCreate();
}

Form1 --> Form1ViewModel
Form1 -> AbstractFactory

Form1ViewModel --> IProduct
Form1ViewModel --> IStock

IProduct <|-- ProductSqlServer
IProduct <|-- ProductFake
IProduct <|-- ProductMock

IStock <|-- StockSqlServer
IStock <|-- StockFake
IStock <|-- StockMock

ProductSqlServer <-- SqlFactory
ProductFake <-- FakeFactory
ProductMock <-- MockFactory

StockSqlServer <-- SqlFactory
StockFake <-- FakeFactory
StockMock <-- MockFactory

SqlFactory --|> AbstractFactory
FakeFactory --|> AbstractFactory
MockFactory --|> AbstractFactory

note top of Form1
AbstractFactoryを使って各インスタンスを生成するのはForm1で行い
Form1ViewModelはIProduct、IStockを受け取る方が良さそうに見える。
Form1VeiwModelが実際に依存しているインスタンスがわかりやすいため。
end note
@enduml
```
## Clean Archtecture
### 実装方法(AbstractFactory)
複数のクラスを組み合わせることで複雑なインスタンスを生成するパターン
- Clean Architecture 11章 DIP:依存関係逆転の原則 P.105
  - 目的：ビジネスロジック層と具象クラス層の間にインターフェースを用意することで変更の影響範囲を抑える。Factoryクラスも具象クラスなので、影響の範囲外にする必要がある。
  - 抽象クラスに依存するために具象クラスの生成をFactoryクラスに任せる
  - Factoryクラスも具象クラスなのでAbstractFactoryのインターフェースをビジネスロジックはサポートする
  - main関数など全体の制御するクラスが具象クラスのFactoryクラスの生成を行う。
  
```plantuml
@startuml

Factory <|-- ConcreteFactoryA
Factory <|-- ConcreteFactoryB

ProductA <|-- ConcreteProductA1
ProductA <|-- ConcreteProductA2
ProductB <|-- ConcreteProductB1
ProductB <|-- ConcreteProductB2

ProductA <... ConcreteFactoryA : 利用
ProductB <... ConcreteFactoryA : 利用
ProductA <... ConcreteFactoryB : 利用
ProductB <... ConcreteFactoryB : 利用

interface ProductA{
}
interface ProductB{
}
interface Factory{
}
@enduml
```
