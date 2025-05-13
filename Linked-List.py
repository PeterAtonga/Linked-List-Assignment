class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, data):
        if index < 0:
            raise IndexError("Index must be non-negative")

        if index == 0:
            self.insert_at_start(data)
            return

        new_node = Node(data)
        curr = self.head
        count = 0

        while curr and count < index - 1:
            curr = curr.next
            count += 1

        if not curr:
            raise IndexError("Index out of bounds")

        new_node.next = curr.next
        curr.next = new_node

    def delete_at_index(self, index):
        if index < 0 or not self.head:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        count = 0

        while curr.next and count < index - 1:
            curr = curr.next
            count += 1

        if not curr.next:
            raise IndexError("Index out of bounds")

        curr.next = curr.next.next

    def search(self, value):
        curr = self.head
        index = 0
        while curr:
            if curr.data == value:
                return index
            curr = curr.next
            index += 1
        return -1

    def display(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(curr.data)
            curr = curr.next
        print("Linked List:", elements)



ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_start(5)
ll.insert_at_index(1, 7)
ll.display()  # Linked List (5, 7, 10)
print("Index of 7:", ll.search(7))  # Index of 7: 1
ll.delete_at_index(1)
ll.display()  # Linked List (5, 10)
