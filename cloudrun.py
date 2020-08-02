import os
import subprocess
from flask import Flask, request, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to cloud Run http Shell!"


@app.route('/<string:command>')
def cmd_to_run(command):
    try:
        cmd = command
        cmd_output = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=10, universal_newlines=True)
        response = make_response(cmd_output.stdout, 200)
        response.mimetype = "text/plain"
        return response
    except subprocess.TimeoutExpired:
        response = make_response("Timedout", 400)
        response.mimetype = "text/plain"
        return response
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
