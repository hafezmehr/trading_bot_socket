import socket, numpy as np
from sklearn.linear_model import LinearRegression

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
        print('connected to', self.addr)

        self.commdata = '' # For storing recieved data
        
        # Recieving data
        # The standard practise is to log the data in this loop if needed
        while True:
            # recv() recieves data in binary
            data = self.conn.recv(10000) # Data size in Bites (binary data)
            
            #appending the recieved data to commdata
            self.commdata+=data.decode("utf-8") # Converting the data to UTF-8
            print(data) # Prints the recieved data
            
            if not data:
                print("no data") # This usually will be printed on clientsocket timeouts
                break # Breaks the while loop but the server will stay online
            # Sending the response to the client (in this case the MetaTrader Expert Advisor)
            # In this case we caculate a regressin on the recieved data and send the regression line position data
            # Data is converted from UTF-8 to binary using bytes()
            self.conn.send(bytes(calcregr(self.commdata), "utf-8"))
            return self.commdata
        
    # Kills the socket server
    def __del__(self):
        self.newSocket.close()

# Regression calculation using SciKit-Learn.
# You can substitue this with any other calculation.
# This part is copyied from this Persian tutorial by Masoomeh Karami: https://soodgah.com/shop/tutorials/P1066-metatrader5-python-socket-connection-course.html
def calcregr(msg = ''):
    chartdata = np.fromstring(msg, dtype=float, sep= ' ') # Data is seperated by a white space in this example
    print(chartdata);
    Y = np.array(chartdata).reshape(-1,1)
    X = np.array(np.arange(len(chartdata))).reshape(-1,1)

    lr = LinearRegression()
    lr.fit(X, Y)
    Y_pred = lr.predict(X)

    P = Y_pred.astype(str).item(-1) + ' ' + Y_pred.astype(str).item(0)
    print(P)
    return str(P)

# Creating a new sockek object with your ip and a port. It starts automatically.
# The same ip and port will be used on the client side
myServer = socketserver('192.168.1.15', 14201) # The TCP port is number between 0 and 65,535

print("Start Python server at",myServer.address, "on port", myServer.port)

# Keeps listening on the port and perform calculations
# The timeout is usually set on the client side
while True:  
    msg = myServer.recvmsg()