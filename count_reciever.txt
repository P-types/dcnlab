import socket

s=socket.socket()
s.bind(('localhost',1234))
s.listen(1)
print("Waiting for sender.....")

conn,addr=s.accept()

print("connected to:",addr)

while True:
    frame=conn.recv(1024)
    if not frame:
        break
    print("Frame recieved:",frame.decode())

conn.close()
s.close()