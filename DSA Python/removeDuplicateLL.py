class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(node.data)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(4)
ll.append(4)
ll.append(5)

def remove_duplicates(ll):
    listy = []
    cursor = ll.head
    while cursor is not None:
        if cursor.data not in listy:
            listy.append(cursor.data)
        cursor = cursor.next
    ll.head = None
    ll.tail = None
    for i in listy:
        ll.append(i)
    return ll
    
def printy(ll):
    cursor = ll.head
    while cursor is not None:
        print(cursor.data)
        cursor = cursor.next
printy(remove_duplicates(ll))