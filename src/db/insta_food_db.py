import sqlite3
from datetime import datetime, timedelta
from sqlite3 import Error


class Insta_Food_DB:
    def __init__(self, db):
        self.db = db
        self.conn = None

    def create_connection(self):
        """ Create a database connection to the SQLite database
            specified by db_file
        Returns:
            Connection Object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(self.db)
            self.conn = conn
            return conn
        except Error as e:
            print(e)
    
        return conn


    def create_table(self, db_table):
        """ Create a table within the SQLite database
        Arguments:
            db_table (str): SQL statement to create table
        """
        conn = self.conn
        if conn:
            # create followers table
            try:
                c = conn.cursor()
                c.execute(db_table)
            except Error as e:
                print(e)
        else:
            print("Error! cannot create the database connection.")
    

    def insert_follower(self, days_till_unfollow=0):
        """ Insert a into followers table when bot follows an account
        Arguments:
            days_till_unfollow (int) [default: 0]: Number of days set for bot to unfollow account
        Returns:
            cursor.lastrowid: read-only attribute provides the rowid of the last modified row
        """
        conn = self.conn
        if conn:
            try:
                current_time = datetime.now()
                expired_time = current_time + timedelta(days=days_till_unfollow)
                sql = f''' INSERT INTO Followers(username,follow_time,unfollow_time)
                        VALUES(?,?,?) '''
                values = ('xaviergiocontreras',current_time,expired_time)
                conn.execute(sql, values)
                conn.commit()
                cur = conn.cursor()
                return cur.lastrowid
            except Error as e:
                print(e)
        else:
            print("Error! cannot create the database connection.")
    

    def retrieve_credentials(self):
        conn = self.conn
        if conn:
            try:
                sql = 'SELECT * FROM Instagram'
                cur = conn.cursor()
                cur.execute(sql)
                creds = cur.fetchone()
                return {'username': creds[0], 'password': creds[1]}
            except Error as e:
                print(e)
        else:
            print("Error! Cannot create the database connections.")


if __name__ == '__main__':
    db_path = "C:\\Users\\Xavier\\Workspace\\instafood-nyc\\src\\db\\pythonsqlite.db"
    db = Insta_Food_DB(db_path)
    db.create_connection()
    '''
    sql_create_followers_table = """-- Followers table
                                        CREATE TABLE IF NOT EXISTS Followers (
                                        username text PRIMARY KEY NOT NULL,
                                        follow_time timestamp,
                                        unfollow_time timestamp
                                    );"""
    '''
    #create_table(conn, sql_create_followers_table)
    #insert_follower(conn, 30)
    db.retrieve_credentials()