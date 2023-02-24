from src.state import IState
from src.no_quarter_state import NoQuarterState
from src.has_quarter_state import HasQuarterState
from src.sold_out_state import SoldOutState
from src.sold_state import SoldState


class GumballMachine:
    def __init__(self, count):
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_out_state = SoldOutState(self)
        self.sold_state = SoldState(self)
        self.count = count
        if count > 0:
            self.state: IState = self.no_quarter_state
        else:
            self.state: IState = self.sold_out_state

    def insert_quarter(self):
        return self.state.insert_quarter()

    def eject_quarter(self):
        return self.state.eject_quarter()

    def turn_crank(self):
        return self.state.turn_crank()

    def dispense(self):
        return self.state.dispense()

    def release_ball(self):
        return "ガムボールがスロットから転がりでてきます。"
