def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

print(middle('letter')) # 'ette'
print(middle('word'))   # 'or'
print(middle(' '))

def is_palindrome(param:str):
    return param == param[::-1]

print(is_palindrome('noon'))
print(is_palindrome('alphabet'))


