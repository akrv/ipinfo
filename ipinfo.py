from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return str(request.remote_addr)

@app.route("/json", methods=["GET"])
def get_my_ip():
    print (request.headers.getlist("X-Forwarded-For"))
    return jsonify({'ip': request.remote_addr}), 200

if __name__ == "__main__":
    app.run(port=25500)