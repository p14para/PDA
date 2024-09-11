import requests

class APIClient:
    BASE_URL = 'http://your-flask-server.com/api'

    def submit_order(self, table_number, order_items):
        order_data = {
            'table_number': table_number,
            'items': order_items
        }
        response = requests.post(f'{self.BASE_URL}/update_order', json=order_data)
        return response.json()
