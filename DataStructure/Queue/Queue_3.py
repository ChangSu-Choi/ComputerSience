# 큐 함수를 이용하여 콜센터의 응답 대기 시간을 계산.
# 입력 예시: waitCall = [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3)]
# 출력 예시
# 귀하의 대기 예상시간은 0분입니다.
# 현재 대기 콜 -->  [None, None, None, None, None]
# 귀하의 대기 예상시간은 9분입니다.
# 현재 대기 콜 -->  [('사용', 9), None, None, None, None]
# 귀하의 대기 예상시간은 12분입니다.
# 현재 대기 콜 -->  [('사용', 9), ('고장', 3), None, None, None]
# 귀하의 대기 예상시간은 16분입니다.
# 현재 대기 콜 -->  [('사용', 9), ('고장', 3), ('환불', 4), None, None]
# 귀하의 대기 예상시간은 20분입니다.
# 현재 대기 콜 -->  [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), None]
# 최종 대기 콜 -->  [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3)]
# 프로그램 종료!

class Queue:
    def __init__(self):
        self.size = 5
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


    def calc_time(self):
        if self.is_queue_empty():
            return 0
        add = 0
        for i in range(self.rear + 1):
            add += self.queue[i][1]
        return add



test_queue = Queue()
waitCall = [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3)]


for i in range(len(waitCall)):
    print('귀하의 대기 예상시간은 ', test_queue.calc_time(), '분입니다.')
    print("현재 대기 콜 --> ", test_queue.queue)
    test_queue.en_queue(waitCall[i])


# 실행 구문
print("최종 대기 콜 --> ", test_queue.queue)
print("프로그램 종료!")