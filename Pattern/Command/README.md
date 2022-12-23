# Command pattern
メソッドの呼び出しを具現化するパターンの特徴
1. メソッドの呼び出しをクラス化して、インスタンスを入れ替えることで処理を動的に切り替えることができるようにする。
2. 依存性の注入でメソッドを汎用化できる
3. 基本的には`execute()`,`undo()`を備える

## 概要
- アクションの要求者とそのアクションを実行するオブジェクトを分離できる。

## 説明
- リクエストをオブジェクトとしてカプセル化する。  
    - メソッドの呼び出しを`execute()`メソッドを持つCommandインターフェースに統一する。  
    - Clientは`execute()`すればリクエストが実行されることだけを知っている。  

- その結果、他のオブジェクトを以下の形でパラメータ化できる。
    - パラメータ化の方法
        - リクエスト
        - キュー
        - ログリクエスト
    - パラメータ化とは、ClientはCommandインターフェースを持つオブジェクトを入れ替えてリクエストを実行することができる。
- アンドゥ可能な操作もサポートする。
    - キュー、ログリクエストを持つことで実現できる。

## 使い所


## 実装方法
- Udemy:Pythonのデザインパターン
Invoker = 起動者
``` plantuml
@startuml
Invoker -o Command
Command <|-- ConcreteCommand
ConcreteCommand o- Receiver

abstract Command {
    execute()
}
@enduml
```

- Head first:クラス図
``` plantuml
@startuml
Client -> Receiver : 生成
Client -> ConcreteCommand : 生成
Receiver <- ConcreteCommand : 実行
Command <|-- ConcreteCommand
Invoker -> Command

Interface Command {
    execute()
    undo()
}

class Invoker {
    setCommand(Command)
    actionCommand()
}

class Receiver {
    action()
} 
@enduml
```

- Head First:例.リモコンと機能
``` plantuml
@startuml
リモコン -> Command
Command <|-- ConcreteCommand
ConcreteCommand -> LightSwitch
ConcreteCommand --> TvSwitch

abstract Command {
    execute()
    undo()
}
@enduml
```

- Head first:例.オブジェクト町 食堂
インボーカ = 起動者
``` plantuml
@startuml
クライアント -> コマンド : createCommandObject()
クライアント ..> インボーカ : execute()
コマンド --> インボーカ : setCommand()
インボーカ --> コマンド : execute()
コマンド -> レシーバ : action()
@enduml
```

- Head first:例.リモートコントロールAPI
``` plantuml
@startuml
RemoteLoader ..> LightOnCommand : 生成 -> Lightをセット
RemoteLoader ..> LightOffCommand : 生成 -> Lightをセット
RemoteLoader --> Light : 生成
RemoteLoader -[hidden] RemoteControl
RemoteControl -> ICommand : has
Cliant --> RemoteControl : use
ICommand <|-- LightOnCommand
ICommand <|-- LightOffCommand
Light <- LightOnCommand : use
Light <-- LightOffCommand : use

Interface ICommand{
    execute()
}
note top of ICommand 
    Command Interfaceを使って、
    LightのON、OFF操作を
    カプセル化している。
    InvokerのRemoteContorolは
    Cliantに指示されたslotの
    execute()を実行するだけで
    様々なクラスを使用することができる。
end note
@enduml
```

## 参考書籍
- [Game Programming Patterns](https://www.amazon.co.jp/Programming-Patterns-ソフトウェア開発の問題解決メニュー-impress-gearシリーズ-ebook/dp/B015R0M8W0/ref=sr_1_1?crid=2DW0VKCLAEIXQ&keywords=game+programming+patterns&qid=1670129877&sprefix=game+prog%2Caps%2C212&sr=8-1)
- [Head First デザインパターン](https://www.amazon.co.jp/Head-Firstデザインパターン-―頭とからだで覚えるデザインパターンの基本-Eric-Freeman/dp/4873112494/ref=sr_1_7?__mk_ja_JP=カタカナ&crid=35ZU66TW13MT1&keywords=head+first&qid=1670129893&sprefix=head+firs%2Caps%2C181&sr=8-7)
