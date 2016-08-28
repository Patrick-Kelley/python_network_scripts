## Socket Testing Tool
import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage ():
    print "Testing NET Tool"
    print 
    print "Usage: socket_testing.py -t target_host -p port"
    print "-l --listen    - listen on [host]:[port] for incoming connections"
    print "-e --execute=file_to_run - execute the given file upon receiving a connection"
    print "-c --command - initialize a command shell"
    print "-u --upload=destination - upon receiving connection upload a file and write to [destination]"
    print
    print
    print "Examples: "
    print "socket_testing.py -t 192.168.1.1 -p 10000 -l c"
    print "socket_testing.py -t 192.168.1.1 -p 10000 -l -u=c:\\payload.exe"
    print "socket_testing.py -t 192.168.1.1 -p 10000 -l -e=\"cat /etc/passwd\""
    print "echo 'ABCDEFGHI' | ./socket_testing.py -t 192.168.1.3 -p 135"
    sys.exit(0)

def main():
        global listen
        global port 
        global execute 
        global command
        global upload_destination
        global target

        if not len(sys.argv[1:]):
            usage()

        try:
                opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",
                ["help","listen","execute","target","port","command","upload"])
        except getopt.GetoptError as err:
                print str(err)
                usage()

        for o,a in opts:
                if o in ("-h","--help"):
                        usage()
                elif o in ("-l","--listen"):
                        listen = True
                elif o in ("-e", "--execute"):
                        execute = a
                elif o in ("-c", "--commandshell"):
                        command = True
                elif o in ("-u", "--upload"):
                        upload_destination = a
                elif o in ("-t", "--target"):
                        target = a
                elif o in ("-p", "--port"):
                        port = int(a)
                else:
                        assert False,"Unhandled Option"

        if not listen and len(target) and port > 0:
            buffer = sys.stdin.read()
            client_sender(buffer)

        if listen:
                server_loop()
main()
