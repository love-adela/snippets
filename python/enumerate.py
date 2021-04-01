# use enumerate()
jewelry = ['gold', 'sapphire', 'silver', 'emerald', 'ruby']
print(list(enumerate(jewelry))) # [(0, 'gold'), (1, 'sapphire'), (2, 'silver'), (3, 'emerald'), (4, 'ruby')]

# define custom _enumerate()
def _enumerate(seq:list):
    lst = []
    for i in range(len(seq)):
        lst.append((i, seq[i]))
    return lst

print(_enumerate(jewelry)) # [(0, 'gold'), (1, 'sapphire'), (2, 'silver'), (3, 'emerald'), (4, 'ruby')]

# define custom __enumerate() with yield
def __enumerate(seq:list, start=0):
    n = start
    for item in seq:
        yield n, item
        n += 1

print(list(__enumerate(jewelry, start=0))) # [(0, 'gold'), (1, 'sapphire'), (2, 'silver'), (3, 'emerald'), (4, 'ruby')]



