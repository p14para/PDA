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

    def fetch_menu(self):
        cursor = self.conn.execute('SELECT * FROM MenuItem')
        return cursor.fetchall()

    def save_order(self, table_number, order_items):
        # Save order
        cursor = self.conn.execute('INSERT INTO Orders (table_number, status) VALUES (?, ?)', (table_number, 'pending'))
        order_id = cursor.lastrowid

        # Save ordered items
        for item in order_items:
            self.conn.execute('INSERT INTO OrderItems (order_id, item_id, quantity) VALUES (?, ?, ?)',
                              (order_id, item['id'], 1))

        self.conn.commit()
        return order_id


# Example function to add menu items
def populate_menu():
    db = Database()
    db.add_menu_item('Burger', 'Food', 5.99)
    db.add_menu_item('Pizza', 'Food', 8.99)
    db.add_menu_item('Coke', 'Drinks', 1.99)
    db.add_menu_item('Coffee', 'Drinks', 2.99)

