class DBConnector:
    def __init__(self, name):
        self.__name = name


    def print_name(self):
        print(self.__name)


if __name__ == '__main__':
    dbConnector = DBConnector("Leon")
    dbConnector.print_name()
    print(dbConnector.name)