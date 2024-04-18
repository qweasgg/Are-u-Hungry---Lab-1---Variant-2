class DynamicArray:

    def __init__(self, initial_capacity=10, growth_factor=2):
        self.capacity = initial_capacity
        self.growth_factor = growth_factor
        self.length = 0
        self.data = [None] * initial_capacity

    def __getitem__(self, index):
        if 0 <= index < self.length:
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if 0 <= index < self.length:
            self.data[index] = value
        else:
            raise IndexError("Index out of range")

    def append(self, value):
        if value is None:
            raise ValueError("Input is None")
        if self.length == self.capacity:
            self._resize()
        self.data[self.length] = value
        self.length += 1

    def _resize(self):
        new_capacity = self.capacity * self.growth_factor
        new_data = [None] * new_capacity
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def remove(self, value):
        index = -1
        for i in range(self.length):
            if self.data[i] == value:
                index = i
                break
        if index < 0:
            raise ValueError("Value not found")
        else:
            for j in range(index, self.length - 1):
                self.data[j] = self.data[j + 1]
            self.length -= 1

    def size(self):
        return self.length

    def is_member(self, value):
        for i in range(self.length):
            if self.data[i] == value:
                return i
        return -1

    def reverse(self):
        left = 0
        right = self.length - 1
        while left < right:
            temp = self.data[left]
            self.data[left] = self.data[right]
            self.data[right] = temp
            left += 1
            right -= 1

    def to_list(self):
        return [self.data[i] for i in range(self.length)]

    def from_list(cls, lst):
        dynamic_array = cls(initial_capacity=len(lst))
        for item in lst:
            dynamic_array.append(item)
        return dynamic_array

    def filter(self, predicate):
        filtered_array = DynamicArray()
        for i in range(self.length):
            if predicate(self.data[i]):
                filtered_array.append(self.data[i])
        return filtered_array

    def map(self, function):
        map_array = DynamicArray()
        for i in range(self.length):
            map_array.append(function(self.data[i]))
        return map_array

    def reduce(self, function):
        reduce_array = DynamicArray()
        value = self.data[0]
        for i in range(self.length-1):
            value = function(value, self.data[i + 1])
        reduce_array.append(value)
        return reduce_array

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < self.length:
            value = self.data[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration

    @classmethod
    def empty(cls):
        return cls()

    def concat(self, other):
        initial_capacity = self.length + other.length
        concatenated_array = DynamicArray(initial_capacity=initial_capacity)
        for item in self:
            concatenated_array.append(item)
        for item in other:
            concatenated_array.append(item)
        return concatenated_array
