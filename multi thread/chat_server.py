import socket
import threading

# 서버 설정
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('127.0.0.1', 5000))
ss.listen(5)
print('채팅 서버 서비스 시작...')

users = [] # 모든 클라이언트와의 연결 객체를 저장하는 리스트 변수

def ChatUser(conn):   # 각 클라이언트와 연결 및 데이터 송수신 처리 함수
    try:
        # 클라이언트로부터 채팅명 수신 및 문자열 변환
        data_name = conn.recv(1024)
        name = data_name.decode('UTF-8') 
        
        data = '^^ ' + name + '님 입장 ^^'
        print(data)

        # 모든 접속자에게 입장 알림 (Broadcasting)
        for p in users:
            p.send(data.encode('UTF-8'))

        while True:
            msg = conn.recv(1024)            
            if not msg: break # 연결이 끊기면 반복문 탈출
            
            # 수신한 메시지를 닉네임과 합쳐서 전송 데이터 생성
            data = name + '님 메시지: ' + msg.decode('UTF-8')
            
            # 모든 접속자에게 메시지 전달
            for p in users:
                p.send(data.encode('UTF-8'))
    except:
        pass # 에러 발생 시 아래 finally 블록으로 이동하여 처리
    finally:
        # 예외 발생이나 연결 종료 시 사용자 제거
        if conn in users:
            users.remove(conn)        
        
        # name 변수가 정상적으로 생성된 경우에만 퇴장 알림 전송
        exit_name = name if 'name' in locals() else "알 수 없는 사용자"
        data = '~~ ' + exit_name + '님 퇴장 ~~'
        print(data)
        
        if users:
            for p in users:
                p.send(data.encode('UTF-8'))
        else:
            print('exit')
        conn.close() # 소켓 닫기

# 메인 실행 루프
while True:
    conn, addr = ss.accept() # 클라이언트 접속 대기 (Block 상태)
    users.append(conn)
    
    # 각 클라이언트마다 별도의 스레드 생성 (멀티스레딩)
    th = threading.Thread(target=ChatUser, args=(conn,))
    th.start()