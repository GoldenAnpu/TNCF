"""
Additional functions
"""


def clean_it_pass(characters):
    """ Clean it_pass dummy object from body """
    part = 'it_pass'
    for character in characters:
        if part in character:
            character.remove(part)


def product_result(*args):
    """ Itertools product function support in case of impossible import.
        product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
        product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    """
    pools = [tuple(pool) for pool in args]
    pool_result = [[]]
    for pool in pools:
        pool_result = [x + [y] for x in pool_result for y in pool]
    return pool_result
