"""
C, R (= 열, 행) = 7, 6일 때

[6, 7, 8, 9, 10, 11, 12]
[5, 26, 27, 28, 29, 30, 13]
[4, 25, 38, 39, 40, 31, 14]
[3, 24, 37, 42, 41, 32, 15]
[2, 23, 36, 35, 34, 33, 16]
[1, 22, 21, 20, 19, 18, 17]
"""

C, R = map(int, input().split())
grid = [[0]* C for _ in range(R)]

count, offset = 0, 0

while R > 0 and C > 0:
    for i in range(offset+R-1, offset-1, -1):
        count += 1
        grid[i][offset] = count
    for j in range(offset+1, offset+C):
        count += 1
        grid[offset][j] = count

    for i in range(offset+1, offset+R):
        count += 1
        grid[i][offset+C-1] = count

    for j in range(offset+C-2, offset, -1):
        count += 1
        grid[offset+R-1][j] = count

    offset +=1 
    R -=2 
    C -=2 

for row in grid:
    print(row)
