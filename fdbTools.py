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
    print 'end'



if __name__ == '__main__':
    main()
