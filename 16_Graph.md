# 그래프



- 자료구조
  - 비선형 자료
    - 트리
    - **그래프**





1. **인접행렬법**
   ![인접행렬법 이미지 검색결과](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F2637025057BBFC5D11)



2. 방향그래프
   ![방향그래프 이미지 검색결과](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRsYPD41H50TsyPtQXZUA3v7Z6VD5P-ZP-5G2AvW8TXrL_Iu7Pb)



3. **인접리스트**

   > 1이라는 키에 2, 3, 4 배열이 있다라고 생각

   ![인접리스트 이미지 검색결과](https://lh3.googleusercontent.com/22poilDCWxVN7yT5qhzxdzrw8en-V9qGjiTULqjtzDisaVWc4GdhtDOoVw1EP8Dcs2wcYF8WRBH1jEdnbm9HeDMsrCxOMWWCWzpm_zy6AnU3qD4Gk_aa76mul81GkqqS0hphsA)

   





##### 강사님 풀이

- 백준 13023문제

```python
# 강사님 풀이

V, Edge = map(int, input().split()) # 노드, 간선
M = [[0] * V for _ in range(V)] # 인접행렬 초기화
A1 = {node: [] for node in range(V)} # {node : [e1, e2]} 인접리스트 초기화
G = [[] for _ in range(V)] # key 가 숫자로 들어올때
F = []


for _ in range(Edge):
    f, t = map(int, input().split())
    # 1.인접행렬
    M[f][t] = M[t][f] = 1
    
    
    # 2.인접리스트 ( 딕셔너리 버전 )
    G[f].append(t) # 양방향
    G[t].append(f)
    
    # 3.인접리스트 ( 배열 버전 ) , 키가 숫자로 들어올때.
    
    
    # 4. edge 리스트
    F.append([f, t]) # 모든 연결된 간선들의 가능성
    F.append([t, f])
    
    
    for i in range(len(F)):
        for j in range(len(F)):
            A, B = F[i]
            C. D = F[j]
            
            if A == B or A == C or A == D or B == C or B == D or C == D:
                continue
            if not M[B][C]:
                continue
            for E in G[D]:
                if E == A or E == B or E == C or E== D:
                    continue
                print(1)
                sys.exit(0)
                
print(0)
```







### DFS ( 깊이 우선 탐색 )

```python
# 재귀 버전
# def DFS(v):
#     visited[v] = 1

#     print(v, end=' ')

#     for w in G[v]:
#         if not visited[w]:
#             DFS(w)




def DFS(v): # v부터 시작해서 가세요.
    stack = []
    stack.append(v) # 첫번째 방문노드
    visited[v] = 1
    print(v, end="-")

    while stack: # 방금 채운 스택이 없어질때까지.
        p = v
        for w in G[v]:
            if not visited[w]: # 방문안했다면
                stack.append(w) # w로 가시고
                v = w
                visited[w] = 1
                print(v, end="-")
                break
        else:
            if p == v:
                v = stack.pop()

import sys
sys.stdin = open('DFS_input.txt')

V, E = map(int, input().split())

G = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for i in range(E):
    u, v = map(int, input().split()) # u, v 노드와 엣지
    G[u].append(v)
    G[v].append(u)


DFS(1)
```

