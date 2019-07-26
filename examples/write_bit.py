from pyModbusTCP.client import ModbusClient
import time
import socket
from Tkinter import *
import Tkinter as tk

SERVER_HOST = "host_ip"
#ifconfig | grep inet | head -1 | awk '{print $2}'
SERVER_PORT = 502

c = ModbusClient()

# uncomment this line to see debug message
#c.debug(True)

c.host(SERVER_HOST)
c.port(SERVER_PORT)

while True:
    if not c.is_open():
        if not c.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))
    if c.is_open():
        for addr in range(1):
            def toggle(tog=[0]):
                tog[0] = not tog[0]
                if tog[0]:
                    t_btn.config(text='False')
                    is_ok = c.write_single_coil(addr, tog[0])
                    #print("bit #" + str(addr) + ": write to " + str(tog[0]))
                    print(tog[0])
                else:
                    t_btn.config(text='True')
                    is_ok = c.write_single_coil(addr, tog[0])
                    #print("bit #" + str(addr) + ": write to " + str(tog[0]))
                    print(tog[0])
                time.sleep(0.2)
            root = tk.Tk()
            root.title("Led Yakilir USTA 44")
            root.configure(background="black")
            root.geometry('300x300')
            t_btn = tk.Button(text="True", width=12, command=toggle)
            t_btn.pack(pady=5)
            root.mainloop()         

            # if is_ok:
            # else:
            #     print("bit #" + str(addr) + ": unable to write " + str(toggle))
            # # #time.sleep(0.5)

        time.sleep(0.5)


