# Hello Mars 출력하기
print('Hello Mars')


# mission_computer_main.log 파일 내용 출력

import os

def read_log_file(filename):
    try:
   
   # 파일 존재 여부 확인
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Error: '{filename}' 파일을 찾을 수 없습니다.")
        
   # 파일 읽기
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except PermissionError:
        print(f"Error: '{filename}' 파일에 접근할 권한이 없습니다.")
    except Exception as e:
        print(f'알 수 없는 오류 발생: {e}')



# 로그 파일 경로 지정
log_filename = 'mission_computer_main.log'
read_log_file(log_filename)
