from pg import DB

class db_connection():

    def __init__(self):
        self.hostname = 'localhost'
        self.username = 'postgres'
        self.password = 'postgres'
        self.port = 5432
        self.database = 'stock_db'

    def get_connection(self):
        conn = DB(host = self.hostname,user = self.username,
                passwd = self.password,dbname = self.database,port = self.port)
        return conn

    def create_table(self):
        db=self.get_connection()
        db.query("create table fruits(id serial primary key, name varchar)")

obj = db_connection()
obj.create_table()
