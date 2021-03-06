try:
	from PyQt4 import QtCore, QtGui
except:
	from PySide import QtCore, QtGui

class DigitalClock(QtGui.QLCDNumber):
    def __init__(self):
        super(DigitalClock, self).__init__()
        self.setMouseTracking(True)
        self.setStyleSheet("background:rgb(255,255,255);color:blue;font-size:13px;font-family:Andalus;")
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.3)
        quitAction = QtGui.QAction("Exit", self, shortcut="Ctrl+Q",triggered=QtGui.qApp.quit)
        self.move(800,100)
        self.addAction(quitAction)
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.resize(130,60)
        self.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.setWindowFlags(QtCore.Qt.Drawer | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.showTime()
        self.setWindowTitle("Digital Clock")
    def enterEvent(self,event):
        self.setWindowOpacity(0.9)
    def leaveEvent(self,event):
        self.setWindowOpacity(0.6)
            
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def showTime(self):
        time = QtCore.QTime.currentTime()
        DataTime = QtCore.QDateTime.currentDateTime ()
        if time.toString("hh") > "12":
            h = str(int(time.toString("hh")) - 12)
            text = time.toString('m')
            text = ("0"+h+":"+text)
        else:
            text = time.toString('hh:mm')
            self.setToolTip("<h1>"+DataTime.toString("yyyy/dd/MM")+"</h1>")

        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]
        self.display(text)



if __name__ == '__main__':
    app = QtGui.QApplication([])
    clock = DigitalClock()
    app.installEventFilter(clock)
    clock.show()
    sys.exit(app.exec_())
