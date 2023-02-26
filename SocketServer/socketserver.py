import socket, numpy as np
from sklearn.linear_model import LinearRegression

class socketserver:
    def __init__(self, address = '', port = ''):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address
        self.port = port
        self.sock.bind((self.address, self.port))
        
    
    def recvmsg(self):
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()
        print('connected to', self.addr)
        self.cummdata = ''
        

        while True:
            data = self.conn.recv(10000)
            self.cummdata+=data.decode("utf-8")
            print(data)
            if not data:
                print("no data")
                break    
            self.conn.send(bytes(calcregr(self.cummdata), "utf-8"))
            return self.cummdata
            
    def __del__(self):
        self.sock.close()

def calcregr(msg = ''):
    chartdata = np.fromstring(msg, dtype=float, sep= ' ') 
    print(chartdata);
    Y = np.array(chartdata).reshape(-1,1)
    X = np.array(np.arange(len(chartdata))).reshape(-1,1)
        
    lr = LinearRegression()
    lr.fit(X, Y)
    Y_pred = lr.predict(X)

    P = Y_pred.astype(str).item(-1) + ' ' + Y_pred.astype(str).item(0)
    print(P)
    return str(P)
    
serv = socketserver('192.168.1.15', 14201)
print("Start Python server at",serv.address, "on port", serv.port)

while True:  
    msg = serv.recvmsg()
 
    