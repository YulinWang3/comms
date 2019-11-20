
import socket

def ping(sender, data, receiver):
	sender.sendto(str(data).encode("utf-8"), receiver)

def receive(sender, receiver):
	data, address = receiver.recvfrom(sender)
	data = data.decode("utf-8")
	
	result = ''

	if data == '0.10' or data == 'XYZ':
		# test_arduinoPingerDepthFail
		result = 'F'

	elif data == 'collect':
		# test_dataCollectorAcknowledgeFail
		result = 'ACC'
		
	else:
		# test_arduinoPingerCollectFail
		result = 'T'

	return result

if __name__ == '__main__':
	port_master = 100 
	addres_master = ('localhost', 100)
	address_helper = ('localhost', 200)
	socket_helper = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	socket_helper.bind(address_helper)
	
	while True:
		try:
			data = receive(100, socket_helper)
			ping(socket_helper, data, addres_master)
		except KeyboardInterrupt:
			exit()
