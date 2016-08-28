## Import Low-Level Network Layer
import socket

## Define Network Host/Service to Test
target_host = "192.168.1.1"
target_port = 443

## Establish client protocol (AF_INET for TCP/IP v4 Support)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Connect to target host/port
client.connect((target_host,target_port))

## Send data to target
client.send("GET / HTTP/1.1\r\nHost: 192.168.1.1\r\n\r\n")

## Receive response
response = client.recv(4096)

print response
