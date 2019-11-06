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

def ping_arduino(s, port, data):
    server_address = ('localhost', port)
    s.sendto(data.encode('utf-8'), server_address)

def ping_data_store(s, port, collected_values):
    server_address = ('localhost', port)
    s.sendto(collected_values, server_address)

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listening_on = ('localhost', 200)
    s.bind(listening_on)
    
    depths = [0.0, 0.25, 0.50, 0.75]
    depth = 0
    
    while True:
        for i in depths:
            depth = i
        
        # Ping the Arduino to set the depth and wait for an acknowledgement
        ping_arduino(s, 100, depth)
        acknowledge = s.recvfrom(100)
        
        # Ping the Arduino to collect the values from the sensors, and send them to the data store
        ping_arduino(s, 100, 'collect')
        collected_values, address= s.recvfrom(100)
        
        ping_data_store(s, 300, collected_values)

        time.sleep(10)

    s.shutdown(1)

