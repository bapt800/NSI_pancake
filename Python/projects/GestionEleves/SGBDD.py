from mysql import connector


class DataBase:
    def __init__(self) -> None:
        self.stream = connector.connect(user='python', password='',
                                        host='localhost',
                                        database='gestion_eleves')

    def execute(self, command:str):
        cursor = self.stream.cursor()
        cursor.execute("SELECT * FROM `eleves`")
        print(cursor.fetchall())

    def closeStream(self):
        self.stream.close()
