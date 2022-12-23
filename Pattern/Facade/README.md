# Facade

# Facade
サブクラスの機能をまとめて理想の動作をするクラスを作るパターン。  
サブシステムを利用する側が容易に使用できるようにする。  
単語の意味：建物の正面。窓口。

## 使い所
- 複数のサブクラスはあるが、使いたい機能を単独のサブクラスだけでは実現できない場合。
- ValueObjectなどをまとめて一つのクラスを作る場合。
- 他システムと連携する場合。

- Clean Architecture 第7章 SRP：単一責務の原則 P.85にて活用の例がある。
- Clean Architecture 第24章 部分的な境界 P.213 完全な境界ではないが、Facadeを使うことで複数のServiceへの依存をまとめて、簡易的な境界として、分離しやすい状態で設計する例がある。
``` plantuml
@startuml
class EmployeeFacade {
    + calculatePay()
    + reportHours()
    + save()
} 

class EmployeeFacade #back:pink

class PayCalculator {
    + calculatePay()
}

class HourReporter {
    + reportHours()
}

class EmployeeSaver {
    + save()
}

class EmployeeData{}


EmployeeFacade -> PayCalculator
EmployeeFacade -> HourReporter
EmployeeFacade -> EmployeeSaver
PayCalculator -[hidden]- HourReporter
HourReporter -[hidden]- EmployeeSaver
PayCalculator -> EmployeeData
HourReporter -> EmployeeData
EmployeeSaver -> EmployeeData
@enduml
```

## 実装方法
``` plantuml
@startuml
Client --> Facade : 利用する
Facade o-- ClassA
Facade o-- ClassB
Facade o-- ClassC
Facade o-- ClassD
@enduml
```
## 参考URL
[Udemy:ピーター・アンダーソン](https://www.udemy.com/course/design01/learn/lecture/30071810#overview)


