import os
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



if __name__ == '__main__':
    test_db = '1815035.FDB'
    sqlfile = 'myquery.sql'
    mycon, mycur = connecFirebird(test_db)
    executeSqlFile(sqlfile, mycon, mycur)
