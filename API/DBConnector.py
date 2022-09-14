import mysql.connector

class DBConnector:
    def __init__(self, host, user, password, database):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database
        self.__mydb = mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            database=self.__database
        )
        self.__mycursor = self.__mydb.cursor()

    def executeSQL(self, sql):
        try:
            self.__mycursor.execute(sql)
            return{
                "data": self.__mycursor.fetchall(),
                "status": 200
            }
        except Exception as error:
            return{
                "error": error,
                "status": 400
            }

    def manipulateData(self, sql, val):
        #INSERT INTO [tbl] ([column1]) VALUES (%s)
        try:
            self.__mycursor.execute(sql, val)
            self.__mydb.commit()
            return{
                "status": 200
            }
        except Exception as error:
            return{
                "errror": error,
                "status": 400
            }

    def is_Existing(self, sql):
        try:
            self.__mycursor.execute(sql)

            if(len(self.__mycursor.fetchall()) > 0):
                return{
                    "result": True,
                    "status": 200
                }         
            return{
                "result": False,
                "status": 200
            }   
        except Exception as error:
            return{
                "error": error,
                "status": 400
            }
        

if __name__ == '__main__':
    dbConnector = DBConnector("localhost", "root", "", "usermanagement")
    
    sql_insert = "INSERT INTO tblusers (username, email, password) VALUES (%s, %s, %s)"
    val_insert = ("Leon", "leon@salenbacher.com", "LeonPW")
    
    sql_get = "SELECT * FROM tblusers;"

    sql_exist = "SELECT * FROM tblusers WHERE username='Len';"

    #res = dbConnector.manipulateData(sql, val)
    res = dbConnector.is_Existing(sql_exist)
    print(res)
