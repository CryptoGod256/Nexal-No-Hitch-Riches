from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/deploy/<task_name>', methods=['POST'])
def deploy_task(task_name):
    print(f"[+] NEXAL COMMAND RECEIVED: Deploying {task_name}")
    # Triggers the specific script
    subprocess.Popen(["python", f"{task_name}.py"])
    return jsonify({"status": "success", "message": f"{task_name} initialized"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
