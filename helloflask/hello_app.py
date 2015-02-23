import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Howdy as-salamu alaykum world!'
