from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

PORT = 8080

class SpacePirateHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]
        connect_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('접속 시간:', connect_time)
        print('클라이언트 IP:', client_ip)
        if self.path == '/':
            try:
                with open('index.html', 'r', encoding='utf-8') as f:
                    content = f.read()
            except FileNotFoundError:
                self.send_response(404)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write('index.html 파일을 찾을 수 없습니다.'.encode('utf-8'))
                return
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write('잘못된 요청입니다.'.encode('utf-8'))

def run_server():
    server = HTTPServer(('', PORT), SpacePirateHandler)
    print('서버가 시작되었습니다. 포트:', PORT)
    server.serve_forever()

if __name__ == '__main__':
    run_server()
