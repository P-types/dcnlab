import socket

ser_port = 6000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("localhost", ser_port))

print("Server Started.")
while True:
  print(f"Server Ready to receive data on port:{ser_port}...")
  receive_data, client_address = server_socket.recvfrom(1024)
  client_message = receive_data.decode().strip()

  print(
      f" Client [IP: {client_address[0]} Port: {client_address[1]}]:"
      f" {client_message}"
  )

  if client_message == "goodbye":
    server_socket.close()
    break