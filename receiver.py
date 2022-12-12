import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

client, addr = server.accept()
file_name = client.recv(1024).decode()
file_size = client.recv(1024).decode()
file = open(file_name, "wb")
file_bytes = b""
done = False

while not done:
    data = client.recv(1024)
    if file_bytes[-5:] == b"<END>":
        done = True
    else:
        file_bytes += data


file. write(file_bytes)

file. close()
client.close()
server.close()