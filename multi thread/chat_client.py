import socket
import threading
import sys

# 채팅 서버로부터 수신되는 메시지를 처리하는 함수
def Handle(socket):
    while True:
        try:
            data = socket.recv(1024)    # 서버가 전송한 메시지 수신
            if not data:
                print("\n[서버와의 연결이 끊어졌습니다.]")
                break # 수신 메시지가 없으면 반복문 종료
            print(data.decode('UTF-8'))
        except:
            break

sys.stdout.flush()                  # 표준 출력장치 비우기
name = input('채팅 아이디 입력:')

# 채팅 서버와 통신을 위한 소켓 객체 생성
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    cs.connect(('127.0.0.1', 5000))
    cs.send(name.encode('UTF-8'))

    th = threading.Thread(target=Handle, args=(cs,))    # 스레드 객체 생성
    th.daemon = True # 메인 종료 시 스레드도 자동 종료 설정
    th.start()                     # 스레드 처리를 하는 Handle() 메소드 호출

    # 채팅 서버와의 지속적 연결을 위해 무한루핑
    while True:
        msg = input()
        sys.stdout.flush()

        if not msg: continue        # 송신 메시지가 없으면 송신하지 않고 반복문 수행
        if msg.lower() == 'exit': break # exit 입력 시 종료 로직 추가
        
        cs.send(msg.encode('UTF-8'))
except Exception as e:
    print(f"연결 오류: {e}")
finally:
    cs.close()