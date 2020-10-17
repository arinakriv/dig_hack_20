# server.py
import socket
from threading import Thread
from socketserver import ThreadingMixIn
import datetime
TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024
#from docx import Document
class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print (" New thread started for "+ip+":"+str(port))

    def run(self):
        fName = datetime.datetime.today().strftime("%A, %d.%m.%Y, %H  %M  %S")
        with open(fName, 'wb') as f:
            print('file opened')
            while True:
                # print('receiving data...')
                data = self.sock.recv(BUFFER_SIZE)
                print('data=%s', (data))
                if not data:
                    f.close()
                    print('file close()')
                    break
                # write data to a file
                f.write(data)


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print("Waiting for incoming connections...")
    (conn, (ip,port)) = tcpsock.accept()
    print('Got connection from ', (ip,port))
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
