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

def ping(s, port, data):
    server_address = ('localhost', port)
    try:
        s.sendto(data.encode('utf-8'), server_address)
    except socket.error as e:
        counter = 0
        while counter < 2:
            try:
                s.sendto(data.encode('utf-8'), server_address)
            except:
                counter += 1
        print("Connection with {} failed after 3 attempts".format(port))
        print(e)
                

if __name__ == "__main__":
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        listening_on = ('localhost', 200)
        s.bind(listening_on)
    except socket.error as e:
        print(e)
        s.shutdown(1)
    
    depths = [0.0, 0.25, 0.50, 0.75]
    depth = 0
    
    while True:
        for i in depths:
            depth = str(i)
            
            # Ping the Arduino to set the depth and wait for an acknowledgement
            print("Pinging arduino with depth")
            ping(s, 100, depth)
            acknowledge_depth, address = s.recvfrom(100)
            print(acknowledge_depth)

            # Ping the Arduino to collect the values from the sensors, and send them to the data store
            print("Pinging arduino for values")
            ping(s, 100, 'collect')
            collected_values, address= s.recvfrom(100)
            print(str(collected_values))
            
            print("storing values")
            ping(s, 300, collected_values.decode('utf-8'))
            acknowledge_store, address= s.recvfrom(100)
            print(acknowledge_store)


            time.sleep(10)

    s.shutdown(1)

