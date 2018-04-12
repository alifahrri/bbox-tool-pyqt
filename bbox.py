import bbox_widget
import imageitem
import os
from PyQt5 import QtWidgets, QtCore, QtGui

class BBOXWidget(object):
	def __init__(self, *args, **kwargs):
		self.ui = bbox_widget.Ui_Form()
		self.form = QtWidgets.QWidget()
		self.ui.setupUi(self.form)
		self.scene = QtWidgets.QGraphicsScene(-300.0,-300.0,600.0,600.0)
		self.current_idx = 0
		self.ui.graphicsView.setScene(self.scene)
		self.ui.load_btn.clicked.connect(self.readImages)
		self.ui.next_btn.clicked.connect(self.nextImages)
		self.ui.prev_btn.clicked.connect(self.prevImages)
		self.ui.zoom_in_btn.clicked.connect(self.zoomIn)
		self.ui.zoom_out_btn.clicked.connect(self.zoomOut)
		self.img = imageitem.ImageItem()
		self.scene.addItem(self.img)
		self.scale = 1.0
		self.img.bbox_list_callback = self.printBBoxes
		self.form.setWindowTitle("Bounding Box Tool")

	def printBBoxes(self, bboxes) :
		self.ui.bbox_text_edit.clear()
		for b in bboxes :
			s = "%s, %s, %s, %s" %(b[0].x(), b[0].y(), b[1].x(), b[1].y())
			self.ui.bbox_text_edit.append(s)

	def readImages(self) :
		self.path = QtWidgets.QFileDialog.getExistingDirectory()
		self.files = os.listdir(self.path)
		self.current_idx = 0
		self.ui.dir_line_edit.setText(self.path)
		print("read images : %s" % self.path)
		print("files: %s" % len(self.files))
		print self.files
		self.showImages(self.current_idx)

	def prevImages(self) :
		self.current_idx = self.current_idx - 1
		if(self.current_idx < 0) :
			self.current_idx = len(self.files) - 1
		self.showImages(self.current_idx)

	def nextImages(self) :
		self.current_idx = self.current_idx + 1
		if(self.current_idx >= len(self.files)) :
			self.current_idx = 0
		self.showImages(self.current_idx)

	def showImages(self, idx) :
		self.ui.bbox_text_edit.clear()
		path = self.path+'/'+self.files[idx]
		print "opening : %s" %path
		self.img.fromFile(path)
		self.ui.cur_img_label.setText(str(self.current_idx)+" / "+str(len(self.files)))

	def zoomIn(self) :
		self.ui.graphicsView.scale(1.1,1.1)
		self.scale *= 1.1

	def zoomOut(self) :
		self.ui.graphicsView.scale(0.9,0.9)
		self.scale *= 0.9

	def show(self) :
		self.form.show()