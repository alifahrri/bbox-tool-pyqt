from PyQt5 import QtWidgets, QtCore, QtGui
import math

class ImageItem(QtWidgets.QGraphicsItem) :
	def __init__(self, parent = None):
		QtWidgets.QGraphicsItem.__init__(self,parent)
		self.pxmap = QtGui.QPixmap()
		self.bboxes = []
		self.box_start = QtCore.QPointF()
		self.box_end = QtCore.QPointF()
		self.draw_box = False
		self.bbox_list_callback = None
		self.setAcceptHoverEvents(True)
		self.hover_pos = QtCore.QPointF()

	def fromFile(self, str) :
		self.pxmap = QtGui.QPixmap.fromImage(QtGui.QImage(str))
		del self.bboxes[:]
		self.scene().update()

	def paint(self, painter, option, widget = None) :
		w = self.pxmap.size().width()
		h = self.pxmap.size().height()
		pt = QtCore.QPointF(-w/2, -h/2)
		if not self.pxmap.isNull() :
			painter.drawPixmap(pt, self.pxmap)
			x = min(self.hover_pos.x(),w/2)
			x = max(x, -w/2)
			y = min(self.hover_pos.y(),h/2)
			y = max(y, -h/2)
			hover_line_x = QtCore.QLineF(x,-h/2,x,h/2)
			hover_line_y = QtCore.QLineF(-w/2,y,w/2,y)
			painter.setPen(QtGui.QPen(QtGui.QColor(0,0,255)))
			painter.drawLine(hover_line_x)
			painter.drawLine(hover_line_y)
		if(self.draw_box) :
			painter.setPen(QtGui.QPen(QtGui.QColor(255,0,0)))
			painter.drawRect(QtCore.QRectF(self.box_start,self.box_end))
		rects = []
		for box in self.bboxes :
			rect = QtCore.QRectF(box[0],box[1])
			rects.append(rect)
		painter.setPen(QtGui.QPen(QtGui.QColor(0,255,0)))
		painter.drawRects(rects)

	def boundingRect(self) :
		s = self.pxmap.size()
		w = s.width()
		h = s.height()
		o = 300
		rect = QtCore.QRectF(-self.pxmap.size().width()/2-o,-self.pxmap.size().height()/2-o,self.pxmap.size().width()+o*2,self.pxmap.size().height()+o*2)
		# rect = QtCore.QRectF(-w,-h,w*2,h*2)
		# print "size %s, rect %s" %(str(s), str(rect))
		return rect

	def mousePressEvent(self, event) :
		self.box_start = event.pos()
		self.box_end = event.pos()
		self.draw_box = True
		self.scene().update()
		# print "mouse press %s" %str(event.pos())
	
	def mouseMoveEvent(self, event) :
		self.box_end = event.pos()
		self.scene().update()

	def mouseReleaseEvent(self, event) :
		self.draw_box = False
		if(self.box_start != self.box_end) :
			self.bboxes.append((self.box_start, self.box_end))
		if(self.bbox_list_callback != None) :
			self.bbox_list_callback(self.bboxes)
		self.scene().update()

	def hoverMoveEvent(self, event) :
		self.hover_pos = event.pos()
		self.scene().update()
		# print "hover event %s" %str(self.hover_pos)