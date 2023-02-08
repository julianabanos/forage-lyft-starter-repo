import unittest

from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        current_mileage = 100000
        last_service_mileage = 35000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())


    def test_engine_doesnt_need_service(self):
        current_mileage = 50000
        last_service_mileage = 45000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())