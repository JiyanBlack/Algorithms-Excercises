class LinkedList():

    def __init__(self):
        self._head = None
        self._tail = None

    def purge(self):
        self._head = None
        self._tail = None

    head = property(
        fget=lambda self: self._head
    )

    tail = property(
        fget=lambda self: self._tail
    )

    isEmpty = property(
        fget=lambda self: self._head is None
    )

    def get_first(self):
        if self._head is None:
            raise ValueError
        return self._head.datum

    def get_last(self):
        if self._tail is None:
            raise ValueError
        return self._tail.datum

    first = property(fget=lambda self: self.get_first())
    last = property(fget=lambda self: self.get_last())

    def prepend(self, item):
        tmp = self.Element(self, item, self._head)
        if self._head is None:
            self._tail = tmp
        self._head = tmp

    def append(self, item):
        tmp = self.Element(self, item, None)
        if self._head is None:
            self._head = tmp
        self._tail = tmp

    def __copy__(self):
        result = LinkedList()
        cur_ele = self.head
        while cur_ele is not None:
            result.append(cur_ele.datum)
            cur_ele = cur_ele.next
        return result

    def extract(self, item):
        pre_target = None
        target = self.head
        while target.datum is not item:
            pre_target = target
            target = target.next
        if target is None:
            raise KeyError
        if target == self.head:
            self.head = self.head.next
        elif target == self.tail:
            self.tail = pre_target
            pre_target._next = None
        else:
            pre_target._next = target.next

    class Element():

        def __init__(self, mylist, datum, mynext):
            self._list = mylist
            self._datum = datum
            self._next = mynext

        datum = property(fget=lambda self: self._datum)

        next = property(fget=lambda self: self._next)

myList = LinkedList()
myList.prepend("Last")
myList.prepend("First")
print(myList.first, myList.last, myList.isEmpty,
      myList.head.datum, myList.tail.datum)
