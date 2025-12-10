import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(gmail_account, gmail_password, to_email, subject, body):
    try:
        # SMTP 서버 접속 설정 (Gmail SMTP 포트: 587)
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        # MIME 멀티파트 메일 객체 생성
        msg = MIMEMultipart()
        msg['From'] = gmail_account
        msg['To'] = to_email
        msg['Subject'] = subject

        # 메일 본문 첨부 (문자열은 기본 ' ' 사용)
        msg.attach(MIMEText(body, 'plain'))

        # SMTP 서버 연결 및 TLS 시작
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # 로그인
        server.login(gmail_account, gmail_password)

        # 메일 전송
        server.sendmail(gmail_account, to_email, msg.as_string())

        # 서버 연결 종료
        server.quit()

        print('메일이 성공적으로 전송되었습니다.')

    except smtplib.SMTPAuthenticationError:
        print('로그인 실패: 아이디 또는 비밀번호를 확인하세요.')

    except smtplib.SMTPException as e:
        print(f'SMTP 오류 발생: {e}')

    except Exception as e:
        print(f'알 수 없는 오류 발생: {e}')


if __name__ == '__main__':
    gmail_account = 'your_email@gmail.com'                              # 실제 Gmail 주소 입력
    gmail_password = 'mycn bhbx njsi penh'                              # Gmail의 경우 https://myaccount.google.com/security 에서 앱 비밀번호 생성 필요     
    to_email = 'ljhk3253@naver.com'                                     # 이메일을 받을 사람의 실제 이메일 주소 입력
    subject = '테스트 메일 제목'
    body = '이것은 Python으로 발송한 테스트 메일입니다.'

    send_email(gmail_account, gmail_password, to_email, subject, body)

