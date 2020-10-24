odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8]


def is_even(lst:list):
    for elem in lst:
        if elem % 2 != 0:
            return False
    return True

#print(is_even(odds))
#print(is_even(evens))
#print(is_even([2, 4, 6, 8, 9]))

# 짝수가 단 하나라도 있는지 검사
def main(lst):
    for elem in lst:
        if elem % 2 == 0:
            return True
    return False

#print(main(evens))
#print(main(odds))
#print(main([2, 4, 6, 8, 9]))

# 짝수가 최소 2개 있는지 검사
def a(lst):
    count = 0
    for elem in lst:
        if elem % 2 == 0:
            count +=1 
    if count >= 2:
        return True
    else:
        return False

#print(a(evens))
#print(a(odds))
#print(a([2, 3, 5, 7, 9]))

# 배열의 절반 이상이 짝수인지 검사
def b(lst):
    count = 0
    for elem in lst:
        if elem % 2 == 0:
            count += 1
    if count * 2 >= len(lst): # 양변에 2 곱함
        return True
    else:
        return False

print(b([1, 3, 5, 6, 8])) # False
print(b([2, 4, 5, 7])) # True

# 배열의 모든 원소가 어떤 자연수의 거듭제곱인지 검사
def c(lst):
    for elem in lst:
        n = elem ** 0.5
        if int(n) != n:
            return False
    return True
print(c([1, 4, 9, 16])) # True
print(c([1, 2, 3, 4])) # False

