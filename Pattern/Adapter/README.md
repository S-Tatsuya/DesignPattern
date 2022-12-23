# Adapter

# Adapter
外部ライブらいなどを使う場合に使いたい機能と使う側のインターフェースを揃える。  
クライアント側、サービス側のどちらのコードも修正する必要が無い。  
単語の意味：適合させるもの

## 使い所
- 使いたい振る舞いを持つクラスがあるが、使いたい側が期待するインターフェースでは無い場合。

## 実装方法
2つの実装方法があるが、基本的にはコンポジションを推奨。
- コンポジション：集約ではない理由は、アダプターがない状態では部品は使えないため
- 継承：サービス側のクラスを継承する。二重継承をサポートしていない言語など制約が多くコンポジションより優れる点は無い。
- Adapteeインターフェース：複数のAdapteeを切り替えることでサービス側のクライアントを切り替える事ができる。

``` plantuml
@startuml
Adaptee <|-- ConcreteAdaptee1
Adaptee <|-- ConcreteAdaptee2

ConcreteAdapter1 --|> Adapter
ConcreteAdapter2 --|> Adapter

ConcreteAdaptee1 <-- ConcreteAdapter1: 利用
ConcreteAdaptee2 <-- ConcreteAdapter2: 利用

interface Adaptee{}
interface Adapter{}
@enduml
```

## メリット
- クライアント側、サービス側のコード変更が不要なため、オープン・クローズドの原則を守ることができる
- Adapteeインターフェースを使った実装とする場合は、集約の関係になる。依存性注入ができるので、テストはしやすい。
- コードのひょうな変更を避けることができる。オープン・クローズドの原則を守るため

##  参考URL
[udemy:ピーター・アンダーソン](https://www.udemy.com/course/design02/learn/lecture/30270046#overview)

