from flask import Flask
from flask import render_template
import os
app = Flask(__name__)

@app.route("/")
def hello():
    mongo = os.popen("ps aux | grep [m]ongo | awk '{print$2}'").read()
    nginx = os.popen("ps aux | grep [n]ginx | awk '{print$2}'").read()
    guni = os.popen("ps aux | grep [g]unicorn | awk '{print$2}'").read()
    return render_template('status.html',mongo=mongo, nginx=nginx,guni=guni)

if __name__ == "__main__":
    app.run(host='0.0.0.0')