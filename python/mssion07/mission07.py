 # calculator.py
# 계산기 클래스와 PyQt5 UI를 포함한 전체 코드입니다.

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
import sys

# PyQt5.QtCore: PyQt에서 기본적인 상수와 기능 제공 (여기서는 정렬에 사용)
from PyQt5.QtCore import Qt

class Calculator:
    def __init__(self):
        self.current_value = ''   # 현재 입력된 숫자 및 연산자 문자열
        self.is_negative = False  # 음수 상태를 뜻함. 초기 상태는 + 이므로 false.
        self.has_decimal = False  # 소수점 입력 여부. 초기 상태는 소수점이 없으므로 false.

    def add(self, a, b):
        return a + b  # 덧셈 연산

    def subtract(self, a, b):
        return a - b  # 뺄셈 연산

    def multiply(self, a, b):
        return a * b  # 곱셈 연산

    def divide(self, a, b):
        if b == 0:
            raise ValueError('0으로 나눌 수 없습니다.')  # 0으로 나누기 예외 처리
        return a / b  # 나눗셈 연산

    def reset(self):
        self.current_value = ''  # 입력값 초기화
        self.is_negative = False  # 음수 상태 초기화
        self.has_decimal = False  # 소수점 상태 초기화

    def negative_positive(self):
        self.is_negative = not self.is_negative  # 음수/양수 상태 토글

    def percent(self):
        if self.current_value:
            try:
                value = float(self.current_value)
                value /= 100  # 100으로 나누어 퍼센트 계산
                self.current_value = self.format_number(value)
            except Exception:
                self.current_value = '잘못된 수식입니다.'

    def input_number(self, num):
        if self.current_value == '0':
            self.current_value = str(num)  # 0으로 시작하면 덮어씀
        else:
            self.current_value += str(num)  # 숫자 누적 입력

    def input_decimal(self):
        if not self.has_decimal:
            if self.current_value == '':
                self.current_value = '0.'  # 빈 상태에서 소수점 입력 시 0.으로 시작
            else:
                self.current_value += '.'  # 소수점 추가
            self.has_decimal = True  # 소수점 입력 플래그 설정

    def equal(self):
        try:
            # 음수 상태 반영
            expr = self.current_value
            if self.is_negative and not expr.startswith('-'):
                expr = '-' + expr
            result = eval(expr)  # 문자열 수식 계산
            self.current_value = self.format_number(result)
            return self.current_value
        except ZeroDivisionError:
            self.current_value = ''
            return '0으로 나눌 수 없습니다.'
        except Exception:
            self.current_value = ''
            return '잘못된 수식입니다.'

    def format_number(self, value):
        # 아이폰 지수 표기법: 10자리 이상이면 e 표기법 사용
        try:
            if abs(value) >= 1e10 or (abs(value) < 1e-6 and value != 0):
                return '{:e}'.format(value)  # 지수 표기법
            else:
                return str(float(value)).rstrip('0').rstrip('.') if '.' in str(value) else str(value)
        except Exception:
            return str(value)

class CalculatorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.calc = Calculator()  # Calculator 클래스 인스턴스 생성
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')  # 창 제목 설정
        self.setGeometry(100, 100, 300, 400)  # 창 크기 및 위치 설정

        self.layout = QVBoxLayout()  # 메인 레이아웃
        self.display = QLineEdit()  # 결과 표시용 입력창
        self.display.setReadOnly(True)  # 직접 입력 방지
        self.display.setAlignment(Qt.AlignRight)  # 오른쪽 정렬
        self.layout.addWidget(self.display)

        self.buttons = QGridLayout()  # 버튼 그리드 레이아웃

        # 버튼 텍스트와 핸들러 매핑
        buttons = [
            ('7', self.num_clicked), ('8', self.num_clicked), ('9', self.num_clicked), ('/', self.op_clicked),
            ('4', self.num_clicked), ('5', self.num_clicked), ('6', self.num_clicked), ('*', self.op_clicked),
            ('1', self.num_clicked), ('2', self.num_clicked), ('3', self.num_clicked), ('-', self.op_clicked),
            ('0', self.num_clicked), ('.', self.decimal_clicked), ('=', self.equal_clicked), ('+', self.op_clicked),
            ('C', self.reset_clicked), ('+/-', self.neg_pos_clicked), ('%', self.percent_clicked), ('', None)
        ]

        positions = [(i, j) for i in range(5) for j in range(4)]  # 5x4 그리드

        for position, (text, handler) in zip(positions, buttons):
            if text:
                button = QPushButton(text)  # 버튼 생성
                button.clicked.connect(handler)  # 클릭 시 핸들러 연결
                self.buttons.addWidget(button, *position)  # 그리드에 버튼 추가

        self.layout.addLayout(self.buttons)
        self.setLayout(self.layout)

    def num_clicked(self):
        button = self.sender()
        self.calc.input_number(button.text())  # 숫자 입력 처리
        self.display.setText(self.calc.current_value)

    def op_clicked(self):
        button = self.sender()
        if self.calc.current_value and self.calc.current_value[-1] not in '+-*/':
            self.calc.input_number(button.text())  # 연산자 입력 처리
            self.calc.has_decimal = False  # 연산자 입력 후 소수점 플래그 초기화
        self.display.setText(self.calc.current_value)

    def decimal_clicked(self):
        self.calc.input_decimal()  # 소수점 입력 처리
        self.display.setText(self.calc.current_value)

    def equal_clicked(self):
        result = self.calc.equal()  # 결과 계산
        self.display.setText(str(result))

    def reset_clicked(self):
        self.calc.reset()  # 초기화
        self.display.setText(self.calc.current_value)

    def neg_pos_clicked(self):
        self.calc.negative_positive()  # 음수/양수 토글
        if self.calc.current_value:
            if self.calc.is_negative and not self.calc.current_value.startswith('-'):
                self.calc.current_value = '-' + self.calc.current_value
            elif not self.calc.is_negative and self.calc.current_value.startswith('-'):
                self.calc.current_value = self.calc.current_value[1:]
        self.display.setText(self.calc.current_value)

    def percent_clicked(self):
        self.calc.percent()  # 퍼센트 계산
        self.display.setText(self.calc.current_value)


# 
if __name__ == '__main__':
    app = QApplication(sys.argv)    # QApplication 객체 생성
    ex = CalculatorUI()             # Calculator 인스턴스 생성
    ex.show()                       # 계산기 윈도우 표시
    sys.exit(app.exec_())           # 이벤트 루프 실행 및 종료 처리
