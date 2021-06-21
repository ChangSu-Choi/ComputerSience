# 삽입정렬 구현
"""
Input: [18, 73, 98, 9, 33, 16, 64, 98, 58, 61]
Sorted: [9, 16, 18, 33, 58, 61, 64, 73, 98, 98]
Output: 61

Input: [84, 49, 27, 13, 63, 4, 50, 56, 78, 98]
Sorted: [4, 13, 27, 49, 50, 56, 63, 78, 84, 98]
Output: 56
"""
def insertionSort(array):
    """
    array: 정렬할 배열
    """
    # 목표: 삽입정렬된 배열 반환
    n = len(array)
    for end in range(1, n):
        for curr in range(end, 0, -1):
            if array[curr] < array[curr - 1]:
                array[curr], array[curr - 1] = array[curr - 1], array[curr]
    
    return array


# 결과 테스트 부분
import random
random.seed(1)  # 실험 결과 재현
num_test = 2  # 테스트 횟수
array_length = 10  # 배열 길이

for i in range(num_test):
    array = [random.randint(1, 100) for _ in range(array_length)]  # 임의의 배열 생성
    print(f'Input: {array}')
    array = insertionSort(array)  # 정렬된 배열 획득
    print(f'Sorted: {array}')
    print(f'Output: {array[len(array) // 2]}\n')  # 정렬 후, 중간값 출력