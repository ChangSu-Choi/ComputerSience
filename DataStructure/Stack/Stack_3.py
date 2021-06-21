# 스택함수를 이용하여 pushed 리스트에 대해서 popped 리스트 출력결과가 발생할 수 있는지 확인.
# (1) 입력 예시
# pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]
# (1) 출력 예시: True
# (1) 설명: 다음의 순서대로 push, pop 수행할 수 있으므로 True 출력
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# (2) 입력 예시
# pushed = [1, 2, 3, 4, 5], popped = [4, 3, 5, 1, 2]
# (2) 출력 예시: False
# (2) 설명: 1 은 2 이전에 pop 할 수 없음

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


    def validate_stack_sequences(self, pushed, popped):
        k = 0
        #self에 push를 시키고 popped배열과 self의 stack이 같으면 pop, 그렇지 않으면 다시 push
        for i in range(len(pushed)):
            self.push(pushed[i])
            if self.peek() != popped[k]:
                continue
            else:
                self.pop()         
                k += 1
        #마지막까지 push한 self는, self의 stack은 뒷번호부터 popped의 k번째 배열과 같아야함
        for i in range(self.top, -1, -1):
            if self.stack[i] == popped[k]:
                self.pop()
                k += 1
            else:
                return False         #같지 않다면 popped리스트의 출력결과가 발생 할 수 없음
        
        return True



test_stack = Stack()
pushed = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
popped = [[4, 5, 3, 2, 1], [4, 3, 5, 1, 2]]
for i in range(len(pushed)):
    print(test_stack.validate_stack_sequences(pushed[i], popped[i]))