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

import socket, unittest

port_master = 100 
port_helper = 200
addres_master = ('localhost', 100)
address_helper = ('localhost', 200)
socket_master = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_master.bind(addres_master)

def ping(sender, data, receiver):
	sender.sendto(str(data).encode("utf-8"), receiver)

def receive(sender, receiver):
	data, address = receiver.recvfrom(sender)
	data = data.decode("utf-8")
	return data

class e2e(unittest.TestCase):

	def test_arduinoPingerDepthFail(self):
		data = '0.10'
		ping(socket_master, data, address_helper)
		result, address = socket_master.recvfrom(100)
		result = result.decode("utf-8")

		self.assertEqual(result,'F')

	def test_arduinoPingerCollectFail(self):
		data = '0.0'
		ping(socket_master, data, address_helper)
		result, address = socket_master.recvfrom(100)
		result = result.decode("utf-8")

		data = 'XYZ'
		ping(socket_master, data, address_helper)
		result, address = socket_master.recvfrom(100)
		result = result.decode("utf-8")

		self.assertEqual(result,'F')


	def test_dataCollectorAcknowledgeFail(self):

		data = 'collect'
		ping(socket_master, data, address_helper)
		result, address = socket_master.recvfrom(100)
		result = result.decode("utf-8")

		self.assertEqual(result,'ACC')

if __name__ == "__main__":
	unittest.main()
	

