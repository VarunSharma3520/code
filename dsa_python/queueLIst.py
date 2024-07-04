class Queue:
    def __init__(self):
        self.list = []
    def showTime(self):
        print(self.list)
    def enqueue(self,data):
        self.list.append(data)
    def dequeue(self):
        if self.isEmpty():
            print("Queue contain no element")
        else:
            self.list.pop(0)
    def isEmpty(self):
        if len(self.list) == 0:
            return True
        return False
    def peek(self):
        if self.isEmpty():
            print("Queue contain no element")
        else:
            print(self.list[0])
customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(3)
customQueue.isEmpty()
customQueue.enqueue(5)
customQueue.showTime()
customQueue.dequeue()
customQueue.peek()
customQueue.showTime()