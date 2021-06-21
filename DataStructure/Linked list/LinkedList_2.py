# 2차원의 데이터를 사용하는 단순 연결 리스트 생성
# 출력 예시
# ## 초기 연결 리스트 ##
# ['파이썬', 1] ['C', 2], ['C++', 3], ['JAVA', 4], ['MATLAB', 5],
# ## R 삽입 결과 ##
# ['R', 0] ['파이썬', 1], ['C', 2], ['C++', 3], ['JAVA', 4], ['MATLAB', 5],
# ## C++ 삭제 결과 ##
# ['R', 0] ['파이썬', 1], ['C', 2], ['JAVA', 4], ['MATLAB', 5],
# ## MATLAB 검색 결과 ##
# ['MATLAB', 5]

class Node():
    def __init__ (self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end = ' ')
    while current.link != None:
        current = current.link
        print(current.data, end = ', ')


def insertNode(findData, insertData):
    global memory, head, current, pre

    # 코드 작성 부분
    if head.data[0] == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)

    else:
        current = head
        find_flag = False
        while current.link != None:
            pre = current
            current = current.link
            if current.data[0] == findData:
                node = Node()
                node.data = insertData
                node.link = current
                pre.link = node
                memory.append(node)
                break

        if not find_flag:
            node = Node()
            node.data = insertData
            current.link = node
            memory.append(node)



def deleteNode(deleteData):
    global memory, head, current, pre

    # 코드 작성 부분

    if head.data[0] == deleteData:
        current = head
        head = head.link
        del current
    else:
        current = head
        while current.link != None:
            pre = current
            current = current.link 
            if current.data[0] == deleteData:
                pre.link = current.link
                del current
                break




def findNode(findData):
    global memory, head, current, pre
    current = head

    # 코드 작성 부분
    if head.data == findData:
        result = head
    else:
        current = head
        while current.link != None:
            current = current.link
            if current.data[0] == findData:
                result = current
                break

    return result


# 실행 구문 (아래 코드를 수정하지 마시오.)
memory = []
head, current, pre = None, None, None
dataArray = [ ['파이썬', 1], ['C', 2], ['C++', 3], ['JAVA', 4], ['MATLAB', 5] ]  # 2차원 데이터

node = Node()			# 첫 번째 노드
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:] :		# 두 번째 노드부터
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

print('## 초기 연결 리스트 ##')
printNodes(head)

print('\n## R 삽입 결과 ##')
insertNode('파이썬', ['R', 0])
printNodes(head)

print('\n## C++ 삭제 결과 ##')
deleteNode('C++')
printNodes(head)

print('\n## MATLAB 검색 결과 ##')
f_node = findNode('MATLAB')
print(f_node.data)