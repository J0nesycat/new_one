from flask import Flask, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

# A simple in-memory user database
users_db = {
    'admin': {'name': 'alice', 'email': 'admin@example.com'},
    'user': {'name': 'bob', 'email': 'user@example.com'}
}

@app.route('/user/<username>')
def get_user(username):
    try:
        user = users_db[username]
        return jsonify(user)
    except KeyError:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)