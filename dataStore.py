import socket, sys, time

def receive_from_arduino_pinger(s, port):
        buf, address = s.recvfrom(port)
        # do stuff
        # return stuff
        return buf

def send_to_arduino_pinger(s, port, collected_values):
        s.sendto(collected_values.encode('utf-8'), ('localhost', 200))

if __name__ == "__main__":
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        listening_on = ('localhost', 300)
        s.bind(listening_on)

        while True:
                collected_values = receive_from_arduino_pinger(s, 100)
                send_to_arduino_pinger(s, 200, collected_values)

