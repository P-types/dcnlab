import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 1111))
server_socket.listen(1)
print("Server is running and waiting for client connection...")
client_socket, addr = server_socket.accept()
print("Client connected!")

while True:
  # Receive message from client
  message = client_socket.recv(1024).decode().strip()
  print(f"Client: {message}")
  if message == "goodbye":
    break
  # Type response for client
  resp = input("Enter Msg for Client: ")
  client_socket.send(resp.encode())

  if resp == "goodbye":
    break

client_socket.close()
server_socket.close()
print("Client closed")