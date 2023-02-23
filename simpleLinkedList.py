if __name__ == "__main__":
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

        # create function to return length
        def length(self):

            # Verify if list is empty
            if self.head is None:
                return 0

            # find the last node
            current, length = self.head, 0
            while current:
                length += 1
                current = current.next
            return length

        # create function to transform list to array
        def toarray(self):
            array = []

            # Verify if list is empty
            if self.head is None:
                return array

            # Append each node into array
            current = self.head
            while current:
                array.append(current.data)
                current = current.next
            return array

        # create function to display list
        def display(self):
            current = self.head
            while current:
                print(current.data)
                current = current.next

        # create function to reverse list
        def reverse(self):

            if self.head is None:
                return
            current = self.head
            next_node = current.next
            current.next.next = current
            current.next = None
            current = next_node
            while current.next is not None:
                next_node = current.next
                current.next.next = current
                current = next_node
            return

        # create function to get the index of a node

        # create function to search item in list

        # create function to remove first item

        # create function to remove last item

        # create function to insert from beginning

        # create function to insert from end

        # create function to remove by value

        # create function to change value of node

        # create function to insert by index


