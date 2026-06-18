'''
Linked List (Singly)

[Data, Address(is the pointer to next node)]

[Data | Address] -> [Data | Address] -> [Data | Address] -> [Data | Address] -> 

in Linked list, to locate the elem its time complexity is O(n), for the deletion or insertion it is O(1)

it has no memory waste, but is memory consuming(because of additional pointers)

'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
                if current == None:
                    return
                prev.next = current.next
                current = None

    def insert(self, new_elem, position):
        count = 1
        current = self.head
        if position == 1:
            new_elem.next = current.head
            self.head = new_elem
        while current:
            '''
                [0]                [1]          [2]             [3]
            [head | next] ->(insert here) [head | next] -> [head | next] -> 
            [0].next -> new_elem.head
            new_elem.head -> [2].head
            '''
            if count+1 == position:
                new_elem.next = current.next
                current.next = new_elem
                return
            else:
                count+=1
                current = current.next
            