import socket

cli_port=6000
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.settimeout(1.0)

while True:
    msg=input("Enter the message for the server:(say goodbye to exit )")
    send_data=msg.encode()
    client_socket.sendto(send_data,('localhost',cli_port))
    if msg == "goodbye":
        client_socket.close()
        break