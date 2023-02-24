from src.GumballMachine import GumballMachine


class TestGumbalMachine:
    def test_insert_quater_of_has_quater(self):
        sut = GumballMachine(1)
        sut.insert_quarter()

        assert sut.insert_quarter() == "もう一度25セントを投入することはできません。"
        assert sut.state == sut.has_quarter_state

    def test_insert_quater_of_no_quater(self):
        sut = GumballMachine(1)

        assert sut.insert_quarter() == "25セントを投入しました。"
        assert sut.state == sut.has_quarter_state

    def test_insert_quater_of_sold_out(self):
        sut = GumballMachine(0)

        assert sut.insert_quarter() == "25セントを投入することはできません。このマシンは売り切れです。"
        assert sut.state == sut.sold_out_state

    def test_insert_quater_of_sold(self):
        sut = GumballMachine(1)
        sut.insert_quarter()
        sut.turn_crank()

        assert sut.insert_quarter() == "お待ちください。すでにガムボールを出しています。"
        assert sut.state == sut.sold_state

    def test_eject_quarter_of_has_quater(self):
        sut = GumballMachine(1)
        sut.insert_quarter()

        assert sut.eject_quarter() == "25セントを返却しました。"
        assert sut.state == sut.no_quarter_state

    def test_eject_quater_of_no_quater(self):
        sut = GumballMachine(1)

        assert sut.eject_quarter() == "25セントを投入していません。"
        assert sut.state == sut.no_quarter_state

    def test_eject_quater_of_sold_out(self):
        sut = GumballMachine(0)

        assert sut.eject_quarter() == "返金できません。まだ25セントを投入していません。"
        assert sut.state == sut.sold_out_state

    def test_eject_quater_of_sold(self):
        sut = GumballMachine(1)
        sut.insert_quarter()
        sut.turn_crank()

        assert sut.eject_quarter() == "申し訳ありません。すでにクランクを回しています。"
        assert sut.state == sut.sold_state

    def test_turn_crank_of_has_quater(self):
        sut = GumballMachine(1)
        sut.insert_quarter()

        assert sut.turn_crank() == "クランクを回しました。"
        assert sut.state == sut.sold_state

    def test_turn_crank_of_no_quater(self):
        sut = GumballMachine(1)

        assert sut.turn_crank() == "クランクを回しましたが、25セントを投入していません。"
        assert sut.state == sut.no_quarter_state

    def test_turn_crank_of_sold_out(self):
        sut = GumballMachine(0)

        assert sut.turn_crank() == "クランクを回しましたが、ガムボールがありません。"
        assert sut.state == sut.sold_out_state

    def test_turn_crank_of_sold(self):
        sut = GumballMachine(1)
        sut.insert_quarter()
        sut.turn_crank()

        assert sut.turn_crank() == "2回回してもガムボールをもう1つ手に入れることはできません。"
        assert sut.state == sut.sold_state

    def test_dispense_of_has_quater(self):
        sut = GumballMachine(1)
        sut.insert_quarter()

        assert sut.dispense() == "販売するガムボールはありません。"
        assert sut.state == sut.has_quarter_state

    def test_dispense_of_no_quater(self):
        sut = GumballMachine(1)

        assert sut.dispense() == "まず支払いをする必要があります。"
        assert sut.state == sut.no_quarter_state

    def test_dispense_of_sold_out(self):
        sut = GumballMachine(0)

        assert sut.dispense() == "販売するガムボールはありません。"
        assert sut.state == sut.sold_out_state

    def test_dispense_of_sold(self):
        sut = GumballMachine(1)
        sut.insert_quarter()
        sut.turn_crank()

        assert sut.dispense() == "ガムボールがスロットから転がりでてきます。\nおっと、ガムボールがなくなりました！"
        assert sut.state == sut.sold_out_state

        sut = GumballMachine(2)
        sut.insert_quarter()
        sut.turn_crank()

        assert sut.dispense() == "ガムボールがスロットから転がりでてきます。"
        assert sut.state == sut.no_quarter_state
