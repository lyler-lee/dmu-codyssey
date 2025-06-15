import os
import csv
import wave
import speech_recognition as sr # pip install SpeechRecognition 명령을 통해 설치한 후 실행하여야 함.

class AudioProcessor:
    """오디오 파일 처리 클래스"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def get_audio_duration(self, file_path):
        """WAV 파일 지속 시간 계산"""
        try:
            with wave.open(file_path, 'rb') as audio_file:
                return audio_file.getnframes() / audio_file.getframerate()
        except (wave.Error, IOError) as e:
            print(f"오디오 파일 오류: {e}")
            return 0.0
    
    def process_audio(self, file_path):
        """오디오 파일을 청크 단위로 처리"""
        results = []
        try:
            with sr.AudioFile(file_path) as source:
                total_duration = self.get_audio_duration(file_path)
                start_time = 0.0
                
                while start_time < total_duration:
                    audio_chunk = self.recognizer.record(
                        source, duration=min(10.0, total_duration - start_time)
                    )
                    text = self._recognize_speech(audio_chunk)
                    results.append((start_time, text))
                    start_time += 10.0
        except Exception as e:
            print(f"오디오 처리 실패: {e}")
        return results
    
    def _recognize_speech(self, audio_chunk):
        """음성 인식 수행"""
        try:
            return self.recognizer.recognize_google(audio_chunk, language='ko-KR')
        except sr.UnknownValueError:
            return "인식 불가"
        except sr.RequestError as e:
            print(f"STT 서비스 에러: {e}")
            return "서비스 오류"

def generate_csv(audio_file, data):
    """CSV 파일 생성기"""
    base_name = os.path.splitext(audio_file)[0]
    try:
        with open(f"{base_name}.csv", 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['시간(초)', '텍스트'])
            for time, text in data:
                writer.writerow([f"{time:.2f}", text])
        print(f"{base_name}.csv 생성 완료")
    except IOError as e:
        print(f"파일 저장 실패: {e}")

def main():
    processor = AudioProcessor()
    records_dir = 'records'
    
    if not os.path.exists(records_dir):
        print("녹음 파일 디렉토리 없음")
        return

    for filename in os.listdir(records_dir):
        if filename.endswith('.wav'):
            file_path = os.path.join(records_dir, filename)
            stt_results = processor.process_audio(file_path)
            generate_csv(filename, stt_results)

if __name__ == "__main__":
    main()
