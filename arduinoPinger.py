# SYSC 3010 F 2019

# Arduino Pinger
# - sends on 10.0.0.1:100
# - receives on 10.0.0.1:200

# Data Collector
# - sends on 10.0.0.1:300
# - receives on 10.0.0.1:400

# Data Store
# - sends on 10.0.0.1:500
# - receives on 10.0.0.1:600

import socket, sys, time

def ping_arduino(s, port):
	server_address = ('10.0.0.1', port)
	data = 'test'
	s.sendto(data.encode('utf-8'), server_address)

def receive_arduino(s, port):
	server_address = ('10.0.0.1', port)
	s.bind(server_address)
	buf, address = s.recvfrom(port)
	return buf

def ping_data_store(s, port, collected_values):
	server_address = ('10.0.0.1', port)
	s.sendto(collected_values.encode('utf-8'), server_address)

def receive_data_store(s, port):
	print('nice')

if __name__ == "__main__":
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	while True:
		print("PINGING ARDUINO")
		ping_arduino(s, 100)
		collected_values = receive_arduino(s, 200)
		print("RECEIVED FROM ARDUINO, PINGING DATA_STORE")
		ping_data_store(s, 300, collected_values)
		receive_data_store()
		print("RECEIVED FROM DATA_STORE")
		time.sleep(10)

	s.shutdown(1)

