class Node():
    def __init__(self,data = None):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def prepend(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
            node.next = node
        else:
            node.next = self.head
            self.tail.next = node
            self.head = node
        self.length += 1

    def insert(self,data,index):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
            node.next = node
        else:
            cursor = self.head
            for _ in range(index-1):
                cursor = cursor.next
            node.next = cursor.next
            cursor.next = node
        self.length += 1
    def append(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
            node.next = node
        else:
            self.tail.next = node
            node.next = self.head
            self.tail = node
        self.length += 1

    def find(self,data):
        cursor = self.head
        counter = 0
        while cursor is not None:
            if cursor.data == data:
                return counter
            cursor = cursor.next
            counter += 1
            if cursor == self.head:
                break
        return None

    def get(self,index):
        cursor = self.head
        counter = 0
        while cursor is not None:
            if counter == index:
                return cursor.data
            cursor = cursor.next
            counter += 1
            if cursor == self.head:
                break
        return None

    def setat(self,data,index):
        cursor = self.head
        counter = 0
        while cursor is not None:
            if counter == index:
                cursor.data = data
            cursor = cursor.next
            counter += 1
            if cursor == self.head:
                break

    def showTime(self):
        cursor = self.head
        string = 'Head -> '
        while cursor is not None:
            string += str(cursor.data) + ' -> '
            cursor = cursor.next
            if cursor == self.head:
                break
        string += 'Tail'
        print(string)

    def popFirst(self):
        self.head = self.head.next
        self.tail.next = self.head
        self.length -= 1

    def pop(self,index):
        cursor = self.head
        for _ in range(index-1):
            cursor = cursor.next
        cursor.next = cursor.next.next
        self.length += 1

    def remove(self,data):
        if self.head is None:
            return -1
        else:    
            cursor = self.head
            while cursor is not None:
                if cursor.next.data == data:
                    cursor.next = cursor.next.next
                    break
                cursor = cursor.next
                if cursor == self.head:
                    break

    def drop(self):
        self.tail.next = None
        self.tail = None
        self.tail = None
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.insert(999,2)
ll.append(3)
ll.append(4)
ll.prepend(0)
ll.showTime()
print(ll.find(3))
print(ll.get(2))
ll.setat(456,2)
ll.pop(3)
ll.popFirst()
ll.remove(456)
ll.showTime()
ll.drop()