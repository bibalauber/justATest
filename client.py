from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/endpoint', methods=['POST'])
def handle_post_request():
    data = request.get_json()  # Get the JSON data sent by the server
    # Process the data received from the server as needed
    print('Received POST request data:', data)
    return jsonify({'message': 'POST request received successfully'})

if __name__ == '__main__':
    app.run(host='localhost', port=5500)
