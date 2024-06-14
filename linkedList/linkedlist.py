
class Node :
    def __init__(self, data):
        self.val = data
        self.next = None



class LinkedList:
    def __init__(self) -> None:
        self.head = None


    def add_first(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        return 
    
    def add_last(self, val):
        if self.head is None:
            self.head = Node(val)
            return 
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(val)
        return 
    
    def delete(self, val):
        if self.head is None:return 
        node = Node(0)
        node.next = self.head
        while node:
            if node.next.val == val:
                node.next = node.next.next
            node = node.next
        return 
    
    def iterate(self):
        if self.head == None:
            print('empty')
            return
        node = self.head
        while node:
            print(node.val , end="-> ")
            node = node.next

    def add_rec(self,node, val):
        if node.next == None:
            node.next = Node(val)
            return 
        self.add_rec(node.next, val)

    def reversing(self):
        if self.head is None:
            return 
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current 
            current = next 
        self.head = prev

        
    def mid_element_delete(self):
        if self.head.next == None:
            return None

        temp = Node(0)
        temp.next = self.head
        s = temp
        f = temp
        while f.next is not None and f.next.next is not None:
            s = s.next
            f = f.next.next
        s.next = s.next.next

l = LinkedList()
l.add_last(1)
l.add_last(4)
l.add_first(5)
l.iterate()
l.delete(4)
print()
l.iterate()
l.reversing()
print()
l.iterate()
    





    