from itertools import combinations
def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return 
    indices = list(range(r))
    yield tuple
