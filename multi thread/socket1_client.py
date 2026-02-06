# socket 클라이언트 측 처리

from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1', 8888))     # 서버 연결을 시작

clientsock.send('안녕 반가워'.encode(encoding='UTF-8')) # 메세지를 인코딩해 서버로 전송
clientsock.close()     # 클라이언트 소켓 닫기