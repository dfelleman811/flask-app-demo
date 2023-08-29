from flask import Flask

appplication = Flask(__name__)


@appplication.route("/")
def index():
    return "Hello World!"


@appplication.route("/<string:username>")
def say_hello(username):
    return f"Hello, {username}"


if __name__ == "__main__":
    appplication.debug = True
    appplication.run()
