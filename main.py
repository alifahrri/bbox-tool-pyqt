import bbox
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

if __name__ == '__main__' :
	print 'hello!'
	app = QtWidgets.QApplication(sys.argv)
	box = bbox.BBOXWidget()
	box.show()
	r = app.exec_()
	print 'done!'
	sys.exit(r)