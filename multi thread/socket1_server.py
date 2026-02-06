# socket 서버 측 처리

from socket import *

# TCP/IP 소켓
serversock = socket(AF_INET, SOCK_STREAM)   # 소켓(종류, 유형)
serversock.bind(('127.0.0.1', 8888))        # bind 메소드의 인수는 튜플이어야 한다
serversock.listen(1)                        # 클라이언트와의 연결 정보 수는 1~5 값을 허용
print('server start...')

conn.addr = serversock.accept()             # 연결 대기 상태가 된다
print('client addr:', addr)                 # 외부로부터 접속 시 해당 클라이언트의 정보 확인
print('from client message:', conn.recv(1024).decode()) # 메시지 수신 후 디코딩하여 출력
conn.close()                                # 연결 객체를 닫는다
serversock.close()                          # 서버 소켓을 닫는다