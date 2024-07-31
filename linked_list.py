from node import Node

class LinkedList:
    def __init__(self):
        #Cabecera de la lista (primer elemento)
        self.head = None

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def delete(self, value):
        current = self.head
        previous = None

        while current and current.value != value:
            previous = current
            current = current.next

        if current is None:
            return False

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

        return True

    def display(self):
        if self.head is None:
            print("Empty list")
        else:
            current = self.head
            print(current.value, end=" -> ")
            while current:
                print(current.value, end=" -> ")
                current = current.next
            print("End")

    def shift(self):
        if self.head is None:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        return removed_value

    def unshift(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def add(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            previous = None
            current_position = 0
            while current and current_position < position:
                previous = current
                current = current.next
                current_position += 1
            if previous is None:
                self.head = new_node
            else:
                previous.next = new_node
            new_node.next = current
