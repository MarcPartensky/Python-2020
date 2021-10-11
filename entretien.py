#!/usr/bin/env python

msgs = {}
n = 1


def process_msg(msg):
    global n, msgs
    msgs[msg["seq_num"]] = msg
    l = []
    while n in msgs:
        l.append(msgs[n])
        del msgs[n]
        n += 1
    return l


if __name__ == "__main__":
    print(process_msg(dict(seq_num=4)))  # => [] (4) n=1
    print(process_msg(dict(seq_num=2)))  # => [] (4,2) n=1
    print(process_msg(dict(seq_num=1)))  # => [1,2] (4) n=2
    print(process_msg(dict(seq_num=3)))  # => [3,4] () n=4
