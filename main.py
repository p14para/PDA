# from kivy.app import App
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.lang import Builder
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from models import Database

# # Load KV files
# Builder.load_file('views/menu.kv')
# Builder.load_file('views/order.kv')
# Builder.load_file('views/table.kv')

# db = Database()

# class MenuScreen(Screen):
#     def on_enter(self):
#         print("Entering MenuScreen")
#         menu_grid = self.ids.menu_grid
#         menu_grid.clear_widgets()

#         menu_items = db.fetch_menu()
#         for item in menu_items:
#             btn = Button(text=f"{item[1]} - ${item[3]}")
#             btn.bind(on_press=lambda x, i=item: self.add_to_order(i))
#             menu_grid.add_widget(btn)

#     def add_to_order(self, item):
#         app = App.get_running_app()
#         app.order.append({'id': item[0], 'name': item[1], 'price': item[3]})

# class OrderScreen(Screen):
#     def on_enter(self):
#         print("Entering OrderScreen")
#         order_grid = self.ids.order_grid
#         order_grid.clear_widgets()

#         app = App.get_running_app()
#         for item in app.order:
#             order_grid.add_widget(Label(text=f"{item['name']} - ${item['price']}"))

#     def submit_order(self):
#         print("Submitting order")
#         app = App.get_running_app()
#         if app.table_number:
#             order_id = db.save_order(app.table_number, app.order)
#             app.order.clear()
#             self.manager.current = 'menu'
#         else:
#             print("Please assign a table first.")

# class TableScreen(Screen):
#     def assign_table(self, table_number):
#         app = App.get_running_app()
#         app.table_number = table_number

#     def confirm_table(self):
#         if App.get_running_app().table_number:
#             self.manager.current = 'order'
#         else:
#             print("No table selected.")

# class RestaurantApp(App):
#     order = []
#     table_number = None

#     def build(self):
#         sm = ScreenManager()
#         sm.add_widget(MenuScreen(name='menu'))
#         sm.add_widget(OrderScreen(name='order'))
#         sm.add_widget(TableScreen(name='table'))
#         return sm

# if __name__ == '__main__':
#     RestaurantApp().run()

# --------------------------------------------------------------------
# from kivy.app import App
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button

# class MainScreen(Screen):
#     def __init__(self, **kwargs):
#         super(MainScreen, self).__init__(**kwargs)
#         layout = BoxLayout(orientation='vertical')

#         btn_menu = Button(text='Menu', size_hint=(1, 0.2))
#         btn_menu.bind(on_press=self.go_to_menu)
#         layout.add_widget(btn_menu)

#         btn_orders = Button(text='Orders', size_hint=(1, 0.2))
#         btn_orders.bind(on_press=self.go_to_orders)
#         layout.add_widget(btn_orders)

#         btn_settings = Button(text='Settings', size_hint=(1, 0.2))
#         btn_settings.bind(on_press=self.go_to_settings)
#         layout.add_widget(btn_settings)

#         self.add_widget(layout)

#     def go_to_menu(self, instance):
#         self.manager.current = 'menu'

#     def go_to_orders(self, instance):
#         self.manager.current = 'orders'

#     def go_to_settings(self, instance):
#         self.manager.current = 'settings'

# class OrdersScreen(Screen):
#     def __init__(self, **kwargs):
#         super(OrdersScreen, self).__init__(**kwargs)
#         layout = BoxLayout(orientation='vertical')

#         label = Button(text='Order List Placeholder', size_hint=(1, 0.8))
#         layout.add_widget(label)

#         btn_back = Button(text='Back', size_hint=(1, 0.2))
#         btn_back.bind(on_press=self.go_back)
#         layout.add_widget(btn_back)

#         self.add_widget(layout)

#     def go_back(self, instance):
#         self.manager.current = 'main'

# class SettingsScreen(Screen):
#     def __init__(self, **kwargs):
#         super(SettingsScreen, self).__init__(**kwargs)
#         layout = BoxLayout(orientation='vertical')

#         label = Button(text='Settings Placeholder', size_hint=(1, 0.8))
#         layout.add_widget(label)

#         btn_back = Button(text='Back', size_hint=(1, 0.2))
#         btn_back.bind(on_press=self.go_back)
#         layout.add_widget(btn_back)

#         self.add_widget(layout)

#     def go_back(self, instance):
#         self.manager.current = 'main'

# class MenuScreen(Screen):
#     def __init__(self, **kwargs):
#         super(MenuScreen, self).__init__(**kwargs)
#         layout = BoxLayout(orientation='vertical')

#         label = Button(text='Menu Placeholder', size_hint=(1, 0.8))
#         layout.add_widget(label)

#         btn_back = Button(text='Back', size_hint=(1, 0.2))
#         btn_back.bind(on_press=self.go_back)
#         layout.add_widget(btn_back)

#         self.add_widget(layout)

#     def go_back(self, instance):
#         self.manager.current = 'main'

# class MyApp(App):
#     def build(self):
#         sm = ScreenManager()
#         sm.add_widget(MainScreen(name='main'))
#         sm.add_widget(MenuScreen(name='menu'))
#         sm.add_widget(OrdersScreen(name='orders'))
#         sm.add_widget(SettingsScreen(name='settings'))
#         return sm

# if __name__ == '__main__':
#     MyApp().run()


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class HomeScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class OrdersScreen(Screen):
    pass

class TestScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        Builder.load_file('main.kv')
        return ScreenManager()

if __name__ == '__main__':
    MyApp().run()

