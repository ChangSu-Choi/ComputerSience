# 주어진 이진 탐색 트리에서 트리 순회를 이용하여 k번째 작은 값을 출력.
# 출력 예시
# 임의의 숫자 배열: [3, 3, 0, 2, 4, 3, 3, 2, 3, 2]
# 2번째 작은 값: 2

class TreeNode:
    def __init__ (self):
        self.left = None
        self.data = None
        self.right = None


def generate_tree(sellAry):
    # 판매 물품 트리 생성
    node = TreeNode()
    node.data = sellAry[0]
    rootNode = node

    for number in sellAry[1:]:
        node = TreeNode()
        node.data = number

        current = rootNode
        while True:
            if number == current.data:
                #pass
                break
            if number < current.data:
                if current.left == None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right == None:
                    current.right = node
                    break
                current = current.right
    
    return rootNode


def traverse_node(root, result):
    # 이진 탐색 트리에서 작은 값부터 큰 값 순으로 순회 (트리 순회 이용하기)
    # 중위 순회 활용
    if root == None:
        return

    traverse_node(root.left, result)
    result.append(root.data)
    traverse_node(root.right, result)
 

    return result


# 실행 구문 (아래 코드를 수정하지 마시오.)
import random
random.seed(0)  # 결과 재현을 위한 seed 통일
node_array = list(random.randint(0, 5) for _ in range(10) )  # 임의의 숫자 배열
k = 2  # 2번째로 작은 값
result = []  # 순회한 값 리스트
print(f'임의의 숫자 배열: {node_array}')
rootNode = generate_tree(node_array)  # Tree 최상위 노드 (중복 X)
print(f'{k}번째 작은 값: {traverse_node(rootNode, result)[k - 1]}')