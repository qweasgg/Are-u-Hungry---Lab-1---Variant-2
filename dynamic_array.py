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
