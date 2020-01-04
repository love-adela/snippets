# Iterable: iter() 함수에 인자로 넣을수 있는 모든것 (list, set, dict, range, ...)
# Container: 값이 들어있는 무언가, Iterator의 부분집합 (list, set, ...)

# iter : Iterable → Iterator
#
# Example:
#   iter(Iterable) ⇒  Iterator
#   iter([1, 2, 3]) ⇒  <list_iterator ...>
#   iter(range(10)) ⇒  <range_iterator ...>


# Container
my_list = [1, 2, 3]
my_set = {'a', 'b', 'c'}
my_dict = {'a': 100, 'b': 200, 'c': 300}
my_tuple = (1, 2, 3)

# All Container is Iterable
it = iter(my_list)
it = iter(my_set)
it = iter(my_dict)
it = iter(my_tuple)
next(it)
next(it)
next(it)
# it.next() <- Syntax for Python 2 only

# All Iterable is not always Container
my_range = range(30, 40)
it = iter(my_range)
next(it)
next(it)
next(it)

# Conclusion: Container ⊊ Iterable


# All Iterator is Iterable
my_iter = iter(range(30, 40))
it = iter(my_iter)
next(it)
next(it)
next(it)


# Generator: yield 문이 들어간 함수 === "generator iterator"를 반환하는 함수
#            Generator는 함수의 일종
#                                       "generator iterator"는 iterator의 일종
#                                       "generator iterator"는 <generator object ...>

from typing import Generator, Iterator

# yield statement만 존재하는 제네레이터, None을 암시적으로 리턴함
#                   -> Generator[...]       라고 쓰여져있지만 generator를 반환하는게 아니라
#                                           generator iterator를 반환하는것임
def one_two_three() -> Generator[int, None, None]:
    '''
    it = one_two_three()
    next(it) # 1
    next(it) # 2
    next(it) # 3
    next(it) # "StopIterator" 익셉션 발생
    '''

    yield 1
    yield 2
    yield 3

# 아래와 같이 인자가 생략된 좀 더 간단한 버전을 쓸 수 있음
# Generator[T, None, None] == Iterator[T]
def one_two() -> Iterator[int]:
    yield 1
    yield 2

# 무한한 제네레이터도 가능하다
def positive_number() -> Iterator[int]:
    i = 1
    while True:
        yield i
        i += 1

# 제네레이터 버전 피보나치도 짤 수 있음
def generator_fib(n) -> Iterator[int]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 무한버전 제네레이터 피보나치
def infinite_generator_fib() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

# 함수에서 쓸 수 있는 문법은 제네레이터에서도 쓸 수 있다
# Default Parameter 예시
def selected_fibo(end=None) -> Iterator[int]:
    a, b = 0, 1
    if end is None:
        while True:
            yield a
            a, b = b, a+b
    else:
        for _ in range(end):
            yield a
            a, b = b, a+b

# selected_fibo() # 0, 1, 1, 2, 3, 5, 8, ...
# selected_fibo(5) # 0, 1, 1, 2, 3


it = iter(my_list)      # <list_iterator ...>
it = iter(my_set)       # <set_iterator ...>
it = iter(my_dict)      # <dict_keyiterator ...>
it = iter(my_tuple)     # <tuple_iterator ...>
it = iter(my_range)     # <range_iterator ...>
it = one_two_three()    # <generator object ...> = "generator iterator"


# yield statement와 return문이 모두 있는 제네레이터
# 잘 안씀
def one_two_three_done() -> Generator[int, None, str]:
    '''
    it = one_two_three()
    next(it) # 1
    next(it) # 2
    next(it) # 3
    next(it) # "StopIterator: Done" 익셉션 발생
    '''

    yield 1
    yield 2
    yield 3
    return 'Done'


# yield expression이 있어서 .send() 를 불러줘야하는 제네레이터
def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
            sent = yield round(sent)
    return 'Done'
