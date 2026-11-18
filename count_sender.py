import socket

s=socket.socket()
s.connect(('localhost',1234))

while True:
    frame=input("enter the frame:")
    if frame.lower()==exit :
        break
    s.send(frame.encode())
    print("Length of the frame",len(frame.encode()))

s.close()