import sqlite3

class Database:
    def __init__(self, db_name='database.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS MenuItem (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                table_number INTEGER,
                items TEXT
            )
        ''')
        self.connection.commit()

    def fetch_menu(self):
        self.cursor.execute('SELECT * FROM MenuItem')
        return self.cursor.fetchall()

    def save_order(self, table_number, order_items):
        items = ','.join(f"{item['name']} (${item['price']})" for item in order_items)
        self.cursor.execute('INSERT INTO Orders (table_number, items) VALUES (?, ?)', (table_number, items))
        self.connection.commit()
        return self.cursor.lastrowid
