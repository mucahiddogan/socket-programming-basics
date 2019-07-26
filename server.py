import socket 
from _thread import *
import threading 
import sys
from datetime import datetime

#print_lock = threading.Lock() 

host = ''
port = 1905

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host, port))
print("socket binded to post", port) 
s.listen(5) 
print("socket is listening") 


def threaded(c,addr): 
    first = "Welcome to my server bro!\n"
    c.send(first.encode('ascii'))
    goruldu = "goruldu\n"
    
    while True: 
        data = c.recv(1024) 
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S %d/%m/%Y")
        reply = "from: " +addr[0] + "\n" + "message: " + data.decode('ascii') + "time: " + dt_string + "\n\n"
        if not data: 
            print('Bye') 
            #print_lock.release() 
            break;
        print(reply)
        dosya = open("logfile","a")
        dosya.write(reply)
        dosya.close()
        c.send(goruldu.encode('ascii'))
    c.close() 
  
while 1: 
    c, addr = s.accept() 
    #print_lock.acquire(blocking=False)
    print('Connected to :',addr[0],':',addr[1])
    #start_new_thread(threaded, (c,))

    processThread = threading.Thread(target=threaded, args=[c,addr])
    processThread.start()
    if not addr:
        print("no connection")
        break
s.close() 
  

if __name__ == '__main__': 
    Main() 
