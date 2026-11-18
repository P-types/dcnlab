
import socket

s=socket.socket()
s.connect(('localhost',1234))
data=input("Enter the data to be sent:")
stuffed=""
count=0
for bit in data:
    stuffed+=bit
    if bit=='1':
        count+=1
        if count==5:
            stuffed+="0"
            count=0
    else:
        count=0
print("Stuffed data:",stuffed)
s.send(stuffed.encode())
s.close()