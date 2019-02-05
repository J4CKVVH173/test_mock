from . import culc

def test():
    a = culc.sum(1, 2)
    a = a + 1
    return a


if __name__ == '__main__':
    test()
