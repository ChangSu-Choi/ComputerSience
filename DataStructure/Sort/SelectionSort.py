# 선택정렬 구현
"""
Input: [50, 98, 54, 6, 34, 66, 63, 52, 39, 62]
Sorted: [6, 34, 39, 50, 52, 54, 62, 63, 66, 98]
Output: 54

Input: [46, 75, 28, 65, 18, 37, 18, 97, 13, 80]
Sorted: [13, 18, 18, 28, 37, 46, 65, 75, 80, 97]
Output: 46
"""
def selectionSort(array):
    """
    array: 정렬할 배열
    """
    # 선택정렬된 배열 반환
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
    return array

# 결과 테스트 부분
import random
random.seed(0)  # 실험 결과 재현
num_test = 2  # 테스트 횟수
array_length = 10  # 배열 길이

for i in range(num_test):
    array = [random.randint(1, 100) for _ in range(array_length)]  # 임의의 배열 생성
    print(f'Input: {array}')
    array = selectionSort(array)  # 정렬된 배열 획득
    print(f'Sorted: {array}')
    print(f'Output: {array[len(array) // 2]}\n')  # 정렬 후, 중간값 출력