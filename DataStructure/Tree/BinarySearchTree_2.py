# 편의점 판매 물품 종류 트리를 좌우 반전시키고 전위 순회하라.
# 출력 예시
# 오늘 판매된 종류(중복X) 트리 전위 순회 -->  바나나맛우유 레쓰비캔커피 도시락 츄파춥스 삼다수
# 오늘 판매된 종류(중복X) 좌우 반전 트리 전위 순회 -->  바나나맛우유 츄파춥스 삼다수 레쓰비캔커피 도시락
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

    for name in sellAry[1:]:
        node = TreeNode()
        node.data = name

        current = rootNode
        while True:
            if name == current.data:
                #pass
                break
            if name < current.data:
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


def preorder(node):
    # 전위 순회 구현
    if node == None:
        return
    print(node.data, end = ' ')
    preorder(node.left)
    preorder(node.right)


def invertTree(root):
    # 트리 노드들의 위치를 좌우 반전
    # 트리의 마지막 leaf 노드부터 반전시키면서 root방향으로 올라가기 (후위 순회)
    if root == None:
        return
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root


# 실행 구문
dataAry = ['바나나맛우유', '츄파춥스', '삼다수', '레쓰비캔커피', '도시락']  # 판매 물품 종류
rootNode = generate_tree(dataAry)  # Tree 최상위 노드
print('오늘 판매된 종류(중복X) 트리 전위 순회 --> ', end = ' ')
preorder(rootNode)
print('\n오늘 판매된 종류(중복X) 반전 트리 전위 순회 --> ', end = ' ')
preorder(invertTree(rootNode))