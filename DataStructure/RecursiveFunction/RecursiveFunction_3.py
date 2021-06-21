# 재귀함수로 피보나치 구현
# 피보나치 수 --> 0 1 1 2 3 5 8 13 21 34 
def fibo(n):
    # 목표: n번째 피보나치 수 계산
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


# 결과 테스트 부분
print('피보나치 수 --> 0 1', end=' ')
for i in range(2, 10):
    print(fibo(i), end=' ')