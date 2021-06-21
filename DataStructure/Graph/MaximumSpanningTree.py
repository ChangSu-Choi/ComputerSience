# 네트워크 속도가 높은 연결을 남기고 모든 도시가 연결되도록 가장 효율적인 해저 케이블망을 구성.
# 출력 예시
# ## 해저 케이블 연결을 위한 전체 연결도 ##
# 0	80	0	10	0	0	
# 80	0	0	40	70	0	
# 0	0	0	0	30	60	
# 10	40	0	0	50	0	
# 0	70	30	50	0	20	
# 0	0	60	0	20	0	

# ## 가장 효율적인 해저 케이블 연결도 ##
# 0	80	0	0	0	0	
# 80	0	0	0	70	0	
# 0	0	0	0	30	60	
# 0	0	0	0	50	0	
# 0	70	30	50	0	0	
# 0	0	60	0	0	0	

class Graph():
    def __init__ (self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g, cityAry):
    # 그래프 출력 (정점 정보 포함, print 함수 사용 시 end='\t')
    for row in range(g.SIZE):
        for col in range(g.SIZE):
            print(g.graph[row][col], end = '\t')
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
        for vortex in range(g.SIZE):
            if g.graph[current][vortex] != 0:
                if vortex not in visitedAry:
                    next = vortex
            
        if next != None:
            current = next
            stack.append(current)
            visitedAry.append(current)
        else:
            current = stack.pop()

    if find_vtx in visitedAry:
        return True  # 정점 연결 True
    else:
        return False  # 정점 연결 False
    


def efficient_cable_networks(g):
    # 최대 비용(높은 네트워크 속도) 신장 트리
    
    # 가중치 간선 배열 생성
    edgeAry = []
    for row in range(g.SIZE):
        for col in range(g.SIZE):
            if g.graph[row][col] != 0:
                edgeAry.append([g.graph[row][col], row, col])
    # item 0번째 기준(가중치)으로 오름차순 정렬
    from operator import itemgetter
    edgeAry = sorted(edgeAry, key=itemgetter(0), reverse=False)

    # 갱신할 가중치 간선 배열 생성(중복 제거)
    newAry = []
    for i in range(0,len(edgeAry),2):
        newAry.append(edgeAry[i])

    # 가중치가 낮은 간선부터 제거 (반복)
    index = 0
    while len(newAry) > g.SIZE - 1:
        weight = newAry[index][0]
        start = newAry[index][1]
        end = newAry[index][2]

        g.graph[start][end] = 0
        g.graph[end][start] = 0

        start_found = find_vertex(g,start)
        end_found = find_vertex(g,end)

        if start_found and end_found:
            del newAry[index]
        else:
            g.graph[start][end] = weight
            g.graph[end][start] = weight
            index += 1


# 실행 구문
cityAry = ['서울', '뉴욕', '런던', '북경', '방콕', '파리' ]  # 도시 배열
서울, 뉴욕, 런던, 북경, 방콕, 파리 = 0, 1, 2, 3, 4, 5  # 도시, 수치 매핑

G1 = Graph(6)  # 빈 그래프 생성
G1.graph[서울][뉴욕] = 80; G1.graph[서울][북경] = 10
G1.graph[뉴욕][서울] = 80; G1.graph[뉴욕][북경] = 40; G1.graph[뉴욕][방콕] = 70
G1.graph[런던][방콕] = 30; G1.graph[런던][파리] = 60
G1.graph[북경][서울] = 10; G1.graph[북경][뉴욕] = 40; G1.graph[북경][방콕] = 50
G1.graph[방콕][뉴욕] = 70; G1.graph[방콕][북경] = 50; G1.graph[방콕][런던] = 30; G1.graph[방콕][파리] = 20
G1.graph[파리][방콕] = 20; G1.graph[파리][런던] = 60;

print('## 해저 케이블 연결을 위한 전체 연결도 ##')
print_graph(G1, cityAry)  # 그래프 출력

print('## 가장 효율적인 해저 케이블 연결도 ##')
efficient_cable_networks(G1)  # 효율적인 해저 케이블 연결도 생성
print_graph(G1, cityAry)  # 그래프 출력