from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/<string:username>")
def say_hello(username):
    return f"Hello, {username}"


if __name__ == "__main__":
    app.debug = True
    app.run()
