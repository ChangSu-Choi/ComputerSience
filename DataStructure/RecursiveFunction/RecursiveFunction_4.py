# 10진수 정수를 입력하면 2진수, 8진수, 16진수로 변환하여 출력하는 프로그램을 재귀 함수를 이용하여 작성.
"""
  10진수: 37
   2진수: 1 0 0 1 0 1 
   8진수: 4 5 
  16진수: 2 5 

  10진수: 22
   2진수: 1 0 1 1 0 
   8진수: 2 6 
  16진수: 1 6 
  """
def notation(base, n, numberChar):
    """
    base: 진수
    n: 10진수 숫자
    numberChar: 16진수 표현 문자
    """
    # 목표: 주어진 10진수 숫자를 2/8/16진수로 변환하여 출력
    if n == 0:
        return
    else:
        notation(base, (n // base), numberChar)
        print(numberChar[n % base], end=' ')



# 결과 테스트 부분
import random
random.seed(0)  # 실험 결과 재현
num_test = 2  # 테스트 횟수
numberChar = ['0', '1', '2', '3', '4', '5', '6', '7',
              '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']  # 16진수 표현 문자

for _ in range(num_test):    
    number = random.randint(10, 40)
    print(f'  10진수: {number}')  # 10진수 출력
    print('   2진수:', end = ' ')
    notation(2, number, numberChar)  # 2진수 출력
    print('\n   8진수:', end = ' ')
    notation(8, number, numberChar)  # 8진수 출력
    print('\n  16진수:', end = ' ')
    notation(16, number, numberChar)  # 16진수 출력
    print('\n')