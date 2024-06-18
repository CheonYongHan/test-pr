from PyQt5.QtWidgets import ( QApplication, QWidget, QPushButton, QVBoxLayout,
                            QMessageBox, QPlainTextEdit, QHBoxLayout, 
                            QLineEdit, QComboBox, QLabel ) 
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore    # 모듈 추가


class View(QWidget) :

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.le1 = QLineEdit('0', self)   # QLineEdit 객체 생성
        self.le1.setAlignment(QtCore.Qt.AlignRight) # 오른쪽 정렬
        self.le1.setFocus(True)
        self.le1.selectAll()    # 텍스트 전체 선택

        self.le2 = QLineEdit('0', self) # QLineEdit 객체 생성
        self.le2.setAlignment(QtCore.Qt.AlignRight) # 오른쪽 정렬

        self.cb = QComboBox(self)   # QComboBox 객체 생성
        # self.cb.addItems(['+', '-', '*', '/', '^', '%'])    # 아이템 추가
        self.cb.addItems(['+', '-', '*', '/' ])

        self.lbl1 = QLabel('R2.3.0', self)  # QLabel 객체 생성
        self.lbl1.setFont(QFont('Consolas', 10))
        self.btn1 = QPushButton('Calc', self)
        self.btn2 = QPushButton('Clear', self)

        hbox_formular = QHBoxLayout()   # 수식을 입력할 수 있는 레이아웃
        hbox_formular.setSpacing(10)
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)

        hbox = QHBoxLayout()
        hbox.setSpacing(10)
        hbox.addStretch(1)
        hbox.addWidget(self.lbl1)   # 버전 정보 표시
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout()
        vbox.setSpacing(10)
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formular)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256, 256)
        self.show()

    def setDisplay(self, text):
        self.te1.appendPlainText(text)

    def clearMessage(self):
        self.te1.clear()
