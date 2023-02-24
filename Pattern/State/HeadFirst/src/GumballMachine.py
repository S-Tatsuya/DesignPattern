class GumballMachine:
    SOLD_OUT = 0
    NO_QUARTER = 1
    HAS_QUATER = 2
    SOLD = 3

    def __init__(self, count):
        self.count = count
        if count > 0:
            self.state = self.NO_QUARTER
        else:
            self.state = self.SOLD_OUT

    def insert_quarter(self):
        if self.state == self.HAS_QUATER:
            return "もう一度25セントを投入することはできません。"
        elif self.state == self.NO_QUARTER:
            self.state = self.HAS_QUATER
            return "25セントを投入しました。"
        elif self.state == self.SOLD_OUT:
            return "25セントを投入することはできません。このマシンは売り切れです。"
        elif self.state == self.SOLD:
            return "お待ちください。すでにガムボールを出しています。"

    def eject_quarter(self):
        if self.state == self.HAS_QUATER:
            self.state = self.NO_QUARTER
            return "25セントを返却しました。"
        elif self.state == self.NO_QUARTER:
            return "25セントを投入していません。"
        elif self.state == self.SOLD_OUT:
            return "返金できません。まだ25セントを投入していません。"
        elif self.state == self.SOLD:
            return "申し訳ありません。すでにクランクを回しています。"

    def turn_crank(self):
        if self.state == self.HAS_QUATER:
            self.state = self.SOLD
            return "クランクを回しました。"
        elif self.state == self.NO_QUARTER:
            return "クランクを回しましたが、25セントを投入していません。"
        elif self.state == self.SOLD_OUT:
            return "クランクを回しましたが、ガムボールがありません。"
        elif self.state == self.SOLD:
            return "2回回してもガムボールをもう1つ手に入れることはできません。"

    def dispense(self):
        if self.state == self.HAS_QUATER:
            return "販売するガムボールはありません。"
        elif self.state == self.NO_QUARTER:
            return "まず支払いをする必要があります。"
        elif self.state == self.SOLD_OUT:
            return "販売するガムボールはありません。"
        elif self.state == self.SOLD:
            self.count -= 1
            if self.count == 0:
                self.state = self.SOLD_OUT
            else:
                self.state = self.NO_QUARTER

            return "ガムボールがスロットから転がりでてきます。"
