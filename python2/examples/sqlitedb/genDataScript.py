# Author  : freeman
# Date    : 2019.05.25
# Version : 0.0.1
# Desc    : Program 1
#         : 
###################################################################


import json
import sys
import sqlite3
from sqlite3 import Error


"""
0: Date; 1: Open; 2: High; 3: Low; 4: Close; 5: Volume
"""
def readJson():
    with open('fb.json', 'r') as fi:
        ds = json.load(fi)
    d3 = ds['dataset']['data']
    return d3


def genSQL(ds):
    sqlAll ,sql2, cnt = [], "", 1
    sql1 = '''INSERT INTO FBData(id, fbDate, fbOpen, fbHigh, fbLow, fbClose, fbVolume) VALUES '''
    for i in ds:
        sql2 += sql1 + '( ' + str(cnt) + ',' + '\'' + str(i[0]) + '\'' + ',' +  str(i[1])+ ',' + str(i[2]) + ',' +  str(i[3]) + ',' + str(i[4]) + ',' + str(i[5]) + ');'
        sqlAll.append(sql2)
        sql2=""
        cnt+=1

    #for i in sqlAll:
    #    print i

    return sqlAll


def createDBConn(db_file):
    """ create a database connection """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as err:
        print str(err)

    return None


def createTable(conn, sql):
    """ create a table and populate table
    :param conn: Connection object
    :param sql: Insert statements
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as err:
        print str(err)


def insertData(conn, sqls):
    try:
        c = conn.cursor()
        for sql in sqls:
            c.execute(sql)
        conn.commit()
    except Error as err:
        print str(err)

    return c.lastrowid


def main():
    db = "facebook.db"
    sqlTable = """ CREATE TABLE IF NOT EXISTS FBData (
                                    id integer PRIMARY KEY,
                                    fbDate text NOT NULL,
                                    fbOpen numeric NOT NULL,
                                    fbHigh numeric NOT NULL,
                                    fbLow numeric NOT NULL,
                                    fbClose numeric NOT NULL,
                                    fbVolume numeric NOT NULL
                                    ); """
    conn = createDBConn(db)

    d = readJson()
    sqlData = genSQL(d)
    createTable(conn, sqlTable)
    rid = insertData(conn, sqlData)
    conn.close()
    print str(rid)

if __name__ == "__main__":
    main()
