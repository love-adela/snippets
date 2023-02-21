"""
* adjacent : 입력으로 주어지는 그래프 `dict`
* vertex : 시작정점 `int`
* candidates: 방문해야 할 정점 `queue`
* visiteed: 방문한 정점 `list`
"""

from collections import deque
def bfs(adjacent, vertex):
    d = deque([vertex]) # let d be a queue
    # label vertex as discovered
    distance = [-1]*(len(adjacent)+1)
    distance[vertex] = 0
    while d: # while d is not empty do
        p = d.popleft()
        for q in adjacent[p]:
            if distance[q] != -1:
                continue
            distance[q] = distance[p] + 1
            d.append(q)
    return distance

graph = {1:[2,3], 2:[3,4,5], 3:[5,7,8], 4:[5], 5:[6], 6:[], 7:[8], 8:[]}
print(bfs(graph, 1))

