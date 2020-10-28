fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

def count_items(item):
    counts = 0

    for fruit in fruits:
        if fruit == item:
            counts += 1
    return counts

print(count_items('수박'))
print(count_items('감'))

