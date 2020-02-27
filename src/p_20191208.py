# from random import randint
# from time import time, sleep

# def download_tast(filename):
#     print('downloading %s ...' % filename)
#     time_to_download = randint(5,10)
#     sleep(time_to_download)
#     print('%sdownloading succeed, time:%d'%(filename,time_to_download))

# def main():
#     start = time()
#     download_tast('Ab')
#     download_tast('Bob')
#     end = time()
#     print('time in total: %2f' %(end-start))

# if __name__ =='__main__':
#     main()

from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('127.0.0.1',6789))
    #172.20.10.3
    #127.1.1.1
    server.listen(512)
    print('server starts to listen...')
    while True:
        client, addr = server.accept()
        print(str(addr)+'connect to server')
        client.send(str(datetime.now()).encode('uft-8'))
        client.close()
    # client,addr = server.accept()
    # print(str(addr))

if __name__ == '__main__':
    main()

# from socket import socket

# def main():
#     client = socket()
#     client.connect(('127.0.0.2', 6789))
#     print(client.recv(1024).decode('utf-8'))
#     client.close()

# if __name__ == '__main__':
#     main()