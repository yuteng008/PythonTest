def high(l):
    return [i.upper() for i in l]

def test(h,l):
    return h(l)

l = ['python','linux','Git']

test(high,l)
