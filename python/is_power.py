def is_power(a, b)->bool:
    if a // b == b: return True
    return False

print(is_power(16, 4))
print(is_power(27, 3))
