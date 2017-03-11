from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return str(request.headers.getlist("X-Forwarded-For"))

@app.route("/json", methods=["GET"])
def get_my_ip():
    
    return jsonify({'ip': request.headers.getlist("X-Forwarded-For")}), 200

if __name__ == "__main__":
    app.run(port=25500)