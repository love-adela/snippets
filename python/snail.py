# C: 열 (세로) R: 행 (가로)
"""
C, R = 4, 4일 때 
1  2  3  4
12 13 14 5
11 16 15 6
10  9  8 7
"""

# grid 만들기
C, R = map(int, input().split())
grid = [[0]* C for _ in range(R)]

count = 0
offset = 0 

# grid 채워넣기
while R > 0 and C > 0:
    for i in range(offset, offset+C):
        count += 1
        grid[offset][i] = count

    for i in range(offset+1, offset+R):
        count += 1
        grid[i][offset+C-1] = count

    for i in range(offset+C-2, offset-1, -1):
        count += 1
        grid[offset+R-1][i] = count

    for i in range(offset+R-2, offset, -1):
        count += 1
        grid[i][offset] = count

    offset += 1
    R -= 2
    C -= 2


# grid 출력
for param in grid:
    print(' '.join(list(map(str, param))))
