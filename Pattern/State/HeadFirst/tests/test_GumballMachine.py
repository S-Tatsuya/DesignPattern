from src.GumballMachine import GumballMachine
from src.no_quarter_state import NoQuarterState
from src.has_quarter_state import HasQuarterState
from src.sold_out_state import SoldOutState
from src.sold_state import SoldState
from src.winner_state import WinnerState


class TestNoQuarterState:
    def test_insert_quater(self):
        gumball_machine = GumballMachine(1)
        sut = NoQuarterState(gumball_machine)

        assert sut.insert_quarter() == "25セントを投入しました。"
        assert gumball_machine.state == gumball_machine.has_quarter_state

    def test_eject_quater(self):
        gumball_machine = GumballMachine(1)
        expect_state = gumball_machine.state
        sut = NoQuarterState(gumball_machine)

        assert sut.eject_quarter() == "25セントを投入していません。"
        assert gumball_machine.state == expect_state

    def test_turn_crank(self):
        gumball_machine = GumballMachine(1)
        expect_state = gumball_machine.state
        sut = NoQuarterState(gumball_machine)

        assert sut.turn_crank() == "クランクを回しましたが、25セントを投入していません。"
        assert gumball_machine.state == expect_state

    def test_dispense(self):
        gumball_machine = GumballMachine(1)
        expect_state = gumball_machine.state
        sut = NoQuarterState(gumball_machine)

        assert sut.dispense() == "まず支払いをする必要があります。"
        assert gumball_machine.state == expect_state


class TestHasQuarterState:
    def test_insert_quater(self):
        gumball_machine = GumballMachine(1)
        expect_state = gumball_machine.state
        sut = HasQuarterState(gumball_machine)

        assert sut.insert_quarter() == "もう一度25セントを投入することはできません。"
        assert gumball_machine.state == expect_state

    def test_eject_quarter(self):
        gumball_machine = GumballMachine(1)
        sut = HasQuarterState(gumball_machine)

        assert sut.eject_quarter() == "25セントを返却しました。"
        assert gumball_machine.state == gumball_machine.no_quarter_state

    def test_turn_crank_to_sold_state_if_count1(self):
        gumball_machine = GumballMachine(1)
        sut = HasQuarterState(gumball_machine)

        assert sut.turn_crank(2) == "クランクを回しました。"
        assert gumball_machine.state == gumball_machine.sold_state

    def test_turn_crank_to_sold_state_if_count_false(self):
        gumball_machine = GumballMachine(2)
        sut = HasQuarterState(gumball_machine)

        assert sut.turn_crank(0) == "クランクを回しました。"
        assert gumball_machine.state == gumball_machine.sold_state

    def test_turn_crank_to_winner_state(self):
        gumball_machine = GumballMachine(2)
        sut = HasQuarterState(gumball_machine)

        assert sut.turn_crank(2) == "クランクを回しました。"
        assert gumball_machine.state == gumball_machine.winner_state

    def test_dispense(self):
        gumball_machine = GumballMachine(1)
        expect_state = gumball_machine.state
        sut = HasQuarterState(gumball_machine)

        assert sut.dispense() == "販売するガムボールはありません。"
        assert gumball_machine.state == expect_state


class TestSoldOutState:
    def test_insert_quater(self):
        gumball_machine = GumballMachine(0)
        expect_state = gumball_machine.state
        sut = SoldOutState(gumball_machine)

        assert sut.insert_quarter() == "25セントを投入することはできません。このマシンは売り切れです。"
        assert gumball_machine.state == expect_state

    def test_eject_quater_(self):
        gumball_machine = GumballMachine(0)
        expect_state = gumball_machine.state
        sut = SoldOutState(gumball_machine)

        assert sut.eject_quarter() == "返金できません。まだ25セントを投入していません。"
        assert gumball_machine.state == expect_state

    def test_turn_crank_of_sold_out(self):
        gumball_machine = GumballMachine(0)
        expect_state = gumball_machine.state
        sut = SoldOutState(gumball_machine)

        assert sut.turn_crank() == "クランクを回しましたが、ガムボールがありません。"
        assert gumball_machine.state == expect_state

    def test_dispense_of_sold_out(self):
        gumball_machine = GumballMachine(0)
        expect_state = gumball_machine.state
        sut = SoldOutState(gumball_machine)

        assert sut.dispense() == "販売するガムボールはありません。"
        assert gumball_machine.state == expect_state


