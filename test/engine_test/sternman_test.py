import unittest

from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        warning_light_is_on = 1
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())



    def test_engine_doesnt_need_service(self):
        warning_light_is_on = 0
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())