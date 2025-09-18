import socket
import threading

def receive_messages(sock):
    """
    서버로부터 수신된 메시지를 화면에 출력
    """
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                break
            print(message)
        except Exception:
            break

def send_messages(sock, nickname):
    """
    사용자 입력을 서버에 전송. '/종료' 입력 시 연결 종료
    """
    while True:
        msg = input()
        if msg == '/종료':
            sock.send('/종료'.encode())
            sock.close()
            break
        else:
            sock.send(msg.encode())

def main():
    host = input('서버 주소를 입력하세요: ')
    port = int(input('서버 포트를 입력하세요: '))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    # 서버로부터 닉네임 요청받기
    nickname_req = sock.recv(1024).decode()
    print(nickname_req)
    nickname = input()
    sock.send(nickname.encode())

    # 메시지 수신 및 송신용 쓰레드 실행
    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    receive_thread.daemon = True
    receive_thread.start()

    send_messages(sock, nickname)

if __name__ == '__main__':
    main()
