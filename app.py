from flask import *

app = Flask(__name__)
app.secret_key = "super secret key"
app.debug = True
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!

@app.route("/hello", methods=["GET"])
def helloWorld():
    return jsonify({"msg": "HelloWorld"})

@app.route("/", methods=["GET"])
def healthcheck():
    return Response(response="abcd123", status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
