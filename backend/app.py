from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP",
        "message": "Login application backend is healthy"
    })


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "Admin@123":
        return jsonify({
            "status": "success",
            "message": "Login successful"
        }), 200

    return jsonify({
        "status": "failed",
        "message": "Invalid username or password"
    }), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
