# Case1 : 반복문 내에 조건에 해당하는 값 출력하기
print("==================Case1==================")
# 입력 받은 n개만큼 0  ~  9  사이의 짝수 출력하기
# n 회 동안 짝수의 총합 출력하기 
n = int(input())
def even_sum():
    sum = 0
    for i in range(n):
        print(f'i : {i}')
        for j in range(9):
            if j % 2 == 0:
                print(j)
                sum += j
    return sum
              
print(f'{n}회 동안 짝수의 총합: {even_sum()}')

# Case2 : 한 번 입력으로 조건에 해당하는 값이 있는지 확인하기 (numbers)
# print("==================Case2==================")
# 입력받은 수 중 짝수가 있는지 확인하기
# input_numbers = [int(param) for param in input().strip()]
def any_even()->bool:
    for param in input_numbers:
        if param % 2 == 0:
            return True
    return False
          
# print(f'무작위 숫자 중 짝수가 있는지? {any_even()}')

# Case3 : 한 번 입력으로 조건에 해당하는 값이 있는지 확인하기 (string)
# print("==================Case3==================")
# input_string = input()
def any_lowercase():
    for param in input_string:
        if param.islower():
            print(param)
            return True
    return False
        
# print(f'무작위 문자열 중 소문자가 있는지?  {any_lowercase()}')

# Case4 : 한 번 입력으로 조건에 해당하는 값이 있는지 확인하기  -  flag 사용하기
print("==================Case4==================")
def any_uppercase():
    flag = False
    for param in input_string:
          flag = param.isupper()
          if flag == True:
              break
          print(param, flag)
    return flag

# print(f'무작위 문자열 중 대문자가 있는지? {any_uppercase()}')
