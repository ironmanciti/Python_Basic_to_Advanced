import sqlite3
con = sqlite3.connect('test.sqlite')
try:        
    cur = con.cursor()
    cur.execute(" DROP TABLE IF EXISTS student")
    cur.execute('''CREATE TABLE student (
                        StudentID CHAR(2),
                        name TEXT (20) NOT NULL,
                        age INTEGER,
                        marks REAL);''')
    print ('table created successfully')
except Exception as e:
    print ('error in operation, ', e)

cur = con.cursor()

sql = "insert into student (StudentID, name, age, marks) values(?,?,?,?);"
students=[('A1', '홍길동', 20, 70), ('A2', '유병길', 16, 80), ('A3', '김길수', 29, 90)]
cur.executemany(sql, students)

sql = "select * from student"
cur.execute(sql)
print(cur.fetchall())

sql = "insert into student (StudentID, name, age, marks) values('A4', '박재만', 25, 86)"
cur.execute(sql)

sql = "update student set age=59 where StudentID = 'A3'"
cur.execute(sql)

sql = "select * from student"
cur.execute(sql)
print(cur.fetchall())

con.commit()
con.close()