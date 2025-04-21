import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout
)
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setFixedSize(320, 480)
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._create_ui()

    def _create_ui(self):
        main_layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(60)
        self.display.setStyleSheet('font-size: 24px;')
        main_layout.addWidget(self.display)

        grid = QGridLayout()
        buttons = [
            ['C', '+/-', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '0', '.', '=']
        ]

        self.button_map = {}
        for row, row_values in enumerate(buttons):
            for col, btn_text in enumerate(row_values):
                if row == 4 and col == 0:
                    button = QPushButton('0')
                    button.setFixedSize(140, 60)
                    grid.addWidget(button, row, col, 1, 2)
                elif row == 4 and col == 1:
                    continue
                else:
                    button = QPushButton(btn_text)
                    button.setFixedSize(60, 60)
                    grid.addWidget(button, row, col if not (row == 4 and col > 1) else col + 1)
                button.clicked.connect(self._on_button_clicked)
                self.button_map[btn_text] = button
        main_layout.addLayout(grid)
        self._central_widget.setLayout(main_layout)
        self.input_str = ''

    def _on_button_clicked(self):
        sender = self.sender()
        text = sender.text()
        if text in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}:
            self.input_str += text
        elif text in {'+', '-', '*', '/'}:
            if self.input_str and self.input_str[-1] not in '+-*/':
                self.input_str += text
        elif text == 'C':
            self.input_str = ''
        elif text == '+/-':
            if self.input_str and self.input_str[0] == '-':
                self.input_str = self.input_str[1:]
            elif self.input_str:
                self.input_str = '-' + self.input_str
        elif text == '%':
            if self.input_str:
                try:
                    self.input_str = str(float(self.input_str) / 100)
                except Exception:
                    self.input_str = 'Error'
        elif text == '=':
            try:
                self.input_str = str(eval(self.input_str))
            except Exception:
                self.input_str = 'Error'
        self.display.setText(self.input_str)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
