import os
import datetime
import wave
import pyaudio  # 외부 라이브러리, 녹음 부분에만 사용

def create_records_folder():
    '''
    records 폴더가 없으면 생성합니다.
    '''
    if not os.path.exists('records'):
        os.makedirs('records')

def get_timestamp():
    '''
    현재 날짜와 시간을 '년월일-시간분초' 형식의 문자열로 반환합니다.
    '''
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d-%H%M%S')

def record_audio(duration=5, sample_rate=44100, chunk=1024, channels=1):
    '''
    마이크로부터 음성을 녹음하여 records 폴더에 저장합니다.
    duration: 녹음 시간(초)
    sample_rate: 샘플링 레이트(Hz)
    chunk: 버퍼 크기
    channels: 채널 수(모노=1, 스테레오=2)
    '''
    create_records_folder()
    filename = 'records/' + get_timestamp() + '.wav'

    audio = pyaudio.PyAudio()

    # 스트림 열기
    stream = audio.open(format=pyaudio.paInt16,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk)

    print('녹음을 시작합니다...')

    frames = []

    for _ in range(0, int(sample_rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print('녹음이 완료되었습니다.')

    # 스트림 종료
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # WAV 파일로 저장
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

    print('파일이 저장되었습니다:', filename)

if __name__ == '__main__':
    # 녹음 시간(초) 입력 받기
    try:
        duration = int(input('녹음할 시간을 초 단위로 입력하세요(기본값 5초): ') or '5')
    except ValueError:
        duration = 5

    record_audio(duration=duration)  # 녹음 시작
    
# 녹음된 음성은 'records' 폴더에 '년월일-시간분초.wav' 형식으로 저장됩니다.
# 이 코드는 pyaudio와 wave 라이브러리를 사용하여 마이크로부터 음성을 녹음하고,
# 녹음된 데이터를 WAV 파일로 저장합니다.
# pyaudio는 외부 라이브러리이므로 설치가 필요합니다.
# 설치 방법: pip install pyaudio    
