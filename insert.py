import sqlite3
conn=sqlite3.connect("MITMidMorning.db")
print("Open database successfully")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(1,'ANTONIA',22,'eMobilis','Female')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(2,'JESSE',19,'eMobilis','male')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(3,'BRAHIM',24,'eMobilis','Female')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(4,'ADRIAN',18,'eMobilis','Them')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(5,'ANTONIA',10,'eMobilis','Female')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(6,'ANTONIA',14,'eMobilis','male')")

conn.commit()
print("Records Successfully added")
conn.close()