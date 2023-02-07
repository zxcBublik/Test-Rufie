# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *
from second_win import *
class MainWin(QWidget):

    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.set_WindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.btn_next = QPushButton(txt_next, self)
        self.hello.text = QLabel(txt_hello)
        self.instruction = Qlabel(txt_instruction)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, aligment = QtAligLeft)
        self.layout_line.addWidget(self.instruction, aligment = QtAligLeft)
        self.layout_line.addWidget(self.btn_next, aligment = QtAligment)
        self.setLayout(self.layout_line)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def next_click(self):
        self.tw = TestWin()
        self.hide()
 