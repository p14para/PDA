from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from models import Database

# Load KV files
Builder.load_file('views/menu.kv')
Builder.load_file('views/order.kv')
Builder.load_file('views/table.kv')

db = Database()  # Initialize database

class MenuScreen(Screen):
    def on_enter(self):
        menu_grid = self.ids.menu_grid
        menu_grid.clear_widgets()

        # Fetch menu items from database
        menu_items = db.fetch_menu()

        for item in menu_items:
            # item[1] is name, item[3] is price (based on how data is fetched from SQLite)
            btn = Button(text=f"{item[1]} - ${item[3]}")
            btn.bind(on_press=lambda x, i=item: self.add_to_order(i))
            menu_grid.add_widget(btn)

    def add_to_order(self, item):
        app = App.get_running_app()
        app.order.append({'id': item[0], 'name': item[1], 'price': item[3]})

class OrderScreen(Screen):
    def on_enter(self):
        order_grid = self.ids.order_grid
        order_grid.clear_widgets()

        app = App.get_running_app()
        for item in app.order:
            order_grid.add_widget(Label(text=f"{item['name']} - ${item['price']}"))

    def submit_order(self):
        app = App.get_running_app()
        if app.table_number:
            order_id = db.save_order(app.table_number, app.order)  # Save order in database
            print(f"Order {order_id} submitted for Table {app.table_number}")
            app.order.clear()  # Clear current order after submission
            self.manager.current = 'menu'  # Go back to the menu screen
        else:
            print("Please assign a table first.")

class TableScreen(Screen):
    def assign_table(self, table_number):
        app = App.get_running_app()
        app.table_number = table_number
        print(f"Assigned to Table {table_number}")

    def confirm_table(self):
        if App.get_running_app().table_number:
            print(f"Order confirmed for Table {App.get_running_app().table_number}")
            self.manager.current = 'order'  # Go to order screen after assigning table
        else:
            print("No table selected.")

class RestaurantApp(App):
    order = []
    table_number = None

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(OrderScreen(name='order'))
        sm.add_widget(TableScreen(name='table'))
        return sm

if __name__ == '__main__':
    RestaurantApp().run()
