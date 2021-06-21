# 버블정렬
"""
Input: [34, 98, 66, 6, 39, 50, 52, 54, 62, 63]
1번째 사이클: [34, 66, 6, 39, 50, 52, 54, 62, 63, 98]
2번째 사이클: [34, 6, 39, 50, 52, 54, 62, 63, 66, 98]
3번째 사이클: [6, 34, 39, 50, 52, 54, 62, 63, 66, 98]
4번째 사이클: [6, 34, 39, 50, 52, 54, 62, 63, 66, 98]
Sorted: [6, 34, 39, 50, 52, 54, 62, 63, 66, 98]

Input: [65, 97, 37, 75, 13, 46, 80, 18, 28]
1번째 사이클: [65, 37, 75, 13, 46, 80, 18, 28, 97]
2번째 사이클: [37, 65, 13, 46, 75, 18, 28, 80, 97]
3번째 사이클: [37, 13, 46, 65, 18, 28, 75, 80, 97]
4번째 사이클: [13, 37, 46, 18, 28, 65, 75, 80, 97]
5번째 사이클: [13, 37, 18, 28, 46, 65, 75, 80, 97]
6번째 사이클: [13, 18, 28, 37, 46, 65, 75, 80, 97]
7번째 사이클: [13, 18, 28, 37, 46, 65, 75, 80, 97]
Sorted: [13, 18, 28, 37, 46, 65, 75, 80, 97]
"""
def bubble_sort(array):
    """
    array: 임의의 배열
    """
    # 목표: 버블정렬을 이용하여 임의의 배열을 정렬하여 반환, 매 정렬 사이클 출력
    n = len(array)
    for i, end in enumerate(range(n-1, 0, -1)):
        is_change =False
        for curr in range(0, end):
            if array[curr] > array[curr + 1]:
                array[curr], array[curr + 1] = array[curr + 1], array[curr]
                is_change = True
        print(f'{i+1}번째 사이클: {array}')
        if not is_change:
            break


# 결과 테스트 부분
import random
random.seed(0)  # 실험 결과 재현
num_test = 2  # 테스트 횟수
array_length = 10  # 배열 길이

for i in range(num_test):
    array = [random.randint(1, 100) for _ in range(array_length)]  # 임의의 배열 생성
    array = list(set(array))  # unique 숫자 배열 생성
    print(f'Input: {array}')
    bubble_sort(array)  # 배열 버블정렬
    print(f'Sorted: {array}')
    print('')