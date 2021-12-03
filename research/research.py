import sys
import string
import random
import time
import pymysql.cursors


def connect(host_address, username, dbname, password):
    con = pymysql.Connection(host=host_address, user=username, database=dbname, password=password)
    return con

def execute(connection, mycursor, execute_quer):
    mycursor.execute(execute_quer)
    connection.commit()

def DB_Init(con):
    query = """CREATE TABLE IF NOT EXISTS research 
    (research_id INT PRIMARY KEY AUTO_INCREMENT, 
    data1 NVARCHAR(64) NOT NULL,
    data2 INT)"""
    mycursor = con.cursor()
    mycursor.execute(query)
    con.commit()

def DB_Drop(con):
    query = "DROP TABLE IF EXISTS DB_for_research.research"
    mycursor = con.cursor()
    mycursor.execute(query)
    con.commit()

def ReturnToTheStartingPoint(con, count, text):
    DB_Drop(con)
    DB_Init(con)
    DB_InitialInsertRows(con, count, text)

def DB_InitialInsertRows(con, count, text):
    query = "INSERT INTO research (data1, data2) VALUES "
    for i in range(count - 1):
        split_begin = random.randint(0, int(len(text) / 2))
        split_end = random.randint(int(len(text) / 2), len(text) - 1)
        query += f"('{text[split_begin:split_end]}', {i+7}), "
    query += f"('{text}', {count+6});"

    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def SearchKeyColumn(con, key):
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    for i in range(1000):
        query = f"SELECT * FROM research WHERE research_id = {random.randint(1, key)};"
        mycursor.execute(query)
        #mycursor.fetchall()
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / (1e6 * 1000)

def SearchNonKeyColumn(con, num):
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    for i in range(100):
        query = f"SELECT * FROM research WHERE data2 = {i + num};"
        mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / (1e6 * 100)

def SearchByMask(con, mask):
    query = f"SELECT * FROM research WHERE data1 LIKE '{mask}';"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def InsertRow(con, text, num):
    query = f"INSERT INTO research (data1, data2) VALUES ('{text}', {num});"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def InsertSomeRows(con, text, num, count):
    query = "INSERT INTO research (data1, data2) VALUES "
    for i in range(count - 1):
        query += f"('{text}', {num}), "
    query += f"('{text}', {num});"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def UpdateByKeyColumn(con, key, text, num):
    query = f"UPDATE research SET data1 = '{text}', data2 = {num} WHERE research_id = {key};"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def UpdateByNumColumn(con, text, num):
    query = f"UPDATE research SET data1 = '{text}' WHERE data2 = {num};"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def DeleteByKeyColumn(con, key):
    query = f"DELETE FROM research WHERE research_id = {key};"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def DeleteByNumColumn(con, num):
    query = f"DELETE FROM research WHERE data2 = {num};"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def DeleteSomeRows(con, count):
    query = f"DELETE FROM research LIMIT {count};"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def Compress(con):
    query = "ALTER TABLE research ROW_FORMAT=COMPRESSED;"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

if __name__ == '__main__':
    con = connect('127.0.0.1', 'root', 'DB_for_research', '87878987')
    number = 62
    text = "theorcscallittheswampofmemorywhereallgloryburiesitsdead"
    mask = "r%"
    key = 2
    rowGroupCount = 200
    for rowCount in [1000, 10000, 100000]:
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Search key column {} rows: {:.4f} ms'.format(rowCount, SearchKeyColumn(con, rowCount)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Search non-key column {} rows: {:.4f} ms'.format(rowCount, SearchNonKeyColumn(con, number)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Search by mask {} rows: {:.4f} ms'.format(rowCount, SearchByMask(con, mask)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Insert one row {} rows: {:.4f} ms'.format(rowCount, InsertRow(con, text, number)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Insert group of rows {} rows: {:.4f} ms'.format(rowCount, InsertSomeRows(con, text, number, rowGroupCount)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Update key column {} rows: {:.4f} ms'.format(rowCount, UpdateByKeyColumn(con, key, text, number)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Update num (non-key) column {} rows: {:.4f} ms'.format(rowCount, UpdateByNumColumn(con, text, number)))
        print('Delete key column {} rows: {:.4f} ms'.format(rowCount, DeleteByKeyColumn(con, key)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Delete num (non-key) column {} rows: {:.4f} ms'.format(rowCount, DeleteByNumColumn(con, number)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Delete group of rows {} rows: {:.4f} ms'.format(rowGroupCount, DeleteSomeRows(con, rowGroupCount)))
        ReturnToTheStartingPoint(con, rowCount, text)
        DeleteSomeRows(con, rowGroupCount)
        print('Compress db after 200 rows deletion {} rows: {} ms'.format(rowCount, Compress(con)))
        ReturnToTheStartingPoint(con, rowGroupCount, text)
        print('Compress db with 200 rows left {} rows: {} ms'.format(rowCount, Compress(con)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print("\n\n")