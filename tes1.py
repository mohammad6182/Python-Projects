
import sqlite3
conn= sqlite3.connect('test.db')
with conn:
    cur= conn.cursor()
    cur.execute(" CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_ftype TEXT)")
    conn.commit()

conn= sqlite3.connect('test_db')

#tuples of file types


fileList= ('information.docx', 'hello.text', 'myImage.png', \
           'myMovie.mpg', 'world.txt', 'data.pdf', 'myPhoto.jpg')


for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_ftype) VALUES (?)", (x, ))
            print(x)
conn.close()
