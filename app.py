from crypt import methods
from django.http import HttpResponse, HttpResponseForbidden
from flask import Flask, jsonify
import random, string
import json

app = Flask(__name__)


@app.route('/generate-password/<int:length>/<string:lowercase>/<string:uppercase>/<int:digits>', methods=['GET'])
def passwordGeneration(length, lowercase, uppercase, digits):
    chars = lowercase + uppercase + '!@#$%^&*(){}|¨"¦“|\/?'
    rnd = random.SystemRandom()

    password = ''.join(rnd.choice(chars) for i in range(length))
    json_pass = json.dumps(list(password))

    return json_pass

@app.route('/generate-password/<int:length>/<string:lowercase>/<string:uppercase>/<int:digits>', methods=['GET'])
def errorPage(length, lowercase, uppercase, digits):
    if length < 10:
        HttpResponseForbidden
    elif len(lowercase) < 10:
        HttpResponseForbidden
    elif len(uppercase) < 10:
        HttpResponseForbidden
    elif digits < 10:
        HttpResponseForbidden
    else:
        passwordGeneration()


if __name__ == '__main__':
    app.run(debug=True)