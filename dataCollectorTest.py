import dataCollectortesting, json, unittest

# Open a premade text file to read from to automatically run tests
filepath = 'ErrorTesting.txt'
with open(filepath) as fp:
    # Read the first line
    line = fp.readline()
    while line:
        # Change the input value for different error cases
        dataCollectortesting.collected_values = json.loads(line)
        # Load tests from dataCollectesting.py
        suite = unittest.defaultTestLoader.loadTestsFromModule(dataCollectortesting)
        # Run tests
        test = unittest.TextTestRunner(verbosity=3).run(suite)
        # Read next line
        line = fp.readline()
