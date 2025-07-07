from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello from Docker!")

@app.route('/about')
def about():
    return jsonify(
        project="Dockerized Flask API",
        author="Jane Obikwelu",
        purpose="Learn Docker basics by containerizing a Python Flask app."
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
