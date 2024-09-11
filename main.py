from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from models import Database

db = Database()

class MenuScreen(Screen):
    def on_enter(self):
        menu = db.fetch_menu()
        # Code to display menu items dynamically

class OrderScreen(Screen):
    pass

class TableScreen(Screen):
    pass

class RestaurantApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(OrderScreen(name='order'))
        sm.add_widget(TableScreen(name='table'))
        return sm

if __name__ == '__main__':
    RestaurantApp().run()
