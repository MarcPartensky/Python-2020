#!/usr/bin/env python
import requests
import sqlite3
import json
import sys
import os

db = sqlite3.connect('isep.db')
c = db.cursor()
URL = 'https://iseplive.fr/annuaire/'

def create():
    try:
        # c.execute('create table users (
            # name text, picture text,
        # )')
        print('test')
    except:
        print('failed to cretae isep.db')


def add():
    values = sys.argv[2:]
    with open('config.json', 'r') as file:
        data = json.load(file)
        config = json.loads(data)
    config['counter'] = 0
    with open('config.json', 'w') as file:
        data = json.dumps(config)
        json.dump(data)


def reset():
    with open('config.json', 'r') as file:
        data = json.load(file)
        config = json.loads(data)
    config['counter'] = 0
    with open('config.json', 'w') as file:
        data = json.dumps(config)
        json.dump(data)

def fetch():
    data = json.load('config.json')
    config = json.load(data)
    while True:
        config['counter'] += 1
        response = requests.get(
            os.path.join(
                url,
                str(config['counter'])
            )
        )
        print(response.text)
        break

if sys.argv[1] == 'create':
    create()

if sys.argv[1] == 'reset':
    reset()

if sys.argv[1] == 'fetch':
    fetch()
