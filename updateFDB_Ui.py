# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateFDB.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_UpdateDatabase(object):
    def setupUi(self, UpdateDatabase):
        UpdateDatabase.setObjectName(_fromUtf8("UpdateDatabase"))
        UpdateDatabase.resize(251, 324)
        self.verticalLayoutWidget = QtGui.QWidget(UpdateDatabase)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 231, 271))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.setDatabse_Button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.setDatabse_Button.setObjectName(_fromUtf8("setDatabse_Button"))
        self.verticalLayout.addWidget(self.setDatabse_Button)
        self.database_name_Label = QtGui.QLabel(self.verticalLayoutWidget)
        self.database_name_Label.setObjectName(_fromUtf8("database_name_Label"))
        self.verticalLayout.addWidget(self.database_name_Label)
        self.select_text_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.select_text_edit.setObjectName(_fromUtf8("select_text_edit"))
        self.verticalLayout.addWidget(self.select_text_edit)
        self.testSelectButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.testSelectButton.setObjectName(_fromUtf8("testSelectButton"))
        self.verticalLayout.addWidget(self.testSelectButton)
        self.selectLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.selectLabel.setObjectName(_fromUtf8("selectLabel"))
        self.verticalLayout.addWidget(self.selectLabel)
        self.sqlFileButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.sqlFileButton.setObjectName(_fromUtf8("sqlFileButton"))
        self.verticalLayout.addWidget(self.sqlFileButton)
        self.sqlFileLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.sqlFileLabel.setObjectName(_fromUtf8("sqlFileLabel"))
        self.verticalLayout.addWidget(self.sqlFileLabel)
        self.r1 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.r1.setObjectName(_fromUtf8("r1"))
        self.verticalLayout.addWidget(self.r1)
        self.r2 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.r2.setObjectName(_fromUtf8("r2"))
        self.verticalLayout.addWidget(self.r2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.runButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.verticalLayout.addWidget(self.runButton)

        self.retranslateUi(UpdateDatabase)
        QtCore.QMetaObject.connectSlotsByName(UpdateDatabase)

    def retranslateUi(self, UpdateDatabase):
        UpdateDatabase.setWindowTitle(_translate("UpdateDatabase", "Dialog", None))
        self.label.setText(_translate("UpdateDatabase", "Updaet Firebird Database", None))
        self.setDatabse_Button.setText(_translate("UpdateDatabase", "setDatabase", None))
        self.database_name_Label.setText(_translate("UpdateDatabase", "DataBase Name: ", None))
        self.testSelectButton.setText(_translate("UpdateDatabase", "testQuery", None))
        self.selectLabel.setText(_translate("UpdateDatabase", "...", None))
        self.sqlFileButton.setText(_translate("UpdateDatabase", "sqlFile", None))
        self.sqlFileLabel.setText(_translate("UpdateDatabase", "sqlFile name: ", None))
        self.r1.setText(_translate("UpdateDatabase", "query", None))
        self.r2.setText(_translate("UpdateDatabase", "select", None))
        self.runButton.setText(_translate("UpdateDatabase", "RUN", None))

