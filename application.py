from flask import Flask

# I'm using 'application' for elastic beanstalk - it recognizes 'application' but not 'app'
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
