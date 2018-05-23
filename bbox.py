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
		self.ui.clear_btn.clicked.connect(self.clear)
		self.ui.zoom_in_btn.clicked.connect(self.zoomIn)
		self.ui.load_btn.clicked.connect(self.readImages)
		self.ui.next_btn.clicked.connect(self.nextImages)
		self.ui.prev_btn.clicked.connect(self.prevImages)
		self.ui.zoom_out_btn.clicked.connect(self.zoomOut)
		self.ui.traint_btn.clicked.connect(self.createTrain)
		self.ui.test_btn.clicked.connect(self.createTest)
		self.ui.load_names_btn.clicked.connect(self.readNames)
		self.ui.class_combo.currentIndexChanged.connect(self.setLabel)
		self.img = imageitem.ImageItem()
		self.scene.addItem(self.img)
		self.scale = 1.0
		self.img.bbox_list_callback = self.printBBoxes
		self.ui.load_btn.setEnabled(False)
		self.files = []
		self.form.setWindowTitle("Bounding Box Tool")

	def createTrain(self) :
		trains = QtWidgets.QFileDialog.getOpenFileNames()[0]
		save = QtWidgets.QFileDialog.getSaveFileName()[0]
		with open(save, 'w+') as f :
			for file in trains :
				f.write(file + '\n')
		# print trains
		# print save

	def createTest(self) :
		tests = QtWidgets.QFileDialog.getOpenFileNames()[0]
		save = QtWidgets.QFileDialog.getSaveFileName()[0]
		with open(save, 'w+') as f :
			for file in tests :
				f.write(file + '\n')
		# print tests
		# print save

	def clear(self) :
		self.ui.bbox_text_edit.clear()
		self.img.clearAll()

	def printBBoxes(self, bboxes) :
		self.ui.bbox_text_edit.clear()
		for b in bboxes :
			s = "%s, %s, %s, %s" %(b[0].x(), b[0].y(), b[1].x(), b[1].y())
			self.ui.bbox_text_edit.append(s + '\n')
		str = self.annotateBoxes(bboxes)
		for s in str :
			self.ui.bbox_text_edit.append(s + '\n')
	
	def setLabel(self) :
		idx = self.ui.class_combo.currentIndex()
		str = self.ui.class_combo.currentText()
		print 'set label (%s,%s)'%(idx,str)
		self.img.setClass((idx, str))
	
	def readNames(self) :
		self.names_file = QtWidgets.QFileDialog.getOpenFileName()
		print self.names_file
		self.ui.names_line_edit.setText(self.names_file[0])
		with open(self.names_file[0]) as f :
			for line in f :
				label = line.rstrip()
				print label
				self.ui.class_combo.addItem(label)
				self.img.label_list.append(label)
		self.ui.load_btn.setEnabled(True)

	def readImages(self) :
		self.path = QtWidgets.QFileDialog.getExistingDirectory()
		# self.files = os.listdir(self.path)
		files = os.listdir(self.path)
		for f in files :
			file, ext = os.path.splitext(f)
			print ext
			if ext == '.jpg' or ext == '.jpeg' :
				self.files.append(f)
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
		self.saveAnnotation(self.path, self.img.bboxes)
		self.current_idx = self.current_idx + 1
		if(self.current_idx >= len(self.files)) :
			self.current_idx = 0
		self.showImages(self.current_idx)

	def loadAnnotation(self, path) :
		filename, ext = os.path.splitext(path + '/' + self.files[self.current_idx])
		path_txt = filename + '.txt'
		if os.path.isfile(path_txt) :
			print 'annotation file %s exists' %(path_txt)
			with open(path_txt) as f :
				for l in f:
					print l
					self.ui.bbox_text_edit.append(l+'\n')
					self.img.bboxFromString(l)
		else :
			print 'annotation file %s does not exist' %(path_txt)

	def saveAnnotation(self, path, bboxes) :
		filename, ext = os.path.splitext(path + '/' + self.files[self.current_idx])
		path_txt = filename + '.txt'
		txt = open(path_txt, 'w+')
		idx = self.ui.class_combo.currentIndex()
		str = self.annotateBoxes(bboxes)
		for s in str :
			txt.write(s + '\n')
		print 'save to : %s' %(path_txt) 

	def showImages(self, idx) :
		self.ui.bbox_text_edit.clear()
		filename = self.path+'/'+self.files[idx]
		print "opening : %s" %filename
		self.img.fromFile(filename)
		self.ui.cur_img_label.setText(str(self.current_idx)+" / "+str(len(self.files)))
		self.loadAnnotation(self.path)

	def zoomIn(self) :
		self.ui.graphicsView.scale(1.1,1.1)
		self.scale *= 1.1

	def zoomOut(self) :
		self.ui.graphicsView.scale(0.9,0.9)
		self.scale *= 0.9
	
	def annotateBoxes(self, bboxes):
		yolo_str = []
		for b in bboxes :
			w = self.img.pxmap.width()
			h = self.img.pxmap.height()
			size = (w, h)
			box = (b[0].x() + w/2, b[0].y() + h/2, b[1].x() + w/2, b[1].y() + h/2)
			a = self.annotate(size,box)
			label = b[2][0]
			yolo_str.append("%s %s %s %s %s" %(label, a[0], a[1], a[2], a[3]))
		return yolo_str
	
	def annotate(self, size, box) :
		dw = 1.0 / size[0]
		dh = 1.0 / size[1]
		x = (box[0] + box[2]) / 2.0
		y = (box[1] + box[3]) / 2.0
		w = box[2] - box[0]
		h = box[3] - box[1]
		x *= dw
		w *= dw
		y *= dh
		h *= dh
		return (x,y,w,h)

	def show(self) :
		self.form.show()