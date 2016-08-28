import socket

# Define host and port
target_host = "192.168.1.3"
target_port = 53

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto("AAABBBCCCDDD",(target_host,target_port))

  # receive some data
data, addr = client.recvfrom(4096)

print data
