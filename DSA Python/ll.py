class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None
    
class LL():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.data)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    def append(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1 
    def prepend(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node
        self.length += 1
    def insert(self,data,index):
        node = Node(data)
        position = 0
        if self.head is None:
            print("Linked List is empty So Insert at 1 st postion")
            node = Node(data)
            self.head = node
            self.tail = self.head
        else:
            cursor = self.head
            while cursor is not None:
                position += 1
                cursor = cursor.next
                if index == position:
                    node.next = cursor.next
                    cursor.next = node
                    break
            else:
                print("position not found")
        self.length += 1       
    def traverse(self):
        if self.head is None:
            print("Empty List")
        else:
            cursor = self.head
            while cursor is not None:
                print(cursor.data)
                cursor = cursor.next
            print("< length :",self.length,">")
    def search(self,data):
        cursor = self.head
        counter=0
        while cursor is not None:
            
            if cursor.data == data:
                print(data,"is at",counter)
            cursor = cursor.next
            counter += 1
    def get(self,index):
        cursor = self.head
        counter=0
        while cursor is not None:
            if counter == index:
                print(cursor.data,"is on",index)
                print(cursor)
                break
            cursor = cursor.next
            counter += 1
    def set(self,index,data):
        cursor = self.head
        counter=0
        while cursor is not None:
            if counter == index:
                cursor.data = data
                break
            cursor = cursor.next
            counter += 1
    def pop(self,index):
        if index == 1:
            if self.length == 0:
                print("LL contain no element")
            else:
                self.head = self.head.next
        self.length -= 1
        if index == -1:
            cursor = self.head
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.length -= 1
    def remove(self,index):
        if self.head is None:
            print("Empty List Found:")
        else:
            counter = 0
            cursor = self.head
            while cursor is not None:
                pre = cursor
                cursor = cursor.next
                if index-1 == counter:
                    break
                counter +=1
            pre.next = cursor.next
            cursor = None
        self.length -= 1
    def dump(self):
        self.head = None
        self.tail = None
        self.length = 0
x = LL()
x.append(9)
x.append(11)
x.append(12)
x.prepend(1)
x.insert(100,1)
# x.traverse()
# x.search(9)
# x.get(4)
# x.set(2,10)
# x.set(0,2)
# x.append(13)
# x.pop(1)
# x.pop(-1)
# print(x)
# x.remove(1)
print(x)