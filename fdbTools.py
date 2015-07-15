import re
import fdb


def connecFirebird(dbase):
    ''' return connection and curosr

    must use two variables to get this values'''

    con = fdb.connect(database=dbase, user='sysdba', password='masterkey', charset='ISO8859_2')
    cur = con.cursor()
    return con, cur

def execute_select(SELECT, con, cur):

    cur.execute(SELECT)
    if re.search('^select', SELECT, re.IGNORECASE):
        for row in cur:
            print row
    con.commit()
    print 'commit'
    
def executeSqlFile(sql_file_name, con, cur):
    
    with open(sql_file_name) as f:
        sql_query_list = (line.rstrip('\n') for line in f )
        for row in sql_query_list:
            execute_select(row, con, cur)

def close_conn(con):
    con.close()



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
    mycon, mycur = connecFirebird(test_db)
    executeSqlFile(sqlfile, mycon, mycur)
    close_conn(mycon)


