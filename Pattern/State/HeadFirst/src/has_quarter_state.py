from src.state import IState


class HasQuarterState(IState):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        return "もう一度25セントを投入することはできません。"

    def eject_quarter(self):
        self.gumball_machine.state = self.gumball_machine.no_quarter_state
        return "25セントを返却しました。"

    def turn_crank(self):
        self.gumball_machine.state = self.gumball_machine.sold_state
        return "クランクを回しました。"

    def dispense(self):
        return "販売するガムボールはありません。"
