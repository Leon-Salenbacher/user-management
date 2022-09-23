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

    def get_mycursor(self):
        return self.__mycursor

    def get_mydb(self):
        return self.__mydb

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
    
    def sql_manipulateData(self, sql):
        try:
            self.__mycursor.execute(sql)
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

    sql_existing1 = "SELECT * FROM tblusers WHERE username = 'steve';"
    res_existing1 = dbConnector.is_Existing(sql_existing1)
    print(type(res_existing1['result']))
    if(not res_existing1['result']):
        print("here")

    sql1 = "INSERT INTO tblusers (username, email, password, profilePicture) VALUES (%s, %s, %s, %s);"
    val1 = ('steve', 'steve@gmail.com', 'steve1234', 'default')
    result1 = dbConnector.manipulateData(sql1, val1)
    print(result1)

    sql_existing2 = "SELECT * FROM tblusers WHERE username = 'steve';"
    res_existing2 = dbConnector.is_Existing(sql_existing2)
    print(res_existing2)



    sql2 = "SELECT * FROM tblusers WHERE username= 'steve';"
    result2 = dbConnector.executeSQL(sql2)
    print(result2)

    input()

    sql3 = "DELETE FROM tblusers WHERE username = 'steve';"
    result3 = dbConnector.sql_manipulateData(sql3)
    print(result3)

    sql4 = "SELECT * FROM tblusers WHERE username= 'steve';"
    result4 = dbConnector.executeSQL(sql4)
    print(result4)

    input()