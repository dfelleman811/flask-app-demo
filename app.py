from flask import Flask

application = Flask(__name__)


@application.route("/")
def index():
    return "Hello World!"


@application.route("/<string:username>")
def say_hello(username):
    return f"Hello, {username}"


if __name__ == "__main__":
    application.debug = True
    application.run()
