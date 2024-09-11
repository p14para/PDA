import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.create_tables()

    def create_tables(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS MenuItem
                             (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL)''')

        self.conn.execute('''CREATE TABLE IF NOT EXISTS Orders
                             (id INTEGER PRIMARY KEY, table_number INTEGER, status TEXT)''')

        self.conn.execute('''CREATE TABLE IF NOT EXISTS OrderItems
                             (order_id INTEGER, item_id INTEGER, quantity INTEGER)''')

    def add_menu_item(self, name, category, price):
        self.conn.execute('INSERT INTO MenuItem (name, category, price) VALUES (?, ?, ?)', (name, category, price))
        self.conn.commit()

    def fetch_menu(self):
        cursor = self.conn.execute('SELECT * FROM MenuItem')
        return cursor.fetchall()
