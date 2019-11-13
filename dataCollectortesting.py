import json, unittest, main

test_values = '{ "location": 1, "depth" : 0, "temperature" : 15, "pH" : 1, "turbidity": 300}'
collected_values = json.loads(test_values)

class AcceptedRangeTest(unittest.TestCase):
    def test_Temperature_Range_High(self):
        self.assertTrue(collected_values["temperature"] < 150)

    def test_Temperature_Range_Low(self):
        self.assertTrue(collected_values["temperature"] > -50)

    def test_pH_Range_High(self):
         self.assertTrue(collected_values["pH"] <=14, msg= '{0}')

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

class TestOther(unittest.TestCase):
    def test_location(self):
        location_array = main.query("SELECT * FROM locations")
        self.assertTrue(1 <= collected_values["location"] <= len(location_array))

    # can we make this testing dynamic?
    def test_depth(self):
        depths = [0, 0.25, 0.50, 0.75]
        self.assertTrue(collected_values["depth"] in depths)


if __name__ == '__main__':
    unittest.main()
