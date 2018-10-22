from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello Knative & Openshift!\n"

if __name__ == "__main__":
    application.run()
