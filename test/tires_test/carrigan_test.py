import unittest

from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_tires_need_service(self):
        wear = [0.2, 1, 1, 1]
        tires = CarriganTires(wear)
        self.assertTrue(tires.needs_service())


    def test_tires_dont_need_service(self):
        wear = [0, 0.8, 0.5, 0.3]
        tires = CarriganTires(wear)
        self.assertFalse(tires.needs_service())