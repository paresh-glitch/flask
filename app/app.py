from flask import Flask, jsonify
from datetime import datetime
import os

app = Flask(__name__)

PORT = int(os.environ.get('PORT', 5000))
APP_ENV = os.environ.get('APP_ENV', 'development')

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello from Python Flask!',
        'version': '1.0.0',
        'environment': APP_ENV,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'language': 'Python',
        'framework': 'Flask'
    })

@app.route('/api/users')
def users():
    return jsonify([
        { 'id': 1, 'name': 'Alice', 'city': 'Mumbai' },
        { 'id': 2, 'name': 'Bob',   'city': 'Delhi'  },
        { 'id': 3, 'name': 'Carol', 'city': 'Pune'   }
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)
