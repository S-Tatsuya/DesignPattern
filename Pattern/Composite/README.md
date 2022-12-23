# Composite

# Compositeパターン
## 使い所
同じ抽象クラス(Component)から、CompositeとReafを作ることで、お互いに依存せずにコードを書くことができる。  
CompositeとReafの違いは、それぞれのクラスが知っていれば良いので、クライアント側はComponentクラスのことのみ知っていれば良い。


## 実装方法
``` plantuml
@startuml
Component <|-- Reaf
Component <|-- Composite
@enduml
```


