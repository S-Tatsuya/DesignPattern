# DesignPattern

書籍などで勉強したDesignPatternのコードを記録するRepository

## デザインパターン一覧

| No. | パターン名 | 概要 | 使用経験 | その他 | Head First | GoF | Java | C# | Game | TDD | Adaptive Code |
| :---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|1.| [Abstract Factory](./Pattern/AbstractFactory)| Factoryクラスの単位で差し替えることができるパターン | × | |○|○|○|○|-|-|-|
|2.| [Adapter](./Pattern/Adapter) | 外部ライブラリを使う場合など使いたい機能と使う側のインターフェースを揃える。クライアントコード、サービスコードに修正が不要 | × |  |○|○|○|○|-|-|-|
|3.| [Bridge](./Pattern/Bridge)|   各機能を構成する要素をつなぐことで柔軟に機能追加できるようにする。集約のパターンと同じ | × |  |-|○|○|-|-|-|-|
|4.| [Builder](./Pattern/Builder) | 作成する責務のクラスと作成されるクラスの責務を分ける。同じ作成過程で異なるクラスを生成することができるようにする。 | × |  |-|○|○|-|-|-|○|
|5.| [Bite Code](./Pattern/BiteCode) | ? | × |  |-|-|-|-|○|-|-|
|6.| [Chain Of Responsibility](./Pattern/ChainOfResponsibility)| 複数のクラスの処理をつなげて処理できるようにする。 | × |  |-|○|○|-|-|-|-|
|7.| [Command](./Pattern/Command)| コマンドの再利用性や拡張性を高める | × |  |○|○|○|-|○|-|-|
|8.| [Component](/Pattern/Component)| ? | × |  |-|-|-|-|○|-|-|
|9.| [Composite](./Pattern/Composite)| ツリー構造を表現する手段に使われる | × |  |○|○|○|○|-|-|-|
|10.| [Compound](./Pattern/Compound) | ? | × |  |○|-|-|-|-|-|-|-|
|11.| [Data Localization](./Pattern/DataLocalization)| ? | × |  |-|-|-|-|○|-|-|
|12.| [Decorator](./Pattern/Decorator)| クラスの処理をクラスをまたいで追記したい場合の使われる | × |  |○|○|○|-|-|-|-|
|13.| [Double Buffer](./Pattern/DoubleBuffer) | ? | × |  |-|-|-|-|○|-|-|
|14.| [Dirty Flag](./Pattern/DirtyFlag) | ? | × |  |-|-|-|-|○|-|-|
|15.| [Event Queue](./Pattern/EventQueue)| ? | × |  |-|-|-|-|○|-|-|
|16.| [Facade](./Pattern/Facade) | サブクラスの機能をまとめて理想の動作をするクラスを作る。 | × |  |○|○|○|○|-|-|-|
|17.| [Factory Method](./Pattern/FactoryMethod)| オブジェクトの生成を具体的な処理と分離することでオブジェクト再利用性を高める | × | |○|○|○|○|-|-|-|
|18.| [Flyweight](./Pattern/Flyweight)| オブジェクトを共有してメモリの使用量を少なくする | × |  |-|○|○|-|○|-|-|
|19.| [Game Loop](./Pattern/GameLoop) | ? | ? | |-|-|-|-|○|-|-|
|20.| [Humble Object](./Pattern//HumbleObject/) | テストしやすい複雑な機能とテストしにくい簡単な機能に分割して、  複雑なテストをテストできる状態にしておく | × | Clean Architectureより |-|-|-|-|-|-|-|
|21.| [Interpreter](./Pattern/Interpreter) | 規則性をもった分の構文を解析するパターン | × |  |-|○|○|-|-|-|-|
|22.| [Iterator](./Pattern/Iterator)| 集合の中身を気にせずアルゴリズムに沿って順番に出力する | × |  |○|○|○|-|-|-|-|
|23.| [Mediator](./Pattern/Mediator)| オブジェクト間のデータの受け渡しを代理する。 | × | |-|○|○|-|-|-|-|
|24.| [Memento](./Pattern/Memento) | オブジェクトの状態を保存することで元の状態に戻せるようにする | × | |-|○|○|-|-|-|-|
|25.| [Object Pool](./Pattern/ObjectPool)| ? | × |  |-|-|-|-|○|-|-|
|26.| [Observer](./Pattern/Observer)| 変更があった場合に関連するクラスに通知を行うパターン。ポーリングを防ぐことができる | × |  |○|○|○|○|○|-|-|
|27.| [Prototype](./Pattern/Prototype) | インスタンスのコピーを作成する仕組みを提供するパターン | × |  |-|○|○|-|○|-|-|
|28.| [Proxy](./Pattern/Proxy)| オブジェクトの代わりに処理を行う。 | × |  |-|○|○|-|-|-|-|
|29.| [Service Locator](./Pattern/ServiceLocator)| ？ | × |  |-|-|-|-|○|-|-|
|30.| [Singleton](i./Pattern/Singleton)| プロジェクト内で必ず一つしかインスタンス化されないクラス | × |  |○|○|○|○|○|-|-|
|31.| [Simple Factory](./Pattern/SimpleFactory)| 生成するインスタンスの判定をカプセル化するパターン | × |  |-|-|-|○|-|-|-|
|32.| [Space Division](./Pattern/SpaceDivision)| ? | × |  |-|-|-|-|○|-|-|
|33.| [State](./Pattern/State)| 状態をクラスで表現することで、各状態の動きを定義することができる | × | |○|○|○|-|○|-|-|
|34.| [Strategy](./Pattern/Strategy)| 戦略を実装して、選択できるようにすることで目的を達成する。| × | |-|○|○|-|-|-|-|
|35.| [Sub Class Sandbox](./Pattern/SubClassSandbox)| ? | × | |-|-|-|-|○|-|-|
|36.| [Template Method](./Pattern/Template)| 外部へは共通インターフェースを提供して、サブクラスで処理することで機能追加を用意にできるようにする | × | |○|○|○|-|-|-|-|
|37.| [Type Object](./Pattern/TypeObject)| ? | × | |-|-|-|-|○|-|-|
|38.| [Update Method](./Pattern/UpdateMethod) | ? | ? | |-|-|-|-|○|-|-|
|39.| [Visitor](./Pattern/Visitor)| 複数のクラスにまたがった処理を作成するときに使う | × | |-|○|○|-|-|-|-|
| No. | パターン名 | 概要 | 使用経験 | その他 | Head First | GoF | Java | C# | Game | TDD | Adaptive Code|
