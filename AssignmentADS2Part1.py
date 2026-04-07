class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. 
    def add_to_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2.
    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # 3. 
    def remove_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    # 4. 
    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Список пуст")

    # 5. 
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # 6. 
    def insert_at(self, position, data):
        if position == 0:
            self.add_to_front(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current:
                current = current.next
        if not current:
            return
        new_node.next = current.next
        current.next = new_node

    # 7. 
    def remove_by_value(self, value):
        current = self.head
        if current and current.data == value:
            self.head = current.next
            return
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

    # 8. 
    def combine(self, other_list):
        if not self.head:
            self.head = other_list.head
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = other_list.head

    # 9.
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 10. 
    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def _sorted_insert(self, head_ref, new_node):
        if not head_ref or head_ref.data >= new_node.data:
            new_node.next = head_ref
            return new_node
        current = head_ref
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return head_ref