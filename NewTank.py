__author__ = 'piyush'

from PyQt4 import QtGui, QtCore
import sys
import time

class Tank(QtGui.QWidget):

    def __init__(self):
        super(Tank, self).__init__()
        self.resize(800, 600)
        self.initUI()

    def initUI(self):
        btn = QtGui.QPushButton('FILL', self)
        btn.move(10, 10)

        lbl = QtGui.QLabel('%age :', self)
        lbl.move(10,55)

        self.entry = QtGui.QTextEdit(self)
        self.entry.move(60, 50)
        self.entry.resize(100, 30)

        self.limit = 396

        canvas = QtGui.QGraphicsView(self)
        self.scene = QtGui.QGraphicsScene(self)
        canvas.setScene(self.scene)
        canvas.move(200, 10)
        canvas.resize(300, 400)

        g_brush = QtGui.QBrush(QtGui.QColor("green"))
        self.item = QtGui.QGraphicsRectItem(0, 0, 297, 1)           #Main Rect
        self.item2 = QtGui.QGraphicsRectItem(0, -396, 297, 0)       #Limit Rect
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
        fill = int((396/100)*fill)
        print(fill)
        self.a.setScaleAt(1, 1, -fill)
        self.tl.start()
        print(self.tl.state())


def main():
    app = QtGui.QApplication(sys.argv)
    window = Tank()
    sys.exit(app.exec_())


main()
