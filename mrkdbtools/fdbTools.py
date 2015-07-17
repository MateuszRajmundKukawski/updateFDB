import re
import fdb


class DbTool(object):
    
    def __init__(self, dbName):
        self.dbName = dbName
        
    def dbConnection(self):
        
        self.con = fdb.connect(database=self.dbName, user='sysdba', password='masterkey', charset='ISO8859_2')
        self.cur = self.con.cursor()
        
    def execute_select(self, SELECT):
        
        self.cur.execute(SELECT)
        if re.search('^select', SELECT, re.IGNORECASE):
            for row in self.cur:
                print row
        self.con.commit()
        print 'commit'
        
    def executeSqlFile(self, sql_file_name):
            
        with open(sql_file_name) as f:
            sql_query_list = (line.rstrip('\n') for line in f )
            for row in sql_query_list:
                self.execute_select(row)
                
    def close_connection(self):
        
        self.con.close()
        
    

if __name__ == '__main__':
    test_db = '1815035.FDB'
    sqlfile = 'myquery.sql'
    print '*'*10
    x = DbTool(test_db)
    x.dbConnection()
    x.executeSqlFile(sqlfile)
    x.close_connection()

