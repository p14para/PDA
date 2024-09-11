from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Load KV files
Builder.load_file('views/menu.kv')
Builder.load_file('views/order.kv')
Builder.load_file('views/table.kv')

class MenuScreen(Screen):
    def on_enter(self):
        # This is where we'll dynamically load the menu items
        menu_grid = self.ids.menu_grid
        menu_grid.clear_widgets()

        # Example menu items
        menu_items = [
            {"name": "Burger", "price": 5.99},
            {"name": "Pizza", "price": 8.99},
            {"name": "Salad", "price": 4.99}
        ]

        for item in menu_items:
            btn = Button(text=f"{item['name']} - ${item['price']}")
            btn.bind(on_press=lambda x, i=item: self.add_to_order(i))
            menu_grid.add_widget(btn)

    def add_to_order(self, item):
        # Logic to add menu item to the order
        app = App.get_running_app()
        app.order.append(item)

class OrderScreen(Screen):
    def on_enter(self):
        # Populate order items
        order_grid = self.ids.order_grid
        order_grid.clear_widgets()

        app = App.get_running_app()
        for item in app.order:
            order_grid.add_widget(Label(text=f"{item['name']} - ${item['price']}"))

    def submit_order(self):
        # Logic to submit the order
        app = App.get_running_app()
        print(f"Submitting order: {app.order}")
        app.order.clear()

class TableScreen(Screen):
    def assign_table(self, table_number):
        # Logic to assign table
        app = App.get_running_app()
        app.table_number = table_number
        print(f"Assigned to Table {table_number}")

    def confirm_table(self):
        print(f"Order confirmed for Table {App.get_running_app().table_number}")

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
