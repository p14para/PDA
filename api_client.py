import requests

class APIClient:
    BASE_URL = 'http://your_flask_server/api'

    def update_order(self, order_data):
        response = requests.post(f'{self.BASE_URL}/update_order', json=order_data)
        return response.json()
