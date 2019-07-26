import argparse
from pyModbusTCP.server import ModbusServer, DataBank
import socket
import sys
import time
import threading
from threading import Thread, Lock


if __name__ == '__main__':
    # parse args
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', type=str, default='host_ip', help='Host')
    #ifconfig | grep inet | head -1 | awk '{print $2}'
    parser.add_argument('-p', '--port', type=int, default=502, help='TCP port')
    args = parser.parse_args()
    # start modbus server
    server = ModbusServer(host=args.host, port=args.port)


def threadFunc(self): 
    while 1:
        bits=DataBank.get_bits(0,5)
        print(bits)
        #words = DataBank.get_words(0,4)
        #print(words)
        time.sleep(0.2)
i=1
thread1 = Thread(target=threadFunc, args=[i,])
thread1.start()
while 1:
    server.start()
    break



    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # s.bind((host, port))
    # print("socket binded to post", port) 
    # s.listen(5) 
    # print("socket is listening") 

