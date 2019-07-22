import itertools

from string import ascii_uppercase


def next_letter():
    for r in range(1, 4):
        for s in itertools.product(ascii_uppercase, repeat=r):
            yield ''.join(s)
