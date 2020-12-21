from functools import wraps


def print_markers(func):
    @wraps(func)
    def wrapped():
        return '[ ! ]' + func() + '[ ! ]'
    return wrapped


@print_markers
def foo():
    return 'I\'m simple function'


if __name__ == '__main__':
    print(foo())
