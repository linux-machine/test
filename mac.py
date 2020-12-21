import re
from functools import wraps


def decor_func(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        args[0].mac = args[0].normalized()
        args[1].mac = args[1].normalized()
        r = f(*args, **kwargs)
        return r

    return wrapped


class Mac:
    def __init__(self, m):
        self.regs = {0: {'match': r'((?:[0-9A-Fa-f]{2}\-){5}(?:[0-9A-Fa-f]{2}))',
                         'sub': r'\1-\2-\3-\4-\5-\6'},
                     1: {'match': r'((?:[0-9A-Fa-f]{2}\:){5}(?:[0-9A-Fa-f]{2}))',
                         'sub': r'\1:\2:\3:\4:\5:\6'},
                     2: {'match': r'((?:[0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4})',
                         'sub': r'\1\2.\3\4.\5\6'},
                     3: {'match': r'((?:[0-9A-Fa-f]{12}))',
                         'sub': r'\1\2\3\4\5\6'}}

        if not (isinstance(m, str) and any(re.match(self.regs[x]['match'], m) for x in self.regs)):
            raise ValueError('Wrong mac address format')
        else:
            self.mac = m
            self.tp = 0

    def set_type(self, t):
        if 0 <= t <= 3:
            self.tp = t
        else:
            raise ValueError('Wrong mac address type')

    def normalized(self):
        return ''.join(re.findall(r'(\w+)', self.mac))

    def __str__(self):
        return re.sub(r'(\w{2})(\w{2})(\w{2})(\w{2})(\w{2})(\w{2})',
                      self.regs[self.tp]['sub'], self.normalized())

    @decor_func
    def __eq__(self, second_mac):
        return self.mac == second_mac.mac


m1 = Mac('AA:AA:AA:FA:AA:AA')
m2 = Mac('AAAA.AAFA.BBAA')
m3 = Mac('AAAAAAFAAAAA')

print('\noriginal:\n')
print('m1 = ', m1)
print('m2 = ', m2)
print('m3 = ', m3)

m1.set_type(1)
m2.set_type(2)
m3.set_type(3)

print('\nretyped:\n')
print('m1 = ', m1)
print('m2 = ', m2)
print('m3 = ', m3)

print('\ncompared:\n')
print('m1 == m2 ?', m1 == m2)
print('m2 == m3 ?', m2 == m3)
print('m1 == m3 ?', m1 == m3)
