import socket 
  
def Main(): 
    
    host = input("Set host address(ip address): ")
    port = int(input("Enter port number: "))

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.connect((host,port)) 

    while True: 
        data = s.recv(1024) 
        print('Received from the server :',str(data.decode('ascii'))) 
        message = input("Server'a Mesaj gönder(ASCII karakter): ")
        message = message + "\n"
        s.send(message.encode('ascii')) 
        ans = input('\nDo you want to continue(y/n) :') 
        if ans == 'y': 
            continue
        else: 
            break
    s.close() 
  
if __name__ == '__main__': 
    Main() 
