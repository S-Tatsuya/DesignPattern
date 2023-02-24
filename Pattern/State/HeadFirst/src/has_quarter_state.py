import random
from src.state import IState


class HasQuarterState(IState):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        return "もう一度25セントを投入することはできません。"

    def eject_quarter(self):
        self.gumball_machine.state = self.gumball_machine.no_quarter_state
        return "25セントを返却しました。"

    def turn_crank(self, _):
        random.seed(_)
        result = random.randint(0, 10)
        if result == 0 and self.gumball_machine.count > 1:
            self.gumball_machine.state = self.gumball_machine.winner_state
        else:
            self.gumball_machine.state = self.gumball_machine.sold_state
        return "クランクを回しました。"

    def dispense(self):
        return "販売するガムボールはありません。"
