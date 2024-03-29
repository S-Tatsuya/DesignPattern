from src.CaffeineBeverage import CaffeineBeverage


class Coffee(CaffeineBeverage):
    def brew(self):
        return "フィルタでコーヒーをドリップします"

    def add_condiments(self):
        return "砂糖とミルクを追加します"

    def customer_wants_condiments(self):
        return self._is_condiments()

    def _question(self):
        print("コーヒーに砂糖とミルクをいれますか？(y/n)")
