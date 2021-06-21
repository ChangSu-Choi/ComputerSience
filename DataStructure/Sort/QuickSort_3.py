# 퀵정렬을 이용해서 배열에서 중복된 숫자를 출력.
"""
Input: [1, 5, 6, 7, 8, 9, 5, 5]
Sorted: [1, 5, 5, 5, 6, 7, 8, 9]
Duplicated: 5

Input: [2, 3, 4, 5, 9, 10, 6, 6]
Sorted: [2, 3, 4, 5, 6, 6, 9, 10]
Duplicated: 6

Input: [2, 3, 5, 6, 8, 9, 10, 7, 7]
Sorted: [2, 3, 5, 6, 7, 7, 8, 9, 10]
Duplicated: 7
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

def find_duplicate(array):
    """
    array: 정렬된 배열
    """
    # 배열에서 중복된 값 반환하기 (파이썬 내장함수, 패키지 사용불가)
    temp = array[0]
    for data in array[1:]:
        if temp == data:
            return data
        temp = data

    return

# 결과 테스트 부분
import random
random.seed(0)  # 실험 결과 재현
num_test = 3  # 테스트 횟수
array_length = 10  # 배열 길이

for i in range(num_test):
    array = [random.randint(1, 10) for _ in range(array_length)]  # 임의의 배열 생성
    array = list(set(array))
    array.append(i + 5)
    array.append(i + 5)
    print(f'Input: {array}')
    quick_sort(array)  # 배열 퀵정렬
    print(f'Sorted: {array}')
    print(f'Duplicated: {find_duplicate(array)}')
    print('')