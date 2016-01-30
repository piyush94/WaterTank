__author__ = 'Piyush Sohal, Prince Dogra'

from PyQt4 import QtGui, QtCore
import sys
import time

class Tank(QtGui.QWidget):

    def __init__(self):
        super(Tank, self).__init__()
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("WATER-TANK")
        self.setWindowIcon(QtGui.QIcon('ChitkaraLogoBig.png'))
        #self.statusBar().showMessage("WATER-TANK")
        self.initUI()

    def initUI(self):
        btn = QtGui.QPushButton('FILL', self)
        btn.move(50, 570)

        lbl = QtGui.QLabel('%age :', self)
        lbl.move(50,635)

        self.entry = QtGui.QTextEdit(self)
        self.entry.move(100, 630)
        self.entry.resize(100, 30)

        self.limit = 396

        canvas = QtGui.QGraphicsView(self)
        self.scene = QtGui.QGraphicsScene(self)
        canvas.setScene(self.scene)
        canvas.move(890, 40)
        canvas.resize(400, 592)

        tank = QtGui.QLabel(self)
        pixel = QtGui.QPixmap("tank_meter.png")
        tank.setPixmap(pixel)
        tank.move(820,40)
        tankHeight = pixel.height()
        tankWidth = pixel.width()

        actualHeightLabel = QtGui.QLabel("Total Height  : ",self)
        actualHeightLabel.resize(400,150)
        actualHeightLabel.setStyleSheet('font-family: Times New Roman, serif; font-size: 30px;font-weight: 700;')
        actualHeightLabel.move(50,90)

        actualHeightValue = QtGui.QLabel("1.2 Meter ",self)
        actualHeightValue.resize(400,150)
        actualHeightValue.setStyleSheet('font-family: Times New Roman, serif; font-size: 30px;font-weight: 700;')
        actualHeightValue.move(250,90)

        actualVolumeLabel = QtGui.QLabel("Total Volume : ",self)
        actualVolumeLabel.resize(400,150)
        actualVolumeLabel.setStyleSheet('font-family: Times New Roman, serif; font-size: 30px;font-weight: 700;')
        actualVolumeLabel.move(50, 160)

        totalStorageCapacity = QtGui.QLabel("Total Storage Capacity                :",self)
        totalStorageCapacity.resize(600,150)
        totalStorageCapacity.setStyleSheet('font-family: Times New Roman, serif; font-size: 30px;font-weight: 700;')
        totalStorageCapacity.move(50, 240)

        totalStorageCapacitysmall = QtGui.QLabel("(in gallons)",self)
        totalStorageCapacitysmall.resize(200,150)
        totalStorageCapacitysmall.setStyleSheet('font-family: Times New Roman, serif; font-size: 25px;font-weight: 200;')
        totalStorageCapacitysmall.move(350, 240)

        totalStorageCapacityValue = QtGui.QLabel("12k",self)
        totalStorageCapacityValue.resize(400,150)
        totalStorageCapacityValue.setStyleSheet('font-family: Times New Roman, serif; font-size: 30px;font-weight: 700;')
        totalStorageCapacityValue.move(500, 240)

        waterInTank = QtGui.QLabel("Water in Tank : ",self)
        waterInTank.resize(400,150)
        waterInTank.setStyleSheet('font-family: Times New Roman, serif; font-size: 30px;font-weight: 700;')
        waterInTank.move(50, 320)

        g_brush = QtGui.QBrush(QtGui.QColor(0,204,255))
        self.item = QtGui.QGraphicsRectItem(0, 0, 397, 1)           #Main Rect
        self.item2 = QtGui.QGraphicsRectItem(0, -588, 397, 0)       #Limit Rect
        self.item.setBrush(g_brush)
        self.scene.addItem(self.item)
        self.scene.addItem(self.item2)

        self.tl = QtCore.QTimeLine(500)
        self.tl.setFrameRange(0, 500)
        self.a = QtGui.QGraphicsItemAnimation()
        self.a.setItem(self.item)
        self.a.setTimeLine(self.tl)

        btn.clicked.connect(self.drawrec)

        self.show()

    def drawrec(self):
        fill = int(self.entry.toPlainText())
        if 0 < fill <= 100:
            fill = int((588/100)*fill)
            print(fill)
            self.a.setScaleAt(0.5, 1, -fill)
            self.tl.start()
            print(self.tl.state())
        else:
            print('limit exceeded')


def main():
    app = QtGui.QApplication(sys.argv)
    window = Tank()
    sys.exit(app.exec_())


main()
