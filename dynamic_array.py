from typing import Any, List, Callable


class DynamicArray:

    def __init__(self, initial_capacity: int = 10,
                 growth_factor: int = 2) -> None:
        self.capacity = initial_capacity
        self.growth_factor = growth_factor
        self.length = 0
        self.data = [None] * initial_capacity

    def __getitem__(self, index: Any) -> Any:
        if 0 <= index < self.length:
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index: Any, value: Any) -> Any:
        if 0 <= index < self.length:
            self.data[index] = value
        else:
            raise IndexError("Index out of range")

    def append(self, value: Any) -> Any:
        if value is None:
            raise ValueError("Input is None")
        if self.length == self.capacity:
            self._resize()
        self.data[self.length] = value
        self.length += 1

    def _resize(self) -> None:
        new_capacity = self.capacity * self.growth_factor
        new_data = [None] * new_capacity
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def remove(self, value: Any) -> None:
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

    def size(self) -> int:
        return self.length

    def is_member(self, value: Any) -> int:
        for i in range(self.length):
            if self.data[i] == value:
                return i
        return -1

    def reverse(self) -> None:
        left = 0
        right = self.length - 1
        while left < right:
            temp = self.data[left]
            self.data[left] = self.data[right]
            self.data[right] = temp
            left += 1
            right -= 1

    def to_list(self) -> List[Any]:
        return [self.data[i] for i in range(self.length)]

    def from_list(cls, lst: List[Any]) -> 'DynamicArray':
        dynamic_array = DynamicArray(initial_capacity=len(lst))
        for item in lst:
            dynamic_array.append(item)
        return dynamic_array

    def filter(self, predicate: Callable[[Any], bool]) -> None:
        for i in range(self.length):
            if predicate(self.data[i]):
                continue
            else:
                self.remove(self.data[i])

    def map(self, function: Callable[[Any], Any]) -> None:
        for i in range(self.length):
            self.data[i] = function(self.data[i])

    def reduce(self, function: Callable[..., Any]) -> None:
        value = self.data[0]
        for i in range(self.length - 1):
            value = function(value, self.data[i + 1])
        self.data = [value]
        self.length = 1

    def __iter__(self) -> Any:
        self._index = 0
        return self

    def __next__(self) -> Any:
        if self._index < self.length:
            value = self.data[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration

    @classmethod
    def empty(cls) -> 'DynamicArray':
        return cls()

    def concat(self, other: 'DynamicArray') -> None:
        for item in other:
            self.append(item)
