import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#csv 파일(형식: 이름, 이메일)에서 수신자 목록 로드
def load_target_list(csv_file_path):
    target_list = []

    with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # 헤더(첫번째 줄) 건너뛰기

        for row in reader:
            if len(row) < 2:
                continue
            name = row[0].strip()
            email = row[1].strip()
            if email:
                target_list.append((name, email))

    return target_list


def create_html_message(sender_email, recipients, subject, html_body):
    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = subject

    # HTML 형식으로 본문 추가
    html_part = MIMEText(html_body, 'html', _charset='utf-8')
    msg.attach(html_part)

    return msg


def send_bulk_email_once(gmail_account, gmail_password, targets, subject, html_template):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(gmail_account, gmail_password)

        # 한 번에 여러 명에게 보내기
        recipient_emails = [email for _, email in targets]

        # 이름은 템플릿 안에서 공통 내용만 사용 (개인화 없음)
        html_body = html_template.format(name='수신자 여러분')

        msg = create_html_message(
            sender_email=gmail_account,
            recipients=recipient_emails,
            subject=subject,
            html_body=html_body,
        )

        server.sendmail(gmail_account, recipient_emails, msg.as_string())
        print('한 번에 여러 명에게 메일을 전송했습니다.')

        server.quit()

    except smtplib.SMTPAuthenticationError:
        print('로그인 실패: 아이디 또는 비밀번호(앱 비밀번호)를 확인하세요.')

    except smtplib.SMTPException as error:
        print(f'SMTP 오류 발생: {error}')

    except Exception as error:
        print(f'알 수 없는 오류 발생: {error}')


def send_bulk_email_each(gmail_account, gmail_password, targets, subject, html_template):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(gmail_account, gmail_password)

        # 한 명씩 반복해서 보내기 (개인화 가능)
        for name, email in targets:
            html_body = html_template.format(name=name)

            msg = create_html_message(
                sender_email=gmail_account,
                recipients=[email],
                subject=subject,
                html_body=html_body,
            )

            server.sendmail(gmail_account, [email], msg.as_string())
            print(f'{name}({email}) 에게 메일을 전송했습니다.')

        server.quit()

    except smtplib.SMTPAuthenticationError:
        print('로그인 실패: 아이디 또는 비밀번호(앱 비밀번호)를 확인하세요.')

    except smtplib.SMTPException as error:
        print(f'SMTP 오류 발생: {error}')

    except Exception as error:
        print(f'알 수 없는 오류 발생: {error}')


def main():
    gmail_account = ' '                         # 보내는 사람의 구글 계정 입력
    gmail_password = ' '                        # 구글 앱 비밀번호 사용
    csv_file_path = './mail_target_list.csv'

    subject = 'HTML 테스트 메일'

    # HTML 템플릿 예시 (name 자리만 포맷팅으로 바꿔 씀)
    html_template = '''
    <html>
      <body>
        <p>{name} 님, 안녕하세요.</p>
        <p>이 메일은 Python SMTP를 이용해 전송된 <b>HTML 형식</b> 테스트 메일입니다.</p>
        <p>감사합니다.</p>
      </body>
    </html>
    '''

    targets = load_target_list(csv_file_path)

    if not targets:
        print('CSV에서 유효한 수신자 정보를 찾지 못했습니다.')
        return

    print('=== 한 번에 여러 명에게 보내기 ===')
    send_bulk_email_once(
        gmail_account=gmail_account,
        gmail_password=gmail_password,
        targets=targets,
        subject=subject,
        html_template=html_template,
    )

    print('=== 한 명씩 반복해서 보내기 ===')
    send_bulk_email_each(
        gmail_account=gmail_account,
        gmail_password=gmail_password,
        targets=targets,
        subject=subject,
        html_template=html_template,
    )


if __name__ == '__main__':
    main()
