from dll import DoublyLinkedList, Node


class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self) -> bool:
        return True if self.items else False

    def size(self) -> int:
        return len(self.items)

    def print(self):
        N = self.size()
        for _ in range(N):
            print(self.items.pop())


class LinkStack:
    def __init__(self):
        self.dll = DoublyLinkedList()

    def push(self, item):
        self.dll.add_last(Node(item))

    def pop(self):
        return self.dll.remove_last()

    def is_empty(self) -> bool:
        return True if self.dll.size == 0 else False

    def size(self) -> int:
        return self.dll.size

    def print(self):
        N = self.size()
        for _ in range(N):
            print(self.pop().data)


def test_ArrayStack():
    stack = ArrayStack()

    stack.push(12)
    stack.push(11)
    stack.push(10)
    stack.push(9)

    stack.pop()

    stack.print()


def test_LinkStack():
    stack = LinkStack()

    stack.push(12)
    stack.push(11)
    stack.push(10)
    stack.push(9)

    stack.pop()

    stack.print()


if __name__ == "__main__":
    # test_ArrayStack()
    test_LinkStack()
