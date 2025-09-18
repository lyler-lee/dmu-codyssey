import socket
import threading

clients = []
nicknames = []

def broadcast(message):
    """
    접속된 모든 클라이언트에게 메시지 전송
    """
    for client in clients:
        client.send(message)

def handle_client(client):
    """
    각 클라이언트별로 독립적으로 메시지 처리
    """
    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                break
            # '/종료' 입력 처리
            if msg.decode() == '/종료':
                # 닉네임 인덱스 찾기
                idx = clients.index(client)
                name = nicknames[idx]
                leave_message = f'{name}님이 퇴장하셨습니다.'.encode()
                broadcast(leave_message)
                client.close()
                clients.remove(client)
                nicknames.remove(name)
                break
            else:
                idx = clients.index(client)
                name = nicknames[idx]
                message = f'{name}> {msg.decode()}'.encode()
                broadcast(message)
        except Exception:
            continue

def receive():
    """
    새로운 클라이언트 연결 받고, 닉네임 등록 및 쓰레드 생성
    """
    while True:
        client, address = server.accept()
        # 닉네임 요청 및 등록
        client.send('닉네임을 입력해 주세요: '.encode())
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)
        # 입장 메시지
        welcome_message = f'{nickname}님이 입장하셨습니다.'.encode()
        broadcast(welcome_message)
        # 클라이언트용 핸들 쓰레드 시작
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == '__main__':
    # 서버 소켓 생성 및 바인딩
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen()
    print('서버가 시작되었습니다.')
    receive()
