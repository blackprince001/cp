from dll import DoublyLinkedList, Node


class ArrayQueue:
    def __init__(self, cap=100):
        self.capacity = cap
        self.items = [0] * self.capacity
        self.size = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            raise Exception("Queue is full")

        self.items[self.size] = item
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue is empty")

        item = self.items[0]
        for i in range(1, self.size):
            self.items[i - 1] = self.items[i]

        self.size -= 1
        return item

    def is_empty(self) -> bool:
        return self.size == 0

    def capacity(self) -> int:
        return self.capacity


class LinkQueue:
    def __init__(self, cap=100):
        self.dll = DoublyLinkedList()

    def enqueue(self, item):
        self.dll.add_last(Node(item))

    def dequeue(self):
        if self.dll.is_empty():
            raise Exception("Queue is empty")

        return self.dll.remove_first().data

    def is_empty(self) -> bool:
        return self.dll.is_empty()

    def capacity(self) -> int:
        return self.dll.size()


def test_ArrayQueue():
    queue = ArrayQueue(5)

    queue.enqueue(12)
    queue.enqueue(11)
    queue.enqueue(10)
    queue.enqueue(9)

    queue.dequeue()

    while not queue.is_empty():
        print(queue.dequeue())


def test_LinkQueue():
    queue = LinkQueue()

    queue.enqueue(12)
    queue.enqueue(11)
    queue.enqueue(10)
    queue.enqueue(9)

    queue.dequeue()

    while not queue.is_empty():
        print(queue.dequeue())


if __name__ == "__main__":
    test_ArrayQueue()
    print("-----")
    test_LinkQueue()
