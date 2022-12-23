# Mediarot

# Mediator
## 使い所

``` plantuml
@startuml
ClassA <-> Mediator
ClassB <--> Mediator
Mediator <-> ClassC
Mediator <--> ClassD

class ClassA{}
@enduml
```

## 実装方法
``` plantuml
@startuml
Mediator <|-- ConcreteMediator
Mediator -o Colleague
Colleague <|-- ConcreteColleague1
Colleague <|-- ConcreteColleague2
ConcreteMediator o- ConcreteColleague1
ConcreteMediator o- ConcreteColleague2
@enduml
```

