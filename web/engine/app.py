from flask import Flask, jsonify
from scanner import run_scan

app = Flask(__name__)

@app.route("/api/scan", methods=['GET'])
def api_scan():
    try:
        data = run_scan()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/")
def index():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
