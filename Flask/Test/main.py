#!/usr/bin/env python

"""Testing flask cause its flask."""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    """Main function that does main things."""
    print('salut')
    return 'wesh mon gars'

app.run()
