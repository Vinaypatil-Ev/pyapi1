import flask
from flask import request
import random

import random
no = random.randint(0,9)

app = flask.Flask(__name__)

@app.route('/', method=["GET"])

def home():
    arg = request.arg['pos']
    while True:
        no = random.randint(0,9)
        if no != arg:
            break
    
    try:
        return f"My Position {no} "
    except KeyError:
        return "Invalid input"