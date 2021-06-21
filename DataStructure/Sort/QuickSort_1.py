# 퀵정렬
"""
Input: [32, 33, 21, 28, 36, 35, 32, 29, 35, 31]
Sorted: [21, 28, 29, 31, 32, 32, 33, 35, 35, 36]

Input: [38, 26, 36, 24, 29, 24, 23, 39, 28, 37]
Sorted: [23, 24, 24, 26, 28, 29, 36, 37, 38, 39]
"""
def q_sort(array, start, end):
    """
    array: 임의의 배열
    start: 시작점
    end: 끝점
    """
    # 목표: 재귀함수를 이용한 퀵정렬
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
    # 목표: 퀵정렬을 이용하여 임의의 배열을 정렬하기
    q_sort(array, 0, len(array) - 1)
 

# 결과 테스트 부분
import random
random.seed(0)  # 실험 결과 재현
num_test = 2  # 테스트 횟수
array_length = 10  # 배열 길이

for i in range(num_test):
    array = [random.randint(20, 40) for _ in range(array_length)]  # 임의의 배열 생성
    print(f'Input: {array}')
    quick_sort(array)  # 배열 퀵정렬
    print(f'Sorted: {array}')
    print('')