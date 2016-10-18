class Array:

    def __init__(self, length=0, baseIndex=0):
        # O(n)
        self._data = [None for i in range(length)]
        self._baseIndex = baseIndex

# shallow copy: creates the copy of the Array
# new array is different but the elements indicate to the same memory address
    def __copy__(self):
        # O(n)
        result = Array(len(self._data), self._baseIndex)
        for i in range(len(self._data)):
            result[i] = self._data[i]
        return result

    def getOffset(self, index):
        # O(1)
        offset = index - self._baseIndex
        if offset < 0 or offset >= len(self._data):
            raise IndexError
        return offset

    def __getitem__(self, index):
        # O(1)
        return self._data[self.getOffset(index)]

    def __setitem__(self, index, value):
        # O(1)
        self._data[self.getOffset(index)] = value

    def getData(self):
        return self._data

    data = property(fget=lambda self: self.getData())

    def getBaseIndex(self):
        return self._baseIndex

    def setBaseIndex(self, baseIndex):
        self._baseIndex = baseIndex

    baseIndex = property(fget=lambda self: self.getBaseIndex(),
                         fset=lambda self, value: self.setBaseIndex(value))

    def setLength(self, value):
        # O(value)
        if len(self._data) != value:
            newData = [None for i in range(value)]
            for i in range(min(value, len(self._data))):
                newData[i] = self._data[i]
            self._data = newData

    length = property(
        fget=lambda self: len(self._data),
        fset=lambda self, value: self.setLength(value))
