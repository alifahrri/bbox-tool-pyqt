# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbox_widget.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(880, 720)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.dir_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dir_label.sizePolicy().hasHeightForWidth())
        self.dir_label.setSizePolicy(sizePolicy)
        self.dir_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.dir_label.setObjectName("dir_label")
        self.gridLayout_3.addWidget(self.dir_label, 0, 0, 1, 1)
        self.dir_line_edit = QtWidgets.QLineEdit(Form)
        self.dir_line_edit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.dir_line_edit.setObjectName("dir_line_edit")
        self.gridLayout_3.addWidget(self.dir_line_edit, 0, 1, 1, 1)
        self.load_btn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_btn.sizePolicy().hasHeightForWidth())
        self.load_btn.setSizePolicy(sizePolicy)
        self.load_btn.setMaximumSize(QtCore.QSize(16777215, 25))
        self.load_btn.setObjectName("load_btn")
        self.gridLayout_3.addWidget(self.load_btn, 0, 2, 1, 1)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.images_group_box = QtWidgets.QGroupBox(self.splitter)
        self.images_group_box.setObjectName("images_group_box")
        self.gridLayout = QtWidgets.QGridLayout(self.images_group_box)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.zoom_out_btn = QtWidgets.QPushButton(self.images_group_box)
        self.zoom_out_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.zoom_out_btn.setWhatsThis("")
        self.zoom_out_btn.setObjectName("zoom_out_btn")
        self.horizontalLayout_2.addWidget(self.zoom_out_btn)
        self.zoom_in_btn = QtWidgets.QPushButton(self.images_group_box)
        self.zoom_in_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.zoom_in_btn.setWhatsThis("")
        self.zoom_in_btn.setObjectName("zoom_in_btn")
        self.horizontalLayout_2.addWidget(self.zoom_in_btn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.prev_btn = QtWidgets.QPushButton(self.images_group_box)
        self.prev_btn.setObjectName("prev_btn")
        self.gridLayout.addWidget(self.prev_btn, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(113, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.cur_img_label = QtWidgets.QLabel(self.images_group_box)
        self.cur_img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cur_img_label.setObjectName("cur_img_label")
        self.gridLayout.addWidget(self.cur_img_label, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(113, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        self.next_btn = QtWidgets.QPushButton(self.images_group_box)
        self.next_btn.setObjectName("next_btn")
        self.gridLayout.addWidget(self.next_btn, 2, 4, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.images_group_box)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 5)
        self.bbox_groupbox = QtWidgets.QGroupBox(self.splitter)
        self.bbox_groupbox.setObjectName("bbox_groupbox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.bbox_groupbox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.bbox_text_edit = QtWidgets.QTextEdit(self.bbox_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bbox_text_edit.sizePolicy().hasHeightForWidth())
        self.bbox_text_edit.setSizePolicy(sizePolicy)
        self.bbox_text_edit.setObjectName("bbox_text_edit")
        self.gridLayout_2.addWidget(self.bbox_text_edit, 0, 0, 1, 1)
        self.delete_btn = QtWidgets.QPushButton(self.bbox_groupbox)
        self.delete_btn.setObjectName("delete_btn")
        self.gridLayout_2.addWidget(self.delete_btn, 1, 0, 1, 1)
        self.clear_btn = QtWidgets.QPushButton(self.bbox_groupbox)
        self.clear_btn.setObjectName("clear_btn")
        self.gridLayout_2.addWidget(self.clear_btn, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.splitter, 1, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.dir_label.setText(_translate("Form", "Dir : "))
        self.load_btn.setText(_translate("Form", "Load"))
        self.images_group_box.setTitle(_translate("Form", "Images :"))
        self.zoom_out_btn.setText(_translate("Form", "-"))
        self.zoom_in_btn.setText(_translate("Form", "+"))
        self.prev_btn.setText(_translate("Form", "Prev"))
        self.cur_img_label.setText(_translate("Form", "0 / 0"))
        self.next_btn.setText(_translate("Form", "Next"))
        self.bbox_groupbox.setTitle(_translate("Form", "Bounding Boxes :"))
        self.delete_btn.setText(_translate("Form", "Delete"))
        self.clear_btn.setText(_translate("Form", "Clear All"))

