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

import socket, sys, time, random, json, serial  

ser = serial.Serial('/dev/tty/ACM0', 9600)

def receive_from_arduino_pinger(s, port):
    buf, address = s.recvfrom(port)
    print(buf.decode('utf-8'))
    
    if buf in [0.0, 0.25, 0.50, 0.75]:
        
        # using serial, send a message to arduino
        ser.write(buf)
        
        return "ACK"
    
    else:
        # write to arduino to start collecting the data
        ser.write(b'1')  
        
        time.sleep(6)
        
        # using serial, read from the serial port
        while 1:
            if (ser.in_waiting > 0):
                line = ser.readline()
            
        # fake_data = json.dumps(fakeTheData())
        return fake_data


def send_to_arduino_pinger(s, port, collected_values):
    s.sendto(collected_values.encode('utf-8'), ('localhost', 200)) 


def fakeTheData():
    return {
        "location": random.choice([1, 2, 3]),
        "depth": random.choice([0, 25, 50, 75, 100]),
        "temperature": random.randint(15, 20),
        "ph": random.randint(0, 14),
        "turbidity": random.randint(0, 3000),
        }


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listening_on = ('localhost', 100)
    s.bind(listening_on)

    while True:
        print("Waiting for value from arduino_pinger")
        collected_values = receive_from_arduino_pinger(s, 100)
        print("got "+collected_values+"\n")
        send_to_arduino_pinger(s, 200, collected_values)
