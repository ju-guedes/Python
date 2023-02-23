class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # create function to add nodes
    def append(self, data):
        new_node = Node(data)

        # Verify if list is empty
        if self.head is None:
            self.head = new_node
            return

        # If it is not, find the last node
        current = self.head
        while current.next:
            current = current.next

        # the last node point to the new one as next
        current.next = new_node
