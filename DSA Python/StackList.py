class Stack:
    def __init__(self):
        self.list = []
        self.length = 0
    def __str__(self):
        datas = self.list.reverse()
        datas = [str(x) for x in self.list]
        return '\n'.join(datas)
    def push(self,data):
        self.list.append(data)
        self.length += 1
    def pop(self):
        self.list.pop()
        self.length -= 1
    def peek(self):
        print("hello")
        return self.list[len(self.list) - 1]
    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False
    def dump():
        self.list = None
customStack = Stack()
customStack.push(1)
customStack.push(15)
customStack.push(2)
customStack.push(0)
customStack.push(9)
customStack.pop()
print(customStack.peek())
print(customStack.isEmpty())
print(customStack)
customStack.dump()
print(customStack)