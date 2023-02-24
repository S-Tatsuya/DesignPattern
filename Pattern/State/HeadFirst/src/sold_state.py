from src.state import IState


class SoldState(IState):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        return "お待ちください。すでにガムボールを出しています。"

    def eject_quarter(self):
        return "申し訳ありません。すでにクランクを回しています。"

    def turn_crank(self):
        return "2回回してもガムボールをもう1つ手に入れることはできません。"

    def dispense(self):
        self.gumball_machine.count -= 1
        if self.gumball_machine.count == 0:
            self.gumball_machine.state = self.gumball_machine.sold_out_state
        else:
            self.gumball_machine.state = self.gumball_machine.no_quarter_state

        return "ガムボールがスロットから転がりでてきます。"
