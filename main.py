from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from models import Database

# Load KV files
Builder.load_file('views/menu.kv')
Builder.load_file('views/order.kv')
Builder.load_file('views/table.kv')

db = Database()

class MenuScreen(Screen):
    def on_enter(self):
        print("Entering MenuScreen")
        menu_grid = self.ids.menu_grid
        menu_grid.clear_widgets()

        menu_items = db.fetch_menu()
        for item in menu_items:
            btn = Button(text=f"{item[1]} - ${item[3]}")
            btn.bind(on_press=lambda x, i=item: self.add_to_order(i))
            menu_grid.add_widget(btn)

    def add_to_order(self, item):
        app = App.get_running_app()
        app.order.append({'id': item[0], 'name': item[1], 'price': item[3]})

class OrderScreen(Screen):
    def on_enter(self):
        print("Entering OrderScreen")
        order_grid = self.ids.order_grid
        order_grid.clear_widgets()

        app = App.get_running_app()
        for item in app.order:
            order_grid.add_widget(Label(text=f"{item['name']} - ${item['price']}"))

    def submit_order(self):
        print("Submitting order")
        app = App.get_running_app()
        if app.table_number:
            order_id = db.save_order(app.table_number, app.order)
            app.order.clear()
            self.manager.current = 'menu'
        else:
            print("Please assign a table first.")

class TableScreen(Screen):
    def assign_table(self, table_number):
        app = App.get_running_app()
        app.table_number = table_number

    def confirm_table(self):
        if App.get_running_app().table_number:
            self.manager.current = 'order'
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
