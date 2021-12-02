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
    query = """CREATE TABLE IF NOT EXISTS maintable 
    (maintable_id INT PRIMARY KEY AUTO_INCREMENT, 
    data1 NVARCHAR(64) NOT NULL,
    data2 INT)"""
    mycursor = con.cursor()
    mycursor.execute(query)
    con.commit()

def DB_Drop(con):
    query = "DROP TABLE IF EXISTS DB_for_research.maintable"
    mycursor = con.cursor()
    mycursor.execute(query)
    con.commit()

def ReturnToTheStartingPoint(con, count, text):
    DB_Drop(con)
    DB_Init(con)
    db_initial_insert_rows(con, count, text)

def db_initial_insert_rows(con, count, text):
    query = "INSERT INTO maintable (data1, data2) VALUES "
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

def db_search_key_column(con, key):
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    for i in range(1000):
        query = f"SELECT * FROM maintable WHERE maintable_id = {random.randint(1, key)};"
        mycursor.execute(query)
        #mycursor.fetchall()
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / (1e6 * 1000)

def db_search_nonkey_column(con, num):
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    for i in range(100):
        query = f"SELECT * FROM maintable WHERE data2 = {i + num};"
        mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / (1e6 * 100)

def db_search_by_mask(con, mask):
    query = f"SELECT * FROM maintable WHERE data1 LIKE '{mask}';"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def db_insert_row(con, text, num):
    query = f"INSERT INTO maintable (data1, data2) VALUES ('{text}', {num});"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def db_insert_some_rows(con, text, num, count):
    query = "INSERT INTO maintable (data1, data2) VALUES "
    for i in range(count - 1):
        query += f"('{text}', {num}), "
    query += f"('{text}', {num});"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def db_update_by_key_column(con, key, text, num):
    query = f"UPDATE maintable SET data1 = '{text}', data2 = {num} WHERE maintable_id = {key};"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def db_update_by_num_column(con, text, num):
    query = f"UPDATE maintable SET data1 = '{text}' WHERE data2 = {num};"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def db_delete_by_key_column(con, key):
    query = f"DELETE FROM maintable WHERE maintable_id = {key};"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def db_delete_by_num_column(con, num):
    query = f"DELETE FROM maintable WHERE data2 = {num};"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def db_delete_some_rows(con, count):
    query = f"DELETE FROM maintable LIMIT {count};"
    mycursor = con.cursor()
    start = time.perf_counter_ns()
    mycursor.execute(query)
    end = time.perf_counter_ns()
    con.commit()
    return (end - start) / 1e6

def db_compress(con):
    query = "ALTER TABLE maintable ROW_FORMAT=COMPRESSED;"
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
        print('Search key column {} rows: {:.4f} ms'.format(rowCount, db_search_key_column(con, rowCount)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Search non-key column {} rows: {:.4f} ms'.format(rowCount, db_search_nonkey_column(con, number)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Search by mask {} rows: {:.4f} ms'.format(rowCount, db_search_by_mask(con, mask)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Insert one row {} rows: {:.4f} ms'.format(rowCount, db_insert_row(con, text, number)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Insert group of rows {} rows: {:.4f} ms'.format(rowCount, db_insert_some_rows(con, text, number, rowGroupCount)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Update key column {} rows: {:.4f} ms'.format(rowCount, db_update_by_key_column(con, key, text, number)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Update num (non-key) column {} rows: {:.4f} ms'.format(rowCount, db_update_by_num_column(con, text, number)))
        print('Delete key column {} rows: {:.4f} ms'.format(rowCount, db_delete_by_key_column(con, key)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Delete num (non-key) column {} rows: {:.4f} ms'.format(rowCount, db_delete_by_num_column(con, number)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print('Delete group of rows {} rows: {:.4f} ms'.format(rowGroupCount, db_delete_some_rows(con, rowGroupCount)))
        ReturnToTheStartingPoint(con, rowCount, text)
        db_delete_some_rows(con, rowGroupCount)
        print('Compress db after 200 rows deletion {} rows: {} ms'.format(rowCount, db_compress(con)))
        ReturnToTheStartingPoint(con, rowGroupCount, text)
        print('Compress db with 200 rows left {} rows: {} ms'.format(rowCount, db_compress(con)))
        ReturnToTheStartingPoint(con, rowCount, text)
        print("\n\n")