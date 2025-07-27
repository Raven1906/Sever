from flask import Flask, request, render_template

app = Flask(__name__)
log_data = []
last_command = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    global last_command
    if request.method == 'POST':
        cmd = request.form.get('command')
        if cmd:
            last_command = cmd
    return render_template('panel.html', logs=log_data, command=last_command)

@app.route('/report', methods=['POST'])
def report():
    data = request.get_json()
    ip = request.remote_addr
    msg = data.get('msg')
    if msg:
        log_data.append(f"[{ip}] {msg}")
    return {"status": "OK"}

@app.route('/getcmd', methods=['GET'])
def getcmd():
    return {"cmd": last_command}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
