from abc import ABC
from tires.tires import Tires


class CarriganTires(Tires, ABC):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        for tire in self.wear:
            if tire >= 0.9:
                return 1
        return 0
