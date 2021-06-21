# 큐 함수의 예.
# 입력 예시: 삽입(파이썬, C, JAVA), 확인, 추출 3번, 종료
# 출력 예시
# 삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 ==> i
# 입력할 데이터 ==> 파이썬
# 큐 상태 :  ['파이썬', None, None, None, None, None, None, None, None, None]
# 삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 ==> i
# 입력할 데이터 ==> C
# 큐 상태 :  ['파이썬', 'C', None, None, None, None, None, None, None, None]
# 삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 ==> i
# 입력할 데이터 ==> JAVA
# 큐 상태 :  ['파이썬', 'C', 'JAVA', None, None, None, None, None, None, None]
# 삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 ==> v
# 확인된 데이터 ==>  파이썬
# 큐 상태 :  ['파이썬', 'C', 'JAVA', None, None, None, None, None, None, None]
# 삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 ==> e
# 추출된 데이터 ==>  파이썬
# 큐 상태 :  [None, 'C', 'JAVA', None, None, None, None, None, None, None]
# 삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 ==> e
# 추출된 데이터 ==>  C
# 큐 상태 :  [None, None, 'JAVA', None, None, None, None, None, None, None]
# 삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 ==> e
# 추출된 데이터 ==>  JAVA
# 큐 상태 :  [None, None, None, None, None, None, None, None, None, None]
# 삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 ==> x
# 프로그램 종료!

class Queue:
    def __init__(self):
        self.size = 10
        self.queue = [ None for _ in range(self.size) ]
        self.front = -1
        self.rear = -1

    def is_queue_full(self):
        # 만약 큐 앞이 비어 있으면 한 칸 당기기
        if self.rear != self.size - 1:
            return False
        elif self.rear == self.size - 1 and self.front == -1:
            return True
        else:
            for i in range(self.front + 1, self.size):
                self.queue[i - 1] = self.queue[i]
                self.queue[i] = None
            self.front -= 1
            self.rear -= 1
            return False
                

    def is_queue_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False


    def en_queue(self, data):
        if self.is_queue_full():
            return
        self.rear += 1
        self.queue[self.rear] = data

    def de_queue(self):
        if self.is_queue_empty():
            return None
        self.front += 1
        data = self.queue[self.front]
        self.queue[self.front] = None
        return data


    def peek(self):
        if self.is_queue_empty():
            return None
        return self.queue[self.front + 1]



test_queue = Queue()
select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 ==> ").lower()

while select != 'x':
    if select == 'i':
        data = input("입력할 데이터 ==> ")
        test_queue.en_queue(data)
        print("큐 상태 : ", test_queue.queue)
    elif select == 'e':
        data = test_queue.de_queue()
        print("추출된 데이터 ==> ", data)
        print("큐 상태 : ", test_queue.queue)
    elif select == 'v':
        data = test_queue.peek()
        print("확인된 데이터 ==> ", data)
        print("큐 상태 : ", test_queue.queue)
    else :
        print("입력이 잘못됨")

    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 ==> ").lower()

print("프로그램 종료!")
