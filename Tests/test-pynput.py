#!/usr/bin/env python

from pynput.keyboard import Listener
from shutil import copyfile

import os
import logging
import string

username = os.getlogin()

logging_directory = os.path.join(
    os.environ['HOME'],
    'desktop'
)

logging.basicConfig(filename=f"{logging_directory}/mylog.txt",
                    level=logging.DEBUG, format="%(asctime)s: %(message)s")
keys = []
def key_handler(key):
    if hasattr(key, 'char'):
        print(key.char)
    logging.info(key)
    parse(key)

def parse(key):
    # if len(keys) > 10:
    #     keys.pop(0)
    keys.append(key)
    print(key.__dict__)
    print(key)

    for key in keys[-4:]:
        if not hasattr(key, 'char'):
            return
        if key.char not in string.ascii_lowercase:
            return

    print(key.char)

    if ''.join(map(lambda k:k.char,keys[-4:]))=="test":
        print("you are testing")

with Listener(on_press=key_handler) as listener:
    listener.join()
