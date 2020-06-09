def similarity(a, b, n=1):
    if n<=1:
        # print(a, b)
        d = len(a+b)
        c = [e for e in a if e in set(b)]
        n = len(c)
        # print(set(a+b))
        # print(d, n)
        return n/d
    sa = [a[i:i+n] for i in range(len(a)-n+1)]
    sb = [b[i:i+n] for i in range(len(b)-n+1)]
    return similarity(sa, sb)


def resemblance(a, b):
    d = len(a+b)
    n = len(set(a+b))
    return n/d

def common(a, b):
    return [e for e in a if e in set(b)]

def common_substring(a, b):
    sa = substring(a)
    sb = substring(b)
    sc = common(sa, sb)
    stc = len(sa+sb)/2
    return len(sc)/stc

def substring(a):
    return [a[i:i+n+1] for n in range(len(a)) for i in range(len(a)-n)]

a = '0'
b = '012345'

def test1():
    sm = 0
    n = min(len(a),len(b))
    for i in range(n):
        s = similarity(a, b, i+1)
        sm += s
        print(i, s)

    print('score:', sm/n)

def test2():
    r = substring("abc")
    print(r)

def test3():
    r = common_substring(a, b)
    print(r)


test3()
