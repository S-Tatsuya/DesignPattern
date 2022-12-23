# Iterator

# Iterator

## 使い所

## 実装方法
``` plantuml
@startuml
Aggregate -> Iterator
Aggregate <|-- ConcreteAggregate
Iterator <|-- ConcreteIterator
ConcreteAggregate -o ConcreteIterator

interface Aggregate{}
interface Iterator{}
@enduml
```

