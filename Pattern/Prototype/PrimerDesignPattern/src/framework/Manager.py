from src.framework.Product import Product
from typing import Dict


class Manager:
    def __init__(self):
        self._showcase: Dict[str, Product] = {}

    def register(self, name, proto: Product):
        self._showcase[name] = proto

    def create(self, protoname) -> Product:
        return self._showcase[protoname].createClone()
