'''
Test #1 Determine Data Store successfully receives JSON
Test #2 Determine Data Store ACK failed received JSON
Test #3 Boolean JSON Location fail
Test #4 Boolean JSON depth fail
Test #5 Boolean JSON temperature fail
Test temperature out of accepted range (-80 -> 150C)
Test# temperature out of probe range (-55C -> 125 C)
Test #6 Boolean JSON ph fail
Test# pH out of accepted range (0 -> 14)
Test ph sensor temperature out of probe range (-10 C -> 50 C)
Test #7 Boolean JSON turbidity
Test turbidity probe temperature out of range (5C -> 90C)
Test Turbidity probe for accepted values (0-3000 NTU)
'''

'''
INSERT DEPTH AND TERMPERATURE ARRAY INTO JSON
'''

from dataStore import receive_from_arduino_pinger
from arduinoPinger import ping_data_store

import socket, json, unittest

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Inputting false data:
test_values = '{ "location": 0, "depth" : 4, "temperature" : 15, "pH" : 1, "turbidity": 300}'

collected_values = json.loads(test_values)
print(test_values)
print(collected_values)
'''
str(collected_values).encode('utf-8')
port = 100
ping_data_store(s, 100, collected_values)
receive_from_arduino_pinger(s, 100)
'''

'''
    Automated Testing Sequence
Reads from a file with automatic errors. Checks the system line by line.
'''

fileRead = open("ErrorTesting.txt", "r")
if fileRead.mode == 'r':
    print(fileRead.readlines())

'''
Test JSON
Confirm that data that has been transfered has not corrupted
'''


class JsonTest(unittest.TestCase):
    def test_location(self):
        self.assertEqual(collected_values["location"], 1)

    def test_1(self):
        self.assertEqual(collected_values["depth"], 0)


class AcceptableRangeTest(unittest.TestCase):
    def test_temperature(self):
        self.assertTrue(5 <= collected_values["temperature"] <= 50)

    def test_pH(self):
        self.assertTrue(0 <= collected_values["pH"] <= 14)

    def test_turbidity(self):
        self.assertTrue(0 <= collected_values["turbidity"] <= 3000)


class TemperatureRangeTest(unittest.TestCase):
    def test_temperature(self):
        self.assertTrue(-50 <= collected_values["temperature"] <= 125)

    def test_pH(self):
        self.assertTrue(-10 <= collected_values["temperature"] <= 50)

    def test_turbidity(self):
        self.assertTrue(5 <= collected_values["temperature"] <= 90)


if __name__ == '__main__':
    unittest.main()
