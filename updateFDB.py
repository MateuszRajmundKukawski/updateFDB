import sys, os
from PyQt4 import QtCore, QtGui

from updateFDB_Ui import Ui_UpdateDatabase
import fdbTools  as fdbt


class MyApp(QtGui.QMainWindow):

    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_UpdateDatabase()
        self.ui.setupUi(self)
        self.my_init()
        
    def my_init(self):
        self.sql_file_name = None
        QtCore.QObject.connect(self.ui.setDatabse_Button, QtCore.SIGNAL('clicked()'), self.getDBFileName)
        QtCore.QObject.connect(self.ui.testSelectButton, QtCore.SIGNAL('clicked()'), self.validSelect)
        QtCore.QObject.connect(self.ui.runButton, QtCore.SIGNAL('clicked()'), self.runUpdate)
        QtCore.QObject.connect(self.ui.sqlFileButton, QtCore.SIGNAL('clicked()'), self.getSqlFileName)
        
        self.ui.r1.setChecked(True)

        
    def getDBFileName(self):

        self.full_file_db_path = QtGui.QFileDialog.getOpenFileName(self, 'Open DataBase', 'E:/', '*.fdb', )
        file_base_name = os.path.basename(str(self.full_file_db_path))
        old_lebel_text =  self.ui.database_name_Label.text()
        self.ui.database_name_Label.setText(old_lebel_text+file_base_name)
        
    def getSqlFileName(self):
        self.full_file_sql_path = QtGui.QFileDialog.getOpenFileName(self, 'Open SqlFile', 'E:/', '*.sql', )
        file_sql_base_name = os.path.basename(str(self.full_file_sql_path))
        old_lebel_text =  self.ui.sqlFileLabel.text()
        self.ui.sqlFileLabel.setText(old_lebel_text+file_sql_base_name)

    def validSelect(self):

        self.SELECT = self.ui.select_text_edit.text()
        self.ui.selectLabel.setText(self.SELECT)
        print self.ui.r1.isChecked()

    def runUpdate(self):
        fdbcon, fdbcur = fdbt.connecFirebird(str(self.full_file_db_path))
        if self.ui.r1.isChecked():            
            fdbt.execute_select(str(self.SELECT), fdbcon, fdbcur )
        else:
            fdbt.executeSqlFile(str(self.full_file_sql_path), fdbcon, fdbcur)
        fdbt.close_conn(fdbcon)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())