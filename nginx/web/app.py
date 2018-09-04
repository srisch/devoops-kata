from flask import Flask
import subprocess
app = Flask(__name__)

@app.route("/")
def hello():
    mongo = subprocess.Popen(['service','mongodb','status'], stdout=subprocess.PIPE)
    stdout = mongo.communicate()[0]
    return 'Mongo Status %s' % stdout

if __name__ == "__main__":
    app.run(host='0.0.0.0')