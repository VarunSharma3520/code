# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with 
# datas 3 and 4, we return the second one.

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LL():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
    def find_middle(self):
        cursor = self.head
        n = self.length//2
        count = 0
        string = ""
        while cursor is not None:
            count += 1 
            if n < count:
                print(cursor.data)
            cursor = cursor.next
    def showTime(self):
        cursor = self.head
        string = ""
        while cursor is not None:
            string += str(cursor.data) + " -> "
            cursor = cursor.next
        print("head -> ",string,"None ")

linky = LL()
linky.append(2)
linky.append(3)
linky.append(4)
linky.append(5)
linky.append(6)
linky.append(7)
linky.showTime()
linky.find_middle()



