from flask import Flask
import subprocess
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    subprocess.Popen(app.run(host='0.0.0.0'))