# 재귀함수 구구단
"""
## 8단 ##
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
## 9단 ##
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
"""
def gugu(dan, num):
    # 목표: 단과 곱할 숫자 이용하여 재귀호출로 구구단 출력
    print(f'{dan} x {num} = {dan * num}')
    if num < 9:
        gugu(dan, num+1)



# 결과 테스트 부분
for dan in range(8, 10):
    print(f"## {dan}단 ##")
    gugu(dan, 1)