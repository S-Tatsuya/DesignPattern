from src.CaffeineBeverage import CaffeineBeverage


class Tea(CaffeineBeverage):
    def brew(self):
        return "紅茶を浸します"

    def add_condiments(self):
        return "レモンを追加します"

    def customer_wants_condiments(self):
        return self._is_condiments()

    def _question(self):
        print("紅茶にレモンをいれますか?(y/n)")
