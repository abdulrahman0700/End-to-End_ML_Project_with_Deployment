import psycopg2

class database():
    def __init__(self):
        self.conn = psycopg2.connect(host='localhost',
                                     dbname='postgres',
                                     user='postgres',
                                     password='DataBase pasword',
                                     port='number of the port')
        self.cursor = self.conn.cursor()

    def create_table(self):
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Football(
               id INT PRIMARY KEY,
               Tesms VARCHAR(255),
               Seasons VARCHAR(255),
               Players VARCHAR(255),
               Matches INT,
               Goals INT,
               Assists INT           
               )
               """)
        
    def insert_data(self,id,Teams,Seasons,Players,Matches,Goals,Assists):
        id += 1
        self.cursor.execute("""INSERT INTO Football (id,
                                                   Tesms,
                                                   Seasons,
                                                   Players,
                                                   Matches,
                                                     Goals,
                            Assists) VALUES (%s,%s,%s,%s,%s,%s,%s)""",(id,Teams,Seasons,Players,Matches,Goals,Assists))
        self.conn.commit()


    def read_data(self):
        return self.cursor.execute("""SELECT * FROM  Football""")


    def update_data(self,id,Teams,Seasons,Players,Matches,Goals,Assists):
        self.cursor.execute(""" UPDATE Football SET (
                            Teams={},
                            Seasons={},
                            Players={},
                            Matches={},
                            Goals={},
                            Assists={}
                            WHERE id={})
                            """.format(Teams,Seasons,Players,Matches,Goals,Assists,id))
        self.conn.commit()
    
    def delete_data(self,id):
        self.cursor.execute(""" DELETE FROM Footbal WHERE id={}""".format(id))
        self.conn.commit()


dataBase = database()

dataBase.cursor.close()
dataBase.conn.close()