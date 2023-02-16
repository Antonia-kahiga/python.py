import sqlite3
conn=sqlite3.connect("MITMidMorning.db")
print("Open database successfully")
data=conn.execute("select * from Wanafunzi")
for row in data:
    print("ID",row[0])
    print("Name",row[1])
    print("Age",row[2])
    print("School",row[3])
    print("Gender",row[4])
conn.close()