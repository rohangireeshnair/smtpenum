
def filecheck(fl, sock) :
    try:
        file=open(fl)
        while(file):
            usrname=file.readline()
            sock.send('VRFY ' + usrname + '\r \n')
            print(sock.recv())
    except(FileNotFoundError):
        print("The mentioned file doesnt't exist")
