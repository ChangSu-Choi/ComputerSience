# 책 이름 트리와 작가 이름 트리를 구성.
# 출력 예시
# 찾을 정보: 책, 동물농장
# 동물농장 을(를) 찾음
# 찾을 정보: 작가, 헤르만헤세
# 헤르만헤세 을(를) 찾음
# 찾을 정보: 책, 자료구조
# 자료구조 이(가) 목록에 없음
# 찾을 정보: 작가, 튜링
# 튜링 이(가) 목록에 없음

class TreeNode:
    def __init__ (self):
        self.left = None
        self.data = None
        self.right = None

def generate_book_tree(bookAry):
    # 책 이름 트리 생성
    node = TreeNode()
    node.data = bookAry[0][0]
    rootBook = node

    for book in bookAry[1:]:
        name = book[0]
        node = TreeNode()
        node.data = name

        current = rootBook
        while True:
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
    
    return rootBook



def generate_author_tree(bookAry):
    # 작가 이름 트리 생성
    node = TreeNode()
    node.data = bookAry[0][1]
    rootAuthor = node


    for book in bookAry:
        name = book[1]
        node = TreeNode()
        node.data = name

        current = rootAuthor
        while True:
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

    return rootAuthor




def find_node(root, findName):
    # 이진 탐색 트리 검색
    current = root
    while True:
        if findName == current.data:
            result = f'{findName} 을(를) 찾음'
            break
        elif findName < current.data:
            if current.left == None:
                result = f'{findName} 이(가) 목록에 없음'
                break
            current = current.left
        else:
            if current.right == None:
                result = f'{findName} 이(가) 목록에 없음'
                break
            current = current.right
                
    return result


# 실행 구문
bookAry = [ ['어린왕자', '쌩떽쥐베리'],['이방인', '까뮈'], ['부활', '톨스토이'],
            ['신곡', '단테'], ['돈키호테', '세브반테스'], ['동물농장', '조지오웰'],
            ['데미안','헤르만헤세'], ['파우스트', '괴테'], ['대지', '펄벅'] ]  # [책, 작가] 순
import random
random.seed(0)
random.shuffle(bookAry)
rootBook = generate_book_tree(bookAry)
rootAuthor = generate_author_tree(bookAry)

test_set = [ [0, '동물농장'], [1, '헤르만헤세'], [0, '자료구조'], [1, '튜링'] ]
category = ['책', '작가']
for bookOrAuth, findName in test_set:
    if bookOrAuth == 0:
        root = rootBook
    else:
        root = rootAuthor
    print(f'찾을 정보: {category[bookOrAuth]}, {findName}')
    print(find_node(root, findName))