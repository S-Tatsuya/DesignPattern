# Flyweight

# Flyweightパターン
## 使い所
メモリ使用量が多いデータを共有する場合に使用することで、同じデータを復数生成して、メモリ使用量が大きくなることを防ぐことができる。  
注意点として、共有するデータのため、基本的には書き換えしない形で保持することが重要。  
-> 書き換えをするとどのオブジェクトがそのデータを使っているかの影響を考慮して設計する必要があり、バグが発生しやすい。

## 実装方法
``` plantuml
@startuml

ClientA --> FlyweightFactory: 利用
ClientB --> FlyweightFactory: 利用
FlyweightFactory o-- FlyweightA
FlyweightFactory o-- FlyweightB

class FlyweightFactory {
    _instances = {}
    get_instance()
}

@enduml
```



