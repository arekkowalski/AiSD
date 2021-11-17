from typing import Any

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value: Any) -> None:
        node = Node(value)
        node.next = self.head
        self.head = node
        self.tail = node

    def __str__(self) -> str:
        if self.head is None:
            print("Lista jest pusta")
            return
        node = self.head
        llstr = ''
        while node.next:
            llstr += str(node.value) + ' -> '
            node = node.next
        llstr += str(node.value)
        return llstr

    def append(self, value: Any) -> None:
        node = Node(value)
        if(self.head == None):
            self.head = node
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        self.tail = node.next

    def __len__(self) -> int:
        count = 0
        node = self.head
        while node:
            count+=1
            node = node.next
        return count

    def node(self, at: int) -> Any:
        node = self.head
        for x in range(at):
            node = node.next
        return node

    def insert(self, value: Any, after: Node) -> None:
        node = Node(value)
        node.next = after.next
        after.next = node
        if after == self.tail:
            self.append(value)
            return

    def pop(self) -> Any:
        first = self.head
        self.head = self.head.next
        return first.value

    def remove_last(self) -> Any:
        node = self.head
        temp = self.tail
        if self.head == None:
            return None
        if node.next == None:
            node = None
            return None
        sec_last = self.head
        while(sec_last.next.next):
            sec_last = sec_last.next
        sec_last.next = None
        self.tail = sec_last
        return temp.value

    def remove(self, after: Node) -> Any:
        after.next = after.next.next

list_ = LinkedList()

assert list_.head == None

list_.push(1)
list_.push(0)
assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)
returned_first_element = list_.pop()
assert first_element.value == returned_first_element


last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

assert last_element.value == returned_last_element

assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'


class Stack:
    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        llstr = ''

    def push(self, element: Any) -> None:
        self._storage.push(element)

    def pop(self) -> Any:
        if len(self._storage) != 0:
            return self._storage.pop()

stack = Stack()

assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)

assert len(stack) == 3

top_value = stack.pop()

assert top_value == 1

assert len(stack) == 2


class Queue:
    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return len(self._storage)

    def __str__(self) -> str:
        temp = self._storage.head
        llstr: str = ""
        while temp.next != None:
            llstr += str(temp.value) + ", "
            temp = temp.next
        llstr += str(temp.value)
        return llstr

    def peek(self) -> Any:
        if len(self._storage) != 0:
            return self._storage.node(0)

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()

queue = Queue()

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2