from src.state import IState


class WinnerState(IState):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        return "抽選結果が出ました。もう少しお待ち下さい。"

    def eject_quarter(self):
        return "抽選結果が出ました。もう少しお待ち下さい。"

    def turn_crank(self):
        return "抽選結果が出ました。もう少しお待ち下さい。"

    def dispense(self):
        result = self.gumball_machine.release_ball()
        self.gumball_machine.count -= 1
        result = result + "\n" + self.gumball_machine.release_ball()
        self.gumball_machine.count -= 1
        if self.gumball_machine.count == 0:
            self.gumball_machine.state = self.gumball_machine.sold_out_state
            return result + "\n" "おっと、ガムボールがなくなりました！"
        else:
            self.gumball_machine.state = self.gumball_machine.no_quarter_state
            return result
