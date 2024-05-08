import serial, sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
def dataCable():
    try:
        global s
        s = serial.Serial('/dev/ttyUSB0', 9600)
    except: 
        s = ''
        return False
def getCm():
    try:
        return str(s.readline()).split('\\')[0].split("b'")[1] + " cm"
    except: dataCable()
def update():
    win.label_1.setText(getCm())
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data")
        self.setFixedHeight(200)
        self.setFixedWidth(400)
        self.label_1 = QLabel("", self)
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_1.setFont(QFont('Arial', 80))
        self.label_1.resize(400, 200)
        self.show()
if __name__ == "__main__":
    dataCable()
    app = QApplication([])
    win = Window()
    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(0)
    sys.exit(app.exec_())