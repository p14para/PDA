from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/update_order', methods=['POST'])
def update_order():
    order_data = request.json
    # Handle the order submission (save to a database or process)
    print(f"Received order for table {order_data['table_number']}")
    return jsonify({'status': 'success', 'order_id': 123})

if __name__ == '__main__':
    app.run(debug=True)
