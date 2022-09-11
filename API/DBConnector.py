class DBConnector:
    def __init__(self, host, user, password, database):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    


if __name__ == '__main__':
    dbConnector = DBConnector("Leon")
    dbConnector.print_name()
    print(dbConnector.name)