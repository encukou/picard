# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/metadata.ui'
#
# Created: Thu Sep 15 13:39:09 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(380, 143)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setTitle(_fromUtf8(""))
        self.vboxlayout = QtGui.QVBoxLayout(Form)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setHorizontalSpacing(2)
        self.gridlayout.setVerticalSpacing(3)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.title = QtGui.QLineEdit(Form)
        self.title.setObjectName(_fromUtf8("title"))
        self.gridlayout.addWidget(self.title, 0, 1, 1, 9)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.artist = QtGui.QLineEdit(Form)
        self.artist.setObjectName(_fromUtf8("artist"))
        self.gridlayout.addWidget(self.artist, 1, 1, 1, 9)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.album = QtGui.QLineEdit(Form)
        self.album.setObjectName(_fromUtf8("album"))
        self.gridlayout.addWidget(self.album, 2, 1, 1, 9)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridlayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.tracknumber = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tracknumber.sizePolicy().hasHeightForWidth())
        self.tracknumber.setSizePolicy(sizePolicy)
        self.tracknumber.setMinimumSize(QtCore.QSize(25, 0))
        self.tracknumber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tracknumber.setObjectName(_fromUtf8("tracknumber"))
        self.gridlayout.addWidget(self.tracknumber, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridlayout.addWidget(self.label_5, 3, 3, 1, 1)
        self.length = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy)
        self.length.setMinimumSize(QtCore.QSize(35, 0))
        self.length.setInputMask(_fromUtf8(""))
        self.length.setAlignment(QtCore.Qt.AlignCenter)
        self.length.setReadOnly(True)
        self.length.setObjectName(_fromUtf8("length"))
        self.gridlayout.addWidget(self.length, 3, 4, 1, 1)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridlayout.addWidget(self.label_6, 3, 6, 1, 1)
        self.date = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date.sizePolicy().hasHeightForWidth())
        self.date.setSizePolicy(sizePolicy)
        self.date.setMinimumSize(QtCore.QSize(65, 0))
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setObjectName(_fromUtf8("date"))
        self.gridlayout.addWidget(self.date, 3, 7, 1, 1)
        spacerItem = QtGui.QSpacerItem(4, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 3, 8, 1, 1)
        self.lookup = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lookup.sizePolicy().hasHeightForWidth())
        self.lookup.setSizePolicy(sizePolicy)
        self.lookup.setMinimumSize(QtCore.QSize(75, 0))
        self.lookup.setObjectName(_fromUtf8("lookup"))
        self.gridlayout.addWidget(self.lookup, 3, 9, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(4, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem1, 3, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(4, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem2, 3, 5, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        spacerItem3 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem3)
        self.label.setBuddy(self.title)
        self.label_2.setBuddy(self.artist)
        self.label_3.setBuddy(self.album)
        self.label_4.setBuddy(self.tracknumber)
        self.label_5.setBuddy(self.length)
        self.label_6.setBuddy(self.date)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.title, self.artist)
        Form.setTabOrder(self.artist, self.album)
        Form.setTabOrder(self.album, self.tracknumber)
        Form.setTabOrder(self.tracknumber, self.length)
        Form.setTabOrder(self.length, self.date)
        Form.setTabOrder(self.date, self.lookup)

    def retranslateUi(self, Form):
        self.label.setText(_("Title:"))
        self.label_2.setText(_("Artist:"))
        self.label_3.setText(_("Album:"))
        self.label_4.setText(_("Track:"))
        self.label_5.setText(_("Length:"))
        self.label_6.setText(_("Date:"))
        self.date.setInputMask(_("0000-00-00; "))
        self.lookup.setText(_("Lookup"))

