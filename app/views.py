from app import app
import socket
from flask import jsonify
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
s.close()


@app.route('/')
@app.route('/index')
def index():
    return "the local ip of this machine is " + local_ip


@app.route("/health")
def health():
    return jsonify({'status': 'ok'})


@app.route("/hello")
def hello():
    return 'hello'
