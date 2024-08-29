class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, x: int):
        self.stack1.append(x)
    
    def dequeue(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None

# Example usage:
q = QueueWithStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  # Output: 10
print(q.dequeue())  # Output: 20
print(q.dequeue())  # Output: 30
