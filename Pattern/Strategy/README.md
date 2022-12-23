# Strategy

# Strategyパターン
## 使い所
- オープンクローズドの原則の基本的なデザインパターン
- Clean Architecture 第24章 部分的な境界 P.213 簡易的な境界の作り方としてStrategyパターンを使う例が紹介されている。

## 実装方法
``` plantuml
@startuml
Strategy <|-- ConcreteStrategy1
Strategy <|-- ConcreteStrategy2
Context o- Strategy
@enduml
```

