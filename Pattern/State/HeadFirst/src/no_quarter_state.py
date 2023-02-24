from src.state import IState


class NoQuarterState(IState):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        self.gumball_machine.state = self.gumball_machine.has_quarter_state
        return "25セントを投入しました。"

    def eject_quarter(self):
        return "25セントを投入していません。"

    def turn_crank(self):
        return "クランクを回しましたが、25セントを投入していません。"

    def dispense(self):
        return "まず支払いをする必要があります。"
