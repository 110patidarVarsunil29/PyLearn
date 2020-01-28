import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="super",database="Python", port =3307, auth_plugin="caching_sha2_password")
mycursors = mydb.cursor()
mycursors.execute("select * from students")
result = mycursors.fetchall()

for i in result:
    print(i)

for i in result:
    name=i[0]
    college=i[1]
    print(f"Name: {name}; College: {college}")

mydb.close()