from src.framework.Manager import Manager
from src.framework.Product import Product
from src.MessageBox import MessageBox
from src.UnderlinePen import UnderlinePen


def test_prototype():
    manager: Manager = Manager()
    upen = UnderlinePen("~")
    mbox = MessageBox("*")
    sbox = MessageBox("/")

    manager.register("strong message", upen)
    manager.register("warning box", mbox)
    manager.register("slash box", sbox)

    p1: Product = manager.create("strong message")
    p2: Product = manager.create("warning box")
    p3: Product = manager.create("slash box")
    p1.use("Hello, world")
    p2.use("Hello, world")
    p3.use("Hello, world")

    assert True
