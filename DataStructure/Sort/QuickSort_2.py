# 퀵정렬을 이용하여 주어진 도서 배열을 정렬하고 이진검색으로 원하는 정보를 검색하여 출력.
"""
# 책장의 도서 ==> [['부활', '톨스토이'], ['신곡', '단테'], ['돈키호테', '세르반테스'], ['동물농장', '조지오웰'], ['데미안', '헤르만헤세'], ['파우스트', '괴테']]
# 도서명 색인표 ==> [('데미안', 4), ('돈키호테', 2), ('동물농장', 3), ('부활', 0), ('신곡', 1), ('파우스트', 5)]
# 작가명 색인표 ==> [('괴테', 5), ('단테', 1), ('세르반테스', 2), ('조지오웰', 3), ('톨스토이', 0), ('헤르만헤세', 4)]

데미안 의 작가는 헤르만헤세 입니다.
톨스토이 의 도서는 부활 입니다.
"""
def q_sort(array, start, end):
    """
    array: 임의의 배열
    start: 시작점
    end: 끝점
    """
    # 재귀함수를 이용한 퀵정렬
    if end <= start:
        return
    low = start
    high = end
    pivot = array[(low + high) // 2]  #중간값으로 피벗 설정
    while low <= high:
        while array[low] < pivot:
            low += 1
        while array[high] > pivot:
            high -= 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
            low += 1
            high -= 1
    
    mid = low

    q_sort(array, start, mid - 1)
    q_sort(array, mid, end)


def quick_sort(array):
    """
    array: 임의의 배열
    """
    # 퀵정렬을 이용하여 임의의 배열을 정렬하기
    q_sort(array, 0, len(array) - 1)


def make_index(array, pos):
    """
    array: [도서명, 작가명] 2차원 배열
    pos: 0은 도서명, 1은 작가명
    """
    # pos에 해당하는 값을 추출하여 정렬된 배열 반환하기
    sorted_array = []
    index = 0
    for data in array:
        sorted_array.append((data[pos], index))
        index += 1
    
    quick_sort(sorted_array)

    return sorted_array


def book_search(index_array, find_name):
    """
    index_array: 인덱스 배열
    find_name: 검색할 이름
    """
    # find_name에 해당하는 값을 이진검색하여 반환하기 (없으면 -1 반환)
    pos = -1
    start = 0
    end = len(index_array) - 1

    while start <= end:
        mid = (start + end) // 2
        if find_name == index_array[mid][0]:
            return index_array[mid][1]
        elif find_name > index_array[mid][0]:
            start = mid + 1
        else:
            end = mid - 1
    
    return pos

# 결과 테스트 부분 
book_array = [['부활', '톨스토이'], ['신곡', '단테'], ['돈키호테', '세르반테스'],
              ['동물농장', '조지오웰'], ['데미안','헤르만헤세'], ['파우스트', '괴테']]
book_index = []
auth_index = []

print('# 책장의 도서 ==>', book_array)
book_index = make_index(book_array, 0)  # ('도서명', book_array 순번) 배열
print('# 도서명 색인표 ==>', book_index)
auth_index = make_index(book_array, 1)  # ('저자명', book_array 순번) 배열
print('# 작가명 색인표 ==>', auth_index)
print('')

find_name = '데미안'
find_pos = book_search(book_index, find_name)
if find_pos != -1:
    print(find_name, '의 작가는', book_array[find_pos][1], '입니다.')
else:
    print(find_name, ' 책은 없습니다.')

find_name = '톨스토이'
find_pos = book_search(auth_index, find_name)
if find_pos != -1:
    print(find_name, '의 도서는', book_array[find_pos][0], '입니다.')
else:
    print(find_name, ' 작가는 없습니다.')