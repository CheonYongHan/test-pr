import sys

from ui import View         # ui.py 의 View 클래스를 import
from ctrl import Control    # ctrl.py 의 Control 클래스를 import
from PyQt5.QtWidgets import QApplication

def main():                 # 프로그램 실행 관련내용 함수화
    calc = QApplication(sys.argv)
    app = QApplication(sys.argv)
    view = View()           # View 클래스의 인스턴스 생성
    Control(view=view)      # Control 클래스의 인스턴스 생성
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    