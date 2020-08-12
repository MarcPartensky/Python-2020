#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    print('salut')
    return 'wesh'

app.run()
