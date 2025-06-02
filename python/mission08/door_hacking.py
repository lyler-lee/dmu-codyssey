# door_hacking.py
import zipfile
import itertools
import time
import datetime
import os

def unlock_zip():
    """
    emergency_storage_key.zip 파일의 암호를 무차별 대입으로 해제하는 함수
    암호는 숫자와 소문자로 구성된 6자리 문자열
    """
    # 허용 문자셋 정의 (숫자 0-9, 소문자 a-z)
    숫자 = '0123456789'
    소문자 = 'abcdefghijklmnopqrstuvwxyz'
    전체문자 = 숫자 + 소문자

    # 스크립트 실행 경로 기준으로 ZIP 파일 경로 확인
    스크립트_경로 = os.path.dirname(os.path.abspath(__file__))
    zip_파일_경로 = os.path.join(스크립트_경로, 'emergency_storage_key.zip')

    # 파일 존재 여부 확인
    if not os.path.exists(zip_파일_경로):
        print('오류: emergency_storage_key.zip 파일을 찾을 수 없습니다.')
        return None

    # ZIP 파일 열기 시도
    try:
        zip_파일 = zipfile.ZipFile(zip_파일_경로)
    except zipfile.BadZipFile:
        print('오류: 유효하지 않은 ZIP 파일 형식입니다.')
        return None
    except Exception as e:
        print(f'ZIP 파일 열기 실패: {e}')
        return None

    # 시간 측정 시작
    시작_시간 = time.time()
    시작_시간_형식 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[시작 시간] {시작_시간_형식}')
    print('[전략 1] 모든 숫자 조합 시도 (1,000,000개)')

    # 전략 1: 모든 숫자 조합 먼저 시도
    for 조합 in itertools.product(숫자, repeat=6):
        암호_시도 = ''.join(조합)
        
        try:
            zip_파일.extractall(pwd=암호_시도.encode('utf-8'))
            성공_처리(암호_시도, 시작_시간)
            return 암호_시도
        except:
            continue

    print('[전략 2] 모든 소문자 조합 시도 (308,915,776개)')
    
    # 전략 2: 모든 소문자 조합 시도
    for 조합 in itertools.product(소문자, repeat=6):
        암호_시도 = ''.join(조합)
        
        try:
            zip_파일.extractall(pwd=암호_시도.encode('utf-8'))
            성공_처리(암호_시도, 시작_시간)
            return 암호_시도
        except:
            continue

    print('[전략 3] 혼합 조합 시도 (남은 모든 경우의 수)')
    총_시도횟수 = 0  # 이미 시도한 1,000,000 + 308,915,776 건 제외

    # 전략 3: 숫자와 문자의 혼합 조합 시도
    for 조합 in itertools.product(전체문자, repeat=6):
        현재_암호 = ''.join(조합)
        
        # 이미 시도한 경우 건너뜀
        if (all(c in 숫자 for c in 현재_암호) or 
            all(c in 소문자 for c in 현재_암호)):
            continue
            
        총_시도횟수 += 1
        
        # 진행 상황 출력 (1,000,000회마다)
        if 총_시도횟수 % 1000000 == 0:
            경과_시간 = time.time() - 시작_시간
            print(f'[진행] 시도 횟수: {총_시도횟수:,}회')
            print(f'[경과 시간] {시간_형식(경과_시간)}')
            print(f'[현재 시도 암호] {현재_암호}')
        
        try:
            zip_파일.extractall(pwd=현재_암호.encode('utf-8'))
            성공_처리(현재_암호, 시작_시간)
            return 현재_암호
        except:
            continue

    print('암호를 찾지 못했습니다.')
    return None

def 성공_처리(암호, 시작_시간):
    """성공 시 공통 처리 루틴"""
    경과_시간 = time.time() - 시작_시간
    
    print(f'\n※ 암호 해독 성공 ※')
    print(f'발견된 암호: {암호}')
    print(f'소요 시간: {시간_형식(경과_시간)}')
    
    # 암호 파일 저장
    try:
        with open('password.txt', 'w') as 파일:
            파일.write(암호)
        print('암호가 password.txt 파일에 저장되었습니다.')
    except Exception as e:
        print(f'파일 저장 오류: {e}')

def 시간_형식(초):
    """초 단위 시간을 읽기 쉬운 형식으로 변환"""
    시간, 나머지 = divmod(초, 3600)
    분, 초 = divmod(나머지, 60)
    return f'{int(시간)}시간 {int(분)}분 {초:.2f}초'



if __name__ == '__main__':
    unlock_zip()
