# 백준  1260번 https://www.acmicpc.net/problem/1260
# DFS & BFS 그래프 탐색하기 

#vertax,edge,start
N,M,V = map(int,input().split())
coordnate = [[0]*(N+1) for _ in range(N+1)]

#간선만큼 돌며.. 
for _ in range(M):
  f_vertax,s_vertax = map(int,input().split())
  coordnate[f_vertax][s_vertax] = 1
  coordnate[s_vertax][f_vertax] = 1

# 4 5 1의 경우.. 
# [[0,0,0,0,0]
#  [0,0,1,1,1]
#  [0,1,0,0,1]
#  [0,1,0,0,1]
#  [0,1,1,1,0]]

#처음은 시작점,좌표,프린트할 리스트
def dfs(current_node,row,print):
  print +=[current_node]
  for search_node in range(len(row[current_node])):
    if row[current_node][search_node] and search_node not in print:
      print = dfs(search_node,row,print)
  return print

def bfs(root):
  queue = [root]
  print = [root]

  while queue:
    current_node = queue.pop(0) #1
    for search_node in range(len(coordnate[current_node])):   
      if coordnate[current_node][search_node] and search_node not in print:
        print+= [search_node]
        queue += [search_node]
  return print

print(" ".join(map(str,dfs(V,coordnate,[]))))
print(" ".join(map(str,bfs(V))))