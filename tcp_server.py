import socket
import sys
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('0.0.0.0', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

sock.listen(1)

while True:
    print >>sys.stderr, 'waiting on connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr,'connection from', client_address
        while True:
            data = connection.recv(1024)
            print >>sys.stderr, 'received from "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
    finally:
        connection.close()
        
