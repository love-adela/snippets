from itertools import combinations 
# Elements are treated as unique based on their position, not on their value. So if the input elements are unique, there will be no repeat values in each combination.
def combinations(iterable, r:int) -> Iterator[tuple]:
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return 
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n -r:
                break
            else:
                return
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
            yield tuple(pool[i] for i in indices)

# combinations() can be also expressed as a subsequence of permutations()
def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)
