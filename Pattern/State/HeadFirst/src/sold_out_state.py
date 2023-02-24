from src.state import IState


class SoldOutState(IState):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        return "25セントを投入することはできません。このマシンは売り切れです。"

    def eject_quarter(self):
        return "返金できません。まだ25セントを投入していません。"

    def turn_crank(self):
        return "クランクを回しましたが、ガムボールがありません。"

    def dispense(self):
        return "販売するガムボールはありません。"
