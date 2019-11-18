import json, unittest, main

#Temp values
test_values = '{ "location": 1, "depth" : 0, "temperature" : 15, "pH" : 1, "turbidity": 300}'
collected_values = json.loads(test_values)

class AcceptedRangeTest(unittest.TestCase):
    # Testing upper bound of the temperature sensor's range
    def test_Temperature_Range_High(self):
        self.assertTrue(collected_values["temperature"] < 150)

    # Testing lower bound of the temperature sensor's range
    def test_Temperature_Range_Low(self):
        self.assertTrue(collected_values["temperature"] > -50)

    # Testing upper bound of the pH sensor's range
    def test_pH_Range_High(self):
         self.assertTrue(collected_values["pH"] <=14)

    # Testing lower bound of the pH sensor's range
    def test_pH_Range_Low(self):
        self.assertTrue(collected_values["pH"] >= 0)

    # Testing upper bound of the turbidity sensor's range
    def test_Turbidity_Range_High(self):
        self.assertTrue(collected_values["turbidity"] <= 3000)

    # Testing lower bound of the turbidity sensor's range
    def test_Turbidity_Range_Low(self):
        self.assertTrue(collected_values["turbidity"] >= 0)


class TemperatureRangeTest(unittest.TestCase):
    # Testing upper bound of turbidity sensor temperature accuracy
    def test_Temperature_High(self):
        self.assertTrue(collected_values["temperature"] <= 125)

    # Testing lower bound of temperature sensor temperature accuracy
    def test_Temperature_Low(self):
        self.assertTrue(collected_values["temperature"] >= -50)

    # Testing lower bound of pH sensor temperature accuracy
    def test_pH_Temperature_High(self):
        self.assertTrue(collected_values["temperature"] <= 50)

    # Testing lower bound of pH sensor temperature accuracy
    def test_pH_Temperature_Low(self):
        self.assertTrue(collected_values["temperature"] >= -10)

    # Testing upper bound of turbidity sensor temperature accuracy
    def test_Turbidity_Temperature_High(self):
        self.assertTrue(collected_values["temperature"] <= 90)

    # Testing lower bound of turbidity sensor temperature accuracy
    def test_Turbidity_Temperature_Low(self):
        self.assertTrue(collected_values["temperature"] >= 5)

class TestOther(unittest.TestCase):
    # Gets all location values from database and checks if in range
    def test_location(self):
        location_array = main.query("SELECT * FROM locations")
        self.assertTrue(1<= collected_values["location"] <= len(location_array))

    # Checks if depth is a specific value(s)
    def test_depth(self):
        depths = [0, 0.25, 0.50, 0.75]
        self.assertTrue(collected_values["depth"] in depths)


if __name__ == '__main__':
    unittest.main();
