from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/hello-page')
def hello_page():
    return 'Hello, World!'

# Run the app
if __name__ == '__main__':
    try:
        app.run( host='0.0.0.0', port=8000, debug=True)
    except (KeyboardInterrupt, SystemExit):
        print("Exiting...")