class TestSoldState:
    def test_insert_quater(self):
        gumball_machine = GumballMachine(1)
        expect_state = gumball_machine.state
        sut = SoldState(gumball_machine)

        assert sut.insert_quarter() == "お待ちください。すでにガムボールを出しています。"
        assert gumball_machine.state == expect_state

    def test_eject_quater(self):
        gumball_machine = GumballMachine(1)
        expect_state = gumball_machine.state
        sut = SoldState(gumball_machine)

        assert sut.eject_quarter() == "申し訳ありません。すでにクランクを回しています。"
        assert gumball_machine.state == expect_state

    def test_turn_crank(self):
        gumball_machine = GumballMachine(1)
        expect_state = gumball_machine.state
        sut = SoldState(gumball_machine)

        assert sut.turn_crank() == "2回回してもガムボールをもう1つ手に入れることはできません。"
        assert gumball_machine.state == expect_state

    def test_dispense(self):
        gumball_machine = GumballMachine(1)
        sut = SoldState(gumball_machine)

        assert sut.dispense() == "ガムボールがスロットから転がりでてきます。\nおっと、ガムボールがなくなりました！"
        assert gumball_machine.state == gumball_machine.sold_out_state

        gumball_machine = GumballMachine(2)
        sut = SoldState(gumball_machine)

        assert sut.dispense() == "ガムボールがスロットから転がりでてきます。"
        assert gumball_machine.state == gumball_machine.no_quarter_state


class TestWinnerState:
    def test_insert_quater(self):
        gumball_machine = GumballMachine(1)
        expect_state = gumball_machine.state
        sut = WinnerState(gumball_machine)

        assert sut.insert_quarter() == "抽選結果が出ました。もう少しお待ち下さい。"
        assert gumball_machine.state == expect_state

    def test_eject_quater(self):
        gumball_machine = GumballMachine(1)
        expect_state = gumball_machine.state
        sut = WinnerState(gumball_machine)

        assert sut.eject_quarter() == "抽選結果が出ました。もう少しお待ち下さい。"
        assert gumball_machine.state == expect_state

    def test_turn_crank(self):
        gumball_machine = GumballMachine(1)
        expect_state = gumball_machine.state
        sut = WinnerState(gumball_machine)

        assert sut.turn_crank() == "抽選結果が出ました。もう少しお待ち下さい。"
        assert gumball_machine.state == expect_state

    def test_dispense(self):
        gumball_machine = GumballMachine(2)
        sut = WinnerState(gumball_machine)

        assert sut.dispense() == (
            "ガムボールがスロットから転がりでてきます。\nガムボールがスロットから転がりでてきます。\nおっと、ガムボールがなくなりました！"
        )

        assert gumball_machine.state == gumball_machine.sold_out_state

        gumball_machine = GumballMachine(3)
        sut = WinnerState(gumball_machine)

        assert sut.dispense() == "ガムボールがスロットから転がりでてきます。\nガムボールがスロットから転がりでてきます。"
        assert gumball_machine.state == gumball_machine.no_quarter_state


class TestGumbalMachine:
    def test_gumball_machine_state(self):
        sut = GumballMachine(3)

        assert sut.insert_quarter() == "25セントを投入しました。"
        assert sut.state == sut.has_quarter_state

        assert sut.turn_crank(0) == "クランクを回しました。"

        assert sut.dispense() == "ガムボールがスロットから転がりでてきます。"
        assert sut.state == sut.no_quarter_state

        assert sut.insert_quarter() == "25セントを投入しました。"
        assert sut.state == sut.has_quarter_state

        assert sut.turn_crank(2) == "クランクを回しました。"
        assert sut.state == sut.winner_state

        assert sut.dispense() == (
            "ガムボールがスロットから転がりでてきます。\nガムボールがスロットから転がりでてきます。\nおっと、ガムボールがなくなりました！"
        )
        assert sut.state == sut.sold_out_state
