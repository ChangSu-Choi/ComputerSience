# 문제 2. 최소 비용의 자전거 도로 연결도를 출력하라.
# 출력 예시
# ## 자전거 도로 건설을 위한 전체 연결도 ##
#  	춘천	서울	속초	대전	광주	부산	
# 춘천	0	10	15	0	0	0	
# 서울	10	0	40	11	50	0	
# 속초	15	40	0	12	0	0	
# 대전	0	11	12	0	20	30	
# 광주	0	50	0	20	0	25	
# 부산	0	0	0	30	25	0	

# ## 최소 비용의 자전거 도로 연결도 ##
#  	춘천	서울	속초	대전	광주	부산	
# 춘천	0	10	0	0	0	0	
# 서울	10	0	0	11	0	0	
# 속초	0	0	0	12	0	0	
# 대전	0	11	12	0	20	0	
# 광주	0	0	0	20	0	25	
# 부산	0	0	0	0	25	0	

class Graph():
    def __init__ (self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g, nameAry):
    # 그래프 출력 (정점 정보 포함, print 함수 사용 시 end='\t')
    print(' ', end='\t')
    for vortex in range(g.SIZE):
        print(nameAry[vortex], end = '\t')
    print()
    for row in range(g.SIZE):
        print(nameAry[row], end = '\t')
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


def minimum_spanning_tree(g):
    # 최소 비용 신장 트리

    # 가중치 간선 배열 생성
    edgeAry = []
    for row in range(g.SIZE):
        for col in range(g.SIZE):
            if g.graph[row][col] != 0:
                edgeAry.append([g.graph[row][col], row, col])


    # item 0번째 기준(가중치)으로 내림차순 정렬
    from operator import itemgetter
    edgeAry = sorted(edgeAry, key=itemgetter(0), reverse=True)
    # 갱신할 가중치 간선 배열 생성(중복 제거)
    newAry = []
    for i in range(0,len(edgeAry), 2):
        newAry.append(edgeAry[i])

    # 가중치가 높은 간선부터 제거 (반복)
    index = 0
    while len(newAry) > g.SIZE - 1:
        weight = newAry[index][0]
        start = newAry[index][1]
        end = newAry[index][2]

        g.graph[start][end] = 0
        g.graph[end][start] = 0

        start_found = find_vertex(g, start)
        end_found = find_vertex(g, end)

        if start_found and end_found:
            del newAry[index]
        else:
             g.graph[start][end] = weight
             g.graph[end][start] = weight
             index += 1

        
    

# 실행 구문
nameAry = ['춘천', '서울', '속초', '대전', '광주', '부산']  # 도시 배열
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5  # 도시명, 숫자 매핑

G1 = Graph(6)  # 빈 그래프 생성
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12; G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25

print('## 자전거 도로 건설을 위한 전체 연결도 ##')
print_graph(G1, nameAry)  # 그래프 출력

print('## 최소 비용의 자전거 도로 연결도 ##')
minimum_spanning_tree(G1)
print_graph(G1, nameAry)  # 그래프 출력