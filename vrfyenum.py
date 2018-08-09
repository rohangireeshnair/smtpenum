import socket
import sys

if(len(sys.argv[1])==0) :
    print("Error! No username file mentioned")

if(len(sys.argv[2]==0)) :
    print("Error! No ip mentioned")

fl=sys.argv[1]
ip=sys.argv[2]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, 25))

banner=sock.recv(1024)
print(banner)


