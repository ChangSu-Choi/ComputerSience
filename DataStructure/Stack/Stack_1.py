# 스택 함수의 예.
# 입력 예시: 삽입(파이썬, C, JAVA), 확인, 추출 3번, 종료
# 출력 예시:
# 삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> i
# 입력할 데이터 ==> 파이썬
# 스택 상태 :  ['파이썬', None, None, None, None, None, None, None, None, None]
# 삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> i
# 입력할 데이터 ==> C
# 스택 상태 :  ['파이썬', 'C', None, None, None, None, None, None, None, None]
# 삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> i
# 입력할 데이터 ==> JAVA
# 스택 상태 :  ['파이썬', 'C', 'JAVA', None, None, None, None, None, None, None]
# 삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> v
# 확인된 데이터 ==>  JAVA
# 스택 상태 :  ['파이썬', 'C', 'JAVA', None, None, None, None, None, None, None]
# 삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> e
# 추출된 데이터 ==>  JAVA
# 스택 상태 :  ['파이썬', 'C', None, None, None, None, None, None, None, None]
# 삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> e
# 추출된 데이터 ==>  C
# 스택 상태 :  ['파이썬', None, None, None, None, None, None, None, None, None]
# 삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> e
# 추출된 데이터 ==>  파이썬
# 스택 상태 :  [None, None, None, None, None, None, None, None, None, None]
# 삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> x
# 프로그램 종료!

class Stack:
    def __init__(self):
        self.size = 10
        self.stack = [ None for _ in range(self.size) ]
        self.top = -1

    def is_stack_full(self):
        if self.top == self.size - 1:
            return True
        else:
            False

    def is_stack_empty(self):
        if self.top == -1:
            return True
        else:
            False


    def push(self, data):
        if self.is_stack_full():
            return
        self.top += 1
        self.stack[self.top] = data
        


    def pop(self):
        if self.is_stack_empty():
            return
        data = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return data
    

    def peek(self):
        if self.is_stack_empty():
            return None
        return self.stack[self.top]


test_stack = Stack()
select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ").lower()

while select != 'x':
    if select == 'i':
        data = input("입력할 데이터 ==> ")
        test_stack.push(data)
        print("스택 상태 : ", test_stack.stack)
    elif select == 'e':
        data = test_stack.pop()
        print("추출된 데이터 ==> ", data)
        print("스택 상태 : ", test_stack.stack)
    elif select == 'v':
        data = test_stack.peek()
        print("확인된 데이터 ==> ", data)
        print("스택 상태 : ", test_stack.stack)
    else:
        print("입력이 잘못됨")

    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ").lower()

print("프로그램 종료!")