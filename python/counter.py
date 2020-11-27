from collections import Counter

"""
Counter is a dict subclass. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
"""

# 1. Make a new counter from Iterable or mapping
c = Counter() # a new, empty counter

# a new counter from an iterable
name = Counter('adela') # Counter({'a':2, 'd': 1, 'e': 1, 'l': 1})

# a new counter from a mapping
color = Counter({'red':4, 'blue':2}) # Counter({'red': 4, 'blue': 2})

# a new counter from keyword args
animals = Counter(cats=4, dogs=8) # Counter({'dogs': 8, 'cats': 4})

# 2. Find values from key
breakfast = Counter(['eggs', 'ham', 'sausage'])
brakfast['bacon'] # 0

# 3. Delete key
del breakfast['sausage']

# 4. Use Methods beyond those available for all dictionaries.

# `elements()`
alphabet = Counter(a=4, b=2, c=0, d=-2)
sorted(alphabet.elements()) # ['a', 'a', 'a', 'a', 'b', 'b']
# `most_common([n])
# if n is omitted or None, it returns all elements in the counter.
Counter('abracadabra').most_common(3) # [('a', 5), ('b', 2)', ('r', 2)]
# `subtract()`
Counter(a=4, b=2, c=0, d=-2).subtract(Counter(a=1, b=2, c=3, d=4)) # Counter({'a':3, 'b':0, 'c':-3, 'd':-6})

# Convert from a list of (elem, cnt) pairs
Counter(dict([('a', 2), ('d', 1), ('e', 1), ('l', 1)])) # Counter({'a': 2, 'd': 1, 'e': 1, 'l': 1})

# 5. Several mathematical operations are provided for combining Counter objects to produce multisets.

# Add
Counter(a=3, b=1) + Counter(a=1, b=2) # Counter({'a':3, 'b': 3})
# Subtract
Counter(a=3, b=1) - Counter(a=1, b=2) # Counter{'a':2}) (keeping only positive counts)
# Intersection: min(c[x], d[x])
Counter(a=3, b=1) & Counter(a=1, b=2) # Counter({'a':1, 'b':1})
# Union: max(c[x], d[x])
Counter(a=3, b=1) | Counter(a=1, b=2) # Counter({'a':3, 'b':2})
# Unary addition and subtraction
+Counter(a=2, b=-4) # Counter({'a':2})
-Counter(a=2, b=-4) # Counter({'b':-4})

# 6. Use `next()`
yolo = Counter({'kiki': 1})
list(yolo.elements()) # ['kiki']
next(list(yolo.elements())) 'kiki'
