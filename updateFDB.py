import sys, os
from PyQt4 import QtCore, QtGui

from updateFDB_Ui import Ui_UpdateDatabase
import fdbTools  as fdbt
from PyQt4.Qt import QString

class MyApp(QtGui.QMainWindow):

    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_UpdateDatabase()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.setDatabse_Button, QtCore.SIGNAL('clicked()'), self.getFileName)
        QtCore.QObject.connect(self.ui.testSelectButton, QtCore.SIGNAL('clicked()'), self.validSelect)
        QtCore.QObject.connect(self.ui.runButton, QtCore.SIGNAL('clicked()'), self.runUpdate)


    def getFileName(self):

        self.full_file_path = QtGui.QFileDialog.getOpenFileName(self, 'Open DataBase', 'E:/', '*.fdb', )
        file_base_name = os.path.basename(str(self.full_file_path))
        self.ui.database_name_Label.setText('DataBase: '+file_base_name)

    def validSelect(self):

        self.SELECT = self.ui.select_text_edit.text()
        self.ui.selectLabel.setText(self.SELECT)

    def runUpdate(self):

        fdbcon, fdbcur = fdbt.connecFirebird(str(self.full_file_path))
        fdbt.execute_select(str(self.SELECT), fdbcon, fdbcur )



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())