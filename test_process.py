#!/usr/bin/env python

while True:
    text = input('write on enter:')
    with open('test_file.txt', 'a') as f:
        f.write(text)
