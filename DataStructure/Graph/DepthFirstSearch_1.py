# 그래프 출력과 정점 탐색(그래프 깊이 우선 탐색) 함수.
# 출력 예시
# ## 무방향 그래프 출력 ##
# 0	 0	1	1	
# 0	 0	1	0	
# 1	 1	0	1	
# 1	 0	1	0	

# ## 정점이 그래프에 연결되어 있는지 확인 ##
# 방문 순서 --> A C B D , 정점 A 연결: True
# 방문 순서 --> A C B D , 정점 B 연결: True
# 방문 순서 --> A C B D , 정점 C 연결: True
# 방문 순서 --> A C B D , 정점 D 연결: True

class Graph():
    def __init__ (self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g):
    # 그래프 출력 (print 함수 사용 시 end='\t')
    for row in range(g.SIZE):
        for col in range(g.SIZE):
            print(g.graph[row][col], end = '\t')
        print()
    print()

def find_vertex(g, find_vtx):
    stack = []  # 스택 초기화
    visitedAry = []  # 방문한 정점 초기화
    current = 0  # 시작 정점
    stack.append(current)
    visitedAry.append(current)
    # 정점 탐색(그래프 깊이 우선 탐색)
    while len(stack) > 0:
        next = None
        for vertex in range(g.SIZE):
            if g.graph[current][vertex] != 0:
                if vertex not in visitedAry:
                    next = vertex
                    break
        
        if next != None:
            current = next
            stack.append(current)
            visitedAry.append(current)
        else:
            current = stack.pop()


    print('방문 순서 -->', end=' ')
    for i in visitedAry:  # 정점 방문 순서 출력
        print(chr(ord('A') + i), end=' ')

    if find_vtx in visitedAry:
        return True  # 정점 연결 True
    else:
        return False  # 정점 연결 False


# 실행 구문
G1 = Graph(4)  # 빈 그래프 생성
G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print('## 무방향 그래프 출력 ##')
print_graph(G1)  # 그래프 출력

print('## 정점이 그래프에 연결되어 있는지 확인 ##')
for i in range(G1.SIZE):
    print(f', 정점 {chr(ord("A") + i)} 연결: {find_vertex(G1, i)}')  # 깊이 우선 탐색 함수 호출