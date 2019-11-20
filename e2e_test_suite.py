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

def ping(sender, data, receiver):
	sender.sendto(str(data).encode("utf-8"), receiver)

def receive(sender, receiver):
	data, address = receiver.recvfrom(sender)
	data = data.decode("utf-8")
	return data

def test_arduinoPingerDepthFail():
	data = '0.10'
    ping(socket_ap, data, receiver)
    result, address = s.recvfrom(100)
    result = result.decode("utf-8")

    assert result == 'F'

def test_arduinoPingerCollectFail():
	data = '0.0'
    ping(socket_ap, data, receiver)
    result, address = s.recvfrom(100)
    result = result.decode("utf-8")

    data = 'XYZ'
    ping(socket_ap, data, receiver)
    result, address = s.recvfrom(100)
    result = result.decode("utf-8")

    assert result == 'F'


def test_dataCollectorAcknowledgeFail():

    data = 'collect'
    ping(socket_ap, data, receiver)
    result, address = s.recvfrom(100)
    result = result.decode("utf-8")

    assert result == 'ACC'

def test_dataStoreFail():

if __name__ == "__main__":
	port_master = 100 
	port_helper = 200
	addres_master = ('localhost', 100)
	address_helper = ('localhost', 200)
	socket_master = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	socket_master.bind(addres_master)


