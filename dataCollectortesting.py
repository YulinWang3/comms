import json
import unittest
import sqlite3
from flask_restful import Resource
from main import wyw_select_locations
import main
import requests

test_values = '{ "location": 0, "depth" : 4, "temperature" : 15, "pH" : 1, "turbidity": 300}'
collected_values = json.loads(test_values)

class AcceptedRangeTest(unittest.TestCase):
    def test_Temperature_Range_High(self):
        self.assertTrue(collected_values["temperature"] < 150)

    def test_Temperature_Range_Low(self):
        self.assertTrue(collected_values["temperature"] > -50)

    def test_pH_Range_High(self):
         self.assertTrue(collected_values["pH"] <=14)

    def test_pH_Range_Low(self):
        self.assertTrue(collected_values["pH"] >= 0)

    def test_Turbidity_Range_High(self):
        self.assertTrue(collected_values["turbidity"] <= 3000)

    def test_Turbidity_Range_Low(self):
        self.assertTrue(collected_values["turbidity"] >= 0)

'''
Is there a way to comment on data if the temperature range is out of bounds 
to note that this data is collected outside of the accepted range of '''
class TemperatureRangeTest(unittest.TestCase):
    def test_Temperature_High(self):
        self.assertTrue(collected_values["temperature"] <= 125)

    def test_Temperature_Low(self):
        self.assertTrue(collected_values["temperature"] >= -50)

    def test_pH_Temperature_High(self):
        self.assertTrue(collected_values["temperature"] <= 50)

    def test_pH_Temperature_Low(self):
        self.assertTrue(collected_values["temperature"] >= -10)

    def test_Turbidity_Temperature_High(self):
        self.assertTrue(collected_values["temperature"] <= 90)

    def test_Turbidity_Temperature_Low(self):
        self.assertTrue(collected_values["temperature"] >= 5)


'''
# Location test takes the database values and compares them to the running value
class TestOther(unittest.TestCase):
    def test_Location(self):
'''

if __name__ == '__main__':
    unittest.main()
