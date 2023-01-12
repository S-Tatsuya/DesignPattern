from src.CaffeineBeverage import CaffeineBeverage


class Tea(CaffeineBeverage):
    def brew(self):
        return "紅茶を浸します"

    def add_condiments(self):
        return "レモンを追加します"
