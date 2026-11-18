import socket

s=socket.socket()
s.bind(('localhost',1234))
s.listen(1)
print("Waiting for sender.....")
conn,addr=s.accept()
stuffed=conn.recv(1024).decode()

print("Received stuffed data:",stuffed)

destuffed=""
count=0
i=0

while i<len(stuffed):
    bit=stuffed[i]
    destuffed+=bit
    if bit=='1':
        count+=1
        if count==5:
            i+=1
            count=0
    else:
        count=0
    i+=1

print("Destuffed data:",destuffed)
conn.close()
s.close()