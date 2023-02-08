import unittest
from datetime import date, datetime

from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())



    def test_battery_doesnt_need_service(self):
        current_date = date.fromisoformat("2023-02-08")
        last_service_date = date.fromisoformat("2022-01-10")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())