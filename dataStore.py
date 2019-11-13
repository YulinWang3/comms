# SYSC 3010 F 2019

# Arduino Pinger
# - sends to 10.0.0.1:100 (data collector)
# - receives on 10.0.0.1:200 (self)
# - sends to 10.0.0.1:300 (data store)

# Data Collector
# - receives on 10.0.0.1:100 (self)
# - sends to 10.0.0.1:200 (arduino pinger)

# Data Store
# - receives on 10.0.0.1:300 (self)
# - sends to 10.0.0.1:200 (arduino pinger)

import socket, sys, time, json, sqlite3
from arduinoPinger import ping

def receive_from_arduino_pinger(s, port):
        buf, address = s.recvfrom(port)
        print(str(buf)+"\n")
        results = json.loads(buf)
        a = results['location']
        b = results['depth']
        c = results['temperature']
        d = results['ph']
        e = results['turbidity']

        db = sqlite3.connect('./location.db')
        cursor = db.cursor()
        sqlite3_query = "INSERT INTO 'location_values' ('location_id', 'tdate', 'ttime', 'tph', 'ttemperature', 'tturbidity', 'tdepth') VALUES ({}, date('now'), time('now'), {}, {}, {}, {});".format(a, b, c, d, e)
        cursor.execute(sqlite3_query)
        db.commit()

def send_to_arduino_pinger(s, port, collected_values):
        s.sendto('nice'.encode('utf-8'), ('localhost', 200))

if __name__ == "__main__":
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        listening_on = ('localhost', 300)
        s.bind(listening_on)

        while True:
                print("Waiting for message from arduino_pinger")
                collected_values = receive_from_arduino_pinger(s, 100)
                ping(s, 200, collected_values.decode('utf-8'))

