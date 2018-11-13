from flask import Flask
from random import randint
from time import sleep

application = Flask(__name__)

@application.route("/")
def hello():
    sleep(200)
    return "Hello Knative & Openshift!\n"

if __name__ == "__main__":
    application.run()
