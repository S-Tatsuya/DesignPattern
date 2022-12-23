# Visitor

# Vistorパターン
## 使い所


## 実装方法
``` plantuml
@startuml
Vistor <|-- ConcreteVisitor1
Vistor <|-- ConcreteVisitor2
Element <|-- ConcreteElement1
Element <|-- ConcreteElement2
Vistor -o Element
@enduml
```

