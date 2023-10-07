
class Node:
    def __init__(self, value):
        self.value = value
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
            result += str(node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
ll = LinkedList()
ll.append(7)
ll.append(1)
ll.append(6)

ll2 = LinkedList()
ll2.append(5)
ll2.append(9)
ll2.append(2)

def ll2num(linky):
    num = 0
    cursor = linky.head
    counter = 1
    while cursor is not None:
        num = num + cursor.value*counter
        cursor = cursor.next
        counter = counter*10
    return num
    
def num2ll(num):
    linky = LinkedList()
    num = str(num)[::-1]
    for i in range(len(num)):
        linky.append(int(num[i]))
    return linky
def sum_list(l1,l2):
    num = ll2num(l1) + ll2num(l2)
    return num2ll(num)
def printy(ll):
    string =''
    cursor = ll.head
    while cursor is not None:
        string += str(cursor.value) + ' -> '
        cursor = cursor.next
    print(string+" None")
printy(sum_list(ll,ll2))