# ChainOfResponsibility

# Chain Of Responsibilityパターン

## 使い所


## 実装方法
``` plantuml
@startuml

Handler o-- Handler
Handler -- ConcreteHandler

abstract Handler {
    set_next()
    handler()
    done()
    end()
    {abstract} filter()

}
@enduml
```

