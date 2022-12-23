# Humble Object

# Humble Objectパターン
## 使い所
- MVVMのようなパターンで使われている。
- テストが難しいGUIの部分や、DBから取得するデータ部分をテストしない簡単な機能としてまとめる。  
それ以外のロジックをテスト可能な複雑な機能としてまとめる。


## 実装方法
``` plantuml
@startuml
Class ViewModel <<DS>> {}
note left of ViewModel : Presenterが作ったデータをViewが読み込むためのData Structure Class
Presenter --> ViewModel
note left of Presenter : 複雑なロジックを含むClass
ViewModel <-- View
note left of View : 簡易的な機能のみを含むClass
@enduml
```