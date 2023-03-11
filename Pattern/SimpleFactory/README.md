# Simple Factory パターン

## 概要
- Gofのパターンではない
- `Factoryクラス` を作ることで具象クラスのインスタンス化の責務をカプセル化する
    - `Factoryクラス` は `static`クラスとする。
- `Open/Closedの原則`、 `依存性注入`などを取り入れることができる。
    - `Opne/Closedの原則`: `Client`は `抽象クラス`のみに依存する。
    - `依存性注入`: `Client`は、具象クラスのインスタンスの責務が無いので外部から受け取れる
- `クラスのカプセル化`できる。
    - `Factoryクラス`と `抽象クラス`のみを `Public`にして、具象クラスをカプセル化できる。

## C#のデザインパターン


### Factoryパターンが無い場合
``` plantuml
@startuml
class ProductSqlServer {
    + GetData()
}
class ProductFake {
    + GetData()
}
Form1 -> ProductSqlServer
Form1 -> ProductFake
ProductSqlServer --[hidden] ProductFake

note top of Form1
Clientコードが各クラスに依存している。
Productが増えるとClientコードの修正が必要
end note
@enduml
```

### Factoryパターンを使う場合
``` plantuml
@startuml
interface IProduct {
    + GetData();
}

class Factory {
    + Create();
}

Form1 -> IProduct
Form1 --> Factory
IProduct <|-- ProductSqlServer
IProduct <|-- ProductFake
ProductSqlServer <-- Factory
ProductFake <-- Factory

note top of Form1
依存先が抽象クラスになった。
しかし、生成できるクラスをCliantコードが決めているため
テストコードが作りにくい。
end note

note bottom of Factory
Factoryクラスに具象クラスのインスタンス化の責務を移した
end note
@enduml
```

### クラス図完成形
``` plantuml
@startuml
interface IProduct {
    + GetData();
}

class Factory {
    + Create();
}

Form1 -> Form1ViewModel
Form1 --> Factory
Form1ViewModel -> IProduct
IProduct <|-- ProductSqlServer
IProduct <|-- ProductFake
IProduct <|-- ProductMock
ProductSqlServer <-- Factory
ProductFake <-- Factory
ProductMock <-- Factory

note top of Form1ViewModel
Form1ViewModelを作ることで依存性の注入をForm1からできるようになった。
これにより、実際のコードには無いProductMockクラスを
Form1ViewModelへ注入して単体テストを実行できるようになった。
end note

note bottom of Factory
本例ではFactoryクラスを別のクラスにしているが
抽象クラスに各具象クラスのインスタンス化のロジックを書いても良い
※個人的には継承の矢印と逆向きの依存関係の矢印ができるのであまり好きではない。
end note
@enduml
```
