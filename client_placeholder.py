# client2.py
#!/usr/bin/env python

import socket

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
filename = 'mytext.txt'
f = open(filename, 'rb')
l = f.read(BUFFER_SIZE)
while (l):
    s.send(l)
     # print('Sent ',repr(l))
    l = f.read(BUFFER_SIZE)
if not l:
    f.close()
    s.close()

print('Successfully get the file')
s.close()
print('connection closed')