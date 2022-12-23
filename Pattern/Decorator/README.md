# Decorator

# Decoratorパターン
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

