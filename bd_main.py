import sys
import pymysql.cursors


def connect():
    con = pymysql.Connection(host='127.0.0.1', user='root', database='OneMoreDataBase', password='87878987')
    return con

def execute(connection, mycursor, execute_quer):
    mycursor.execute(execute_quer)
    connection.commit()