from src.CaffeineBeverage import CaffeineBeverage


class Coffee(CaffeineBeverage):
    def brew(self):
        return "フィルタでコーヒーをドリップします"

    def add_condiments(self):
        return "砂糖とミルクを追加します"
