#!/usr/bin/env python

"""Testing flask cause its flask."""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    """Main function."""
    print('salut')
    return 'wesh'

app.run()
