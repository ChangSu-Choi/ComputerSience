# 이진 탐색 트리를 활용하여 편의점에서 판매된 물건에서 중복을 제외하고 출력.
# 출력 예시
# 오늘 판매된 물건(중복O) --> ['레쓰비캔커피', '레쓰비캔커피', '츄파춥스', '바나나맛우유', '도시락', '레쓰비캔커피', '레쓰비캔커피', '바나나맛우유', '레쓰비캔커피', '바나나맛우유']
# 오늘 판매된 종류(중복X) 전위 순회 -->  레쓰비캔커피 도시락 츄파춥스 바나나맛우유
# 오늘 판매된 종류(중복X) 중위 순회 -->  도시락 레쓰비캔커피 바나나맛우유 츄파춥스
# 오늘 판매된 종류(중복X) 후위 순회 -->  도시락 바나나맛우유 츄파춥스 레쓰비캔커피

import random


class TreeNode:
    def __init__ (self):
        self.left = None
        self.data = None
        self.right = None


def generate_tree(sellAry):
    # 판매 물품 트리 생성
    node = TreeNode()
    node.data = sellAry[0]
    root = node

    for name in sellAry[1:]:
        node = TreeNode()
        node.data = name
        
        current = root
        while True:
            if name == current.data:
                #pass
                break
            elif name < current.data:
                if current.left == None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right == None:
                    current.right = node
                    break
                current = current.right
    return root


def preorder(node):
    # 전위 순회 구현
    if node == None:
        return
    
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    # 중위 순회 구현
    if node == None:
        return
    inorder(node.left)
    print(node.data, end = ' ')
    inorder(node.right)


def postorder(node):
    # 후위 순회 구현
    if node == None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.data, end = ' ')

# 실행 구문
random.seed(0)  # 결과 재현을 위해 seed 값 통일
dataAry = ['츄파춥스', '삼다수', '바나나맛우유', '레쓰비캔커피', '도시락']  # 판매 물품 종류
sellAry = [random.choice(dataAry) for _ in  range(10)]  # 오늘 판매한 물품 목록
print(f'오늘 판매된 물건(중복O) --> {sellAry}')
rootNode = generate_tree(sellAry)  # Tree 최상위 노드
print('오늘 판매된 종류(중복X) 전위 순회 --> ', end = ' ')
preorder(rootNode)
print('\n오늘 판매된 종류(중복X) 중위 순회 --> ', end = ' ')
inorder(rootNode)
print('\n오늘 판매된 종류(중복X) 후위 순회 --> ', end = ' ')
postorder(rootNode)