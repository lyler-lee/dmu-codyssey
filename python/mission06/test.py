import sys 
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)  # QApplication  객체 생성
  
win = QWidget()              # window 생성
win.show()                   # 창을 띄우는 역할

app.exec_()                  # 이벤트 루프 실행
