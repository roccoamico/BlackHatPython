import socket

target_host = "www.beliven.com"
target_port = 80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET=IPv4, SOCK_STREAM=TCP

#connect to the client
client.connect((target_host, target_port))

#send data
client.send(b"GET / HTTP/1.1\r\nHost: beliven.com\r\n\r\n")

#receive data
response = client.recv(4096)

print(response.decode())
client.close()
