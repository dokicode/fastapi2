def couroutine(func):
    def inner(*args, **kwargs):
        _g = func()
        _g.send(None)
        return _g
    return inner


def subgen():
    msg = yield
    print(msg, '23')


@couroutine
def average():
    count = 0
    summ = 0
    avg = None
    while True:
        try:
            x = 123
            yield avg
        except StopIteration:
            print('Done')
            break
        else:
            count += 1
            summ += x
            avg = round(summ / count, 2)

    return avg


if __name__ == '__main__':
    # g = subgen()
    # g.send(None)
    # g.send('123')
    g = average()
    print(next(g))
    print(next(g))
    print(next(g))
    # print(g.send(123))
    # print(g.send(321))
    try:
        g.throw(StopIteration)
    except StopIteration as e:
        print(e.value)