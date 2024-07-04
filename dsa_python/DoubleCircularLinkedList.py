class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.pre = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, data):
        node = Node(data)
        if self.head == None:
            node.pre = node
            node.next = node
            self.head = node
            self.tail = node
            self.length = 1
        else:
            node.next = self.head
            node.pre = self.tail
            self.head.pre = node
            self.tail.next = node
            self.head = self.head.pre
            self.length += 1

    def insert(self, data, index): #not working properly
        node = Node(data)
        if self.head == None:
            node.pre = node
            node.next = node
            self.head = node
            self.tail = node
            self.length = 1
        elif self.length < index:
            self.append(data)
        else:
            cursor = self.head
            for i in range(self.length - 1):
                if i == index:
                    node.pre = cursor
                    node.next = cursor.next
                    cursor.next.pre = node
                    cursor.next = node
                    self.length += 1
                    break
                cursor = cursor.next

    def append(self, data):
        node = Node(data)
        if self.head == None:
            node.pre = node
            node.next = node
            self.head = node
            self.tail = node
            self.length = 1
        else:
            node.pre = self.tail
            node.next = self.head
            self.tail.next = node
            self.head.pre = node
            self.tail = self.tail.next
            self.length += 1

    def find(self, data):
        cursor = self.head
        for i in range(self.length):
            if cursor.data == data:
                print(data,'found at:',i)
                break
            cursor = cursor.next

    def get(self, index):
        cursor = self.head
        for i in range(self.length):
            if i == index:
                print(cursor.data)
                break
            cursor = cursor.next

    def setat(self, data, index):
        cursor = self.head
        for i in range(self.length):
            if i == index:
                cursor.data = data
                break
            cursor = cursor.next

    def showTime(self):
        string = 'Head -> '
        cursor = self.head
        for i in range(self.length):
            string += str(cursor.data) + ' -> '
            cursor = cursor.next
        string += 'Tail'
        print(string)
        print('<self.length:', self.length, '>')

    def popFirst(self):
        if self.length == 0:
            return None
        else:
            pass

    def pop(self, index):
        pass

    def remove(self, data):
        pass

    def drop(self):
        pass


ll = LinkedList()
# ll.prepend(2)
# ll.prepend(99)
# ll.prepend(3)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(6)
ll.showTime()
ll.insert(999,0) # Not Working
# ll.prepend(1)
# ll.find(6)
# ll.get(2)
# ll.setat("Varun Sharma",2)
# ll.popFirst()
# ll.pop(1)
# ll.remove(5)
ll.showTime()
ll.drop()
