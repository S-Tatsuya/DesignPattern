# Interpreter

# Interpreter

## 使い所

## 実装方法
Compositeパターンを使う
``` plantuml
@startuml
Client -> AbstractExpression : 利用
Client --> Context: 作成
AbstractExpression <|-- TerminalExpression
AbstractExpression <|-- NoterminalExpression
AbstractExpression --o NoterminalExpression


abstract AbstractExpression {}
@enduml
```

