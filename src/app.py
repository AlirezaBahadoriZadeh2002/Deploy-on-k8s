from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

# Function to Fetch Information
def fetchDetails():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)    
    return str(hostname),str(ip)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(
        status="Up"        
    )

@app.route("/details")
def details():
    hostname , ip = fetchDetails()
    return render_template('index.html' , HOSTNAME=hostname , IP=ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)