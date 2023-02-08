from abc import ABC
from tires.tires import Tires


class OctoprimeTires(Tires, ABC):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        if sum(self.wear) >= 3.0:
            return 1
        return 0
