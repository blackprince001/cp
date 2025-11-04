class Node:
    def __init__(self, data):
        self.data = data
        self.prev: "Node | None" = None
        self.next: "Node | None" = None


class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head: "Node | None" = None
        self.tail: "Node | None" = None

    def is_empty(self):
        return self.size == 0

    def add_last(self, node: Node):
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def add_at_n(self, n: int, node: Node):
        if n > self.size + 1 or n <= 0:
            return self.add_last(node)

        if n == 1:
            return self.add_first(node)

        # traverse to the node before the insertion point (n-1)
        curr = self.head
        for _ in range(n - 2):
            curr = curr.next

        # check if we are inserting at the end (n = size + 1)
        if curr is self.tail:
            return self.add_last(node)

        next_node = curr.next

        node.prev = curr
        node.next = next_node

        curr.next = node
        next_node.prev = node

        self.size += 1

    def add_first(self, node: Node):
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return None

        removed_node = self.head

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        removed_node.next = None
        self.size -= 1
        return removed_node

    def remove_last(self):
        if self.is_empty():
            return None

        removed_node = self.tail

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        removed_node.prev = None
        self.size -= 1
        return removed_node

    def remove_at_n(self, n: int):
        if self.is_empty() or n < 1 or n > self.size:
            return None

        if n == 1:
            return self.remove_first()

        if n == self.size:
            return self.remove_last()

        curr = self.head
        for _ in range(n - 1):
            curr = curr.next

        removed_node = curr

        prev_node = removed_node.prev
        next_node = removed_node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        removed_node.prev = None
        removed_node.next = None

        self.size -= 1
        return removed_node


def print_dll(dll, test_name):
    print(f"\n--- {test_name} ---")
    if dll.is_empty():
        print("List: [Empty]")
        print(f"Size: {dll.size}, Head: {dll.head}, Tail: {dll.tail}")
        return

    forward_list = []
    curr = dll.head
    while curr:
        forward_list.append(curr.data)
        curr = curr.next
    print(f"Forward: {forward_list}")

    backward_list = []
    curr = dll.tail
    while curr:
        backward_list.append(curr.data)
        curr = curr.prev
    print(f"Backward: {backward_list}")

    print(f"Size: {dll.size}")
    print(f"Head: {dll.head.data} (Prev: {dll.head.prev})")
    print(f"Tail: {dll.tail.data} (Next: {dll.tail.next})")

    if dll.size > 1:
        second = dll.head.next
        second_to_last = dll.tail.prev
        print(f"Check: {second.data}'s prev is {second.prev.data}")
        print(f"Check: {second_to_last.data}'s next is {second_to_last.next.data}")
    print("--------------------")


def tests():
    dll = DoublyLinkedList()

    print_dll(dll, "Test 1a: Empty List Initial")
    dll.add_first(Node("C"))
    print_dll(dll, "Test 1b: add_first (Size 1)")

    dll.add_first(Node("B"))
    dll.add_last(Node("D"))
    print_dll(dll, "Test 1c: add_first and add_last (Size 3)")

    dll.add_first(Node("A"))
    print_dll(dll, "Test 1d: Final Insertion (Size 4)")

    dll_insert = DoublyLinkedList()
    dll_insert.add_last(Node(10))
    dll_insert.add_last(Node(30))

    dll_insert.add_at_n(2, Node(20))
    print_dll(dll_insert, "Test 2a: Insert Middle (n=2)")

    dll_insert.add_at_n(1, Node(5))
    print_dll(dll_insert, "Test 2b: Insert Head (n=1)")

    dll_insert.add_at_n(10, Node(40))
    print_dll(dll_insert, "Test 2c: Insert Past Tail (n > size)")

    dll_remove = DoublyLinkedList()
    dll_remove.add_last(Node("Alpha"))
    dll_remove.add_last(Node("Beta"))
    dll_remove.add_last(Node("Gamma"))
    print_dll(dll_remove, "Test 3a: Initial List for Removal")

    removed_first = dll_remove.remove_first()
    print(f"Removed Node (First): {removed_first.data}")
    print_dll(dll_remove, "Test 3b: After remove_first")

    removed_last = dll_remove.remove_last()
    print(f"Removed Node (Last): {removed_last.data}")
    print_dll(dll_remove, "Test 3c: After remove_last")

    removed_last_single = dll_remove.remove_last()
    print(f"Removed Node (Single): {removed_last_single.data}")
    print_dll(dll_remove, "Test 3d: After remove_last (Single Node)")

    dll_remove_at = DoublyLinkedList()
    dll_remove_at.add_last(Node(100))
    dll_remove_at.add_last(Node(200))
    dll_remove_at.add_last(Node(300))
    removed_middle = dll_remove_at.remove_at_n(2)
    print(f"Removed Node (Middle): {removed_middle.data}")
    print_dll(dll_remove_at, "Test 3e: After remove_at_n (Middle)")


if __name__ == "__main__":
    tests()
