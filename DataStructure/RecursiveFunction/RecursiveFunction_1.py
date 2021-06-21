# 재귀함수
"""
2
1
발사
★
★★


5
4
3
2
1
발사
★
★★
★★★
★★★★
★★★★★
"""
def countDown(n):
    # 재귀호출 이용한 카운트다운 함수
    if n == 0:
        print("발사")
    else:
        print(n)
        countDown(n-1)


def printStar(n):
    # 재귀호출 이용한 별 출력 함수
    if n > 0:
        printStar(n-1)
        print('★'*n)
    else:
        return


# 결과 테스트 부분
import random
random.seed(1)  # 실험 결과 재현
num_test = 2  # 테스트 횟수

for i in range(num_test):
    value = random.randint(1, 5)  # 임의의 값 생성
    countDown(value)
    printStar(value)
    print('\n')