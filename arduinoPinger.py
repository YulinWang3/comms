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

import socket, sys, time

def ping_arduino(s, port):
	server_address = ('localhost', port)
	data = 'test'
	s.sendto(data.encode('utf-8'), server_address)

def ping_data_store(s, port, collected_values):
	server_address = ('localhost', port)
	s.sendto(collected_values.encode('utf-8'), server_address)


if __name__ == "__main__":
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	listening_on = ('localhost', 200)
	s.bind(listening_on)

	while True:
		print("PINGING ARDUINO")
		ping_arduino(s, 100)
		collected_values = s.recvfrom(100)
		print("RECEIVED FROM ARDUINO, PINGING DATA_STORE")
		ping_data_store(s, 300, collected_values)
		ack_store = s.recvfrom(300)
		print(ack_store)
		print("RECEIVED FROM DATA_STORE")
		time.sleep(10)

	s.shutdown(1)

