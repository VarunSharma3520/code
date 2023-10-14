class Node():
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.pre = None
        
class DLL():
    def __init__(self):
        self.head = None
        self.head = None
        self.length = 0
    
    def append(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.pre = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1
            
    def prepend(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.pre = node
            self.head = node
        self.length += 1

    def join(self,data,position):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        elif self.length <= position:
            self.append(data)
        else:
            counter = 0
            cursor = self.head
            while cursor is not None:
                if counter == position:
                    node.pre = cursor
                    node.next = cursor.next
                    cursor.next = node
                    cursor.next.pre = Node
                    break
                else:
                    counter += 1
                cursor = cursor.next
        self.length += 1

    def delete(self,position):
        if self.head == None:
            return -1
        elif position == 0:
            self.head = self.head.next
            self.head.pre = None
        elif position == -1:
            self.tail = self.tail.pre
            self.tail.next = None
        else:
            counter = 0
            cursor = self.head
            while cursor is not None:
                if counter == position - 1:
                    cursor.next = cursor.next.next
                    cursor.next.pre.pre = cursor
                    break
                else:
                    counter += 1
                cursor = cursor.next
        self.length -= 1

    def find(self,data):
        if self.head == None:
            return None
        else:
            counter = 0
            cursor = self.head
            while cursor is not None:
                if cursor.data == data:
                    return counter
                else:
                    counter += 1
                cursor = cursor.next

    def printf(self):
        cursor = self.head
        string = 'Head -> '
        while cursor is not None:
            string = string + str(cursor.data) + ' <=> '
            cursor = cursor.next
        print(string[:-4],'-> Tail','\n''self.length = ',self.length)

    def printb(self):
        cursor = self.tail
        string = 'Tail -> '
        while cursor is not None:
            string = string + str(cursor.data) + ' <=> '
            cursor = cursor.pre
        print(string[:-4],'-> Head','\n''self.length = ',self.length)

    def drop(self):
        cursor = self.head
        while cursor is not None:
            cursor.pre = None
            cursor = cursor.next
        self.head = None
        self.tail = None
        self.length = 0

dll = DLL()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.prepend(6)
dll.prepend(7)
dll.prepend(8)
dll.prepend(9)
dll.printf()
dll.join(999,2)
dll.delete(0)
dll.delete(-1)
dll.delete(3)
dll.printf()
print(dll.find(5))
dll.drop()


