import mysql.connector
con = mysql.connector.Connect(host="localhost", user="root", password="", database="usermanagement")
con.autocommit(True)
cur = con.cursor()
db = cur.execute("SELECT * FROM tblusers WHERE username = 'Rolf';")
data = cur.fetchall()
print (data)


if __name__ == '__main__':