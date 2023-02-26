import socket
import numpy as np
from trading_bot.Bot.pivot_break import pivotBreakStrategy # You should remove this line. Look at the line 50 or README.md

class socketserver:
    def __init__(self, address = '', port = ''):
        # Instanciating the socket server
        self.newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP
        # setting the object's essential properties
        self.address = address # e.g. 192.168.1.15
        self.port = port # e.g. 14201
        # Makes it possible to conncet to the new socket
        self.newSocket.bind((self.address, self.port))        
    
    def recvmsg(self):
        self.newSocket.listen(1) # 1 is the number of simultanous connections (the first one will be processed and the rest will be queued)
        
        # accept() accepts connections from outside:
        # conn is the clientsocket. It's a socket object.
        # addr is the ip and port for data transmission, e.g. ('192.168.1.15', 49396)
        self.conn, self.addr = self.newSocket.accept() # Stablishing the connection
        print('connected to ', self.addr)

        self.commdata = '' # For storing recieved data
        
        # Recieving data
        # The standard practise is to log the data in this loop if needed
        while True:
            # recv() recieves data in binary
            data = self.conn.recv(10000) # Data size in Bites (binary data)
            
            # Appending the recieved data to commdata
            self.commdata+=data.decode("utf-8") # Converting the data to UTF-8
            print(data) # Prints the recieved data
            
            if not data:
                print("No data recieved from the client") # This usually will be printed on clientsocket timeouts
                break # Breaks the while loop but the server will stay online

            # Sending the response to the client (in this case the MetaTrader Expert Advisor)
            # In this case we caculate a regressin on the recieved data and send the regression line position data
            # Data is converted from UTF-8 to binary using bytes()
            self.conn.send(bytes(calc(self.commdata), "utf-8")) # You can remove this line or modify the content if you don't need to send any data back to the client
            return self.commdata
        
    # Kills the socket server
    def __del__(self):
        self.newSocket.close()

# pivotBreakStrategy() is the calculation we needed to be performed and send its results back to the client.
# You can substitue this with any other calculation you desire.
# Examples are provided in the README.md
def calc(msg = ''):
    chartdata = np.fromstring(msg, dtype=float, sep= ' ') # Data is seperated by a white space (in client side's code).
    print(chartdata) # prints the clean data
    
    # The following line is the calculation. You should remove this line and write your own task.
    P = pivotBreakStrategy(chartdata)
    
    print(P) # prints the result
    return str(P) #return the results in order to be sent back to the client

# Creating a new sockek object with your ip and a port. It starts automatically.
# The same ip and port will be used on the client side
myServer = socketserver('192.168.1.15', 14201) # The TCP port is number between 0 and 65,535

print("Start Python server at",myServer.address, "on port", myServer.port)

# Keeps listening on the port and perform calculations
# The timeout is usually set on the client side
while True:  
    msg = myServer.recvmsg()