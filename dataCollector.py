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

import socket, sys, time, random, json

def receive_from_arduino_pinger(s, port):
	buf, address = s.recvfrom(port)
	fake_data = json.dumps(fakeTheData())
	return fake_data

def send_to_arduino_pinger(s, port, collected_values):
	s.sendto(collected_values.encode('utf-8'), ('localhost', 200))

def fakeTheData():
	a = random.choice([1, 2, 3])
	b = random.choice([0, 25, 50, 75, 100])
	c = random.randint(15, 20)
	d = random.randint(0, 14)
	e = random.randint(0, 3000)

	return {
		"location": a,
		"depth": b,
		"temperature": c,
		"ph": d,
		"turbidity": e,
		}

if __name__ == "__main__":
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	listening_on = ('localhost', 100)
	s.bind(listening_on)

	while True:
		print("[DATA_COLLECTOR] waiting for message from arduino_pinger")
		collected_values = receive_from_arduino_pinger(s, 100)
		print(collected_values)
		send_to_arduino_pinger(s, 200, collected_values)
