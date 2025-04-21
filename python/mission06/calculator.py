# sys: 파이썬 인터프리터와 관련된 기능 제공 (여기서는 프로그램 종료에 사용)
import sys

# PyQt5.QtWidgets: PyQt에서 UI 위젯(버튼, 레이아웃 등)을 제공
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout
)

# PyQt5.QtCore: PyQt에서 기본적인 상수와 기능 제공 (여기서는 정렬에 사용)
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()          # 부모 클래스 초기화

        # 윈도우 제목 설정
        self.setWindowTitle('Calculator')

        # 윈도우 크기 고정
        self.setFixedSize(320, 480)

        # 중앙 위젯 생성
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)

        # UI 생성 함수 호출
        self._create_ui()


    def _create_ui(self):

        # 전체 레이아웃(수직 박스 레이아웃) 생성
        main_layout = QVBoxLayout()

        # 결과 및 입력을 보여줄 디스플레이(한 줄 입력창) 생성
        self.display = QLineEdit()                      # 입력창 생성
        self.display.setReadOnly(True)                  # 입력창을 읽기 전용으로 설정
        self.display.setAlignment(Qt.AlignRight)        # 오른쪽 정렬
        self.display.setFixedHeight(60)                 # 60px 높이 설정
        self.display.setStyleSheet('font-size: 24px;')  # 폰트 크기 설정
        main_layout.addWidget(self.display)             # 레이아웃에 추가

        # 버튼을 담을 그리드 레이아웃 생성
        grid = QGridLayout()
        # 아이폰 계산기 어플 레이아웃처럼 버튼 텍스트를 행별로 정의 
        buttons = [
            ['C', '+/-', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '0', '.', '=']
        ]

        self.button_map = {}  # 버튼 텍스트와 버튼 객체 매핑용 딕셔너리
        for row, row_values in enumerate(buttons):
            for col, btn_text in enumerate(row_values):

                # 마지막 행의 첫 번째 '0' 버튼은 두 칸 크기 정도로 만듦 (아이폰 계산기 스타일)
                if row == 4 and col == 0:
                    button = QPushButton('0')
                    button.setFixedSize(140, 60)            # 두 칸 크기
                    grid.addWidget(button, row, col, 1, 2)  # (행, 열, 행합치기, 열합치기)
                

                # 이미 합쳐진 칸은 건너뜀
                elif row == 4 and col == 1:
                    continue
                else:
                    button = QPushButton(btn_text)
                    button.setFixedSize(60, 60)             # 일반 버튼 크기

                    # 마지막 행에서 두 번째 이후 버튼은 위치 조정
                    grid.addWidget(button, row, col if not (row == 4 and col > 1) else col + 1)

                # 버튼 클릭 시 이벤트 연결
                button.clicked.connect(self._on_button_clicked)

                # 버튼 텍스트로 버튼 객체 저장
                self.button_map[btn_text] = button

        # 그리드 레이아웃을 메인 레이아웃에 추가
        main_layout.addLayout(grid)

        # 중앙 위젯에 메인 레이아웃 설정
        self._central_widget.setLayout(main_layout)

        # 입력 문자열을 저장할 변수 초기화
        self.input_str = ''


    def _on_button_clicked(self):

        # 클릭된 버튼 객체를 가져옴
        sender = self.sender()
        text = sender.text()

        # 숫자 및 소수점 입력 처리
        if text in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}:
            self.input_str += text

        # 연산자 입력 처리 (연속 입력 방지)
        elif text in {'+', '-', '*', '/'}:
            if self.input_str and self.input_str[-1] not in '+-*/':
                self.input_str += text

        # 전체 초기화(C) 버튼
        elif text == 'C':
            self.input_str = ''

        # 부호 변경(+/-) 버튼
        elif text == '+/-':
            if self.input_str and self.input_str[0] == '-':
                self.input_str = self.input_str[1:]             # 부호가 '-'인 경우 제거
            elif self.input_str:
                self.input_str = '-' + self.input_str           # 부호가 없는 경우 '-' 추가

        # 백분율(%) 버튼
        elif text == '%':
            if self.input_str:
                try:
                    self.input_str = str(float(self.input_str) / 100)  # 100으로 나누기
                except Exception:
                    self.input_str = 'Error'                            # 나눌수 없을 경우 또는 예외(숫자 입력후 연산자 두번이상 입력 등)에 걸리는 경우 "Error" 출력

        # 계산 결과(=) 버튼
        elif text == '=':

            try:
                self.input_str = str(eval(self.input_str))  # eval() 로 간단한 사칙연산 처리
            except Exception:
                self.input_str = 'Error'                    # eval() 사용 시 예외 발생(= 연산 불가능한 경우) 시 "Error" 출력

        # 입력 문자열을 디스플레이에 출력
        self.display.setText(self.input_str)




# 프로그램 진입점
if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication 객체 생성
    calc = Calculator()           # Calculator 인스턴스 생성
    calc.show()                   # 계산기 윈도우 표시
    sys.exit(app.exec_())         # 이벤트 루프 실행 및 종료 처리
