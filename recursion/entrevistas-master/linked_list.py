class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self, values):
        self.root = None
        if not values:
            return
        prev = None
        for value in values:
            node = LinkedListNode(value)
            if prev:
                prev.next = node
            if self.root is None:
                self.root = node
            prev = node


if __name__ == "__main__":
    linked_list = LinkedList(range(10))
    node = linked_list.root
    while node:
        print(node.value)
        node = node.next
