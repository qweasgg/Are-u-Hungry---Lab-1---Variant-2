import unittest
from hypothesis import given, strategies

from dynamic_array import DynamicArray


class TestDynamicArray(unittest.TestCase):

    def test_init(self):
        dyn_array = DynamicArray(initial_capacity=5, growth_factor=2)
        self.assertEqual(dyn_array.capacity, 5)
        self.assertEqual(dyn_array.length, 0)
        self.assertEqual(dyn_array.growth_factor, 2)

    def test_get(self):
        dyn_array = DynamicArray()
        dyn_array.append(1)
        dyn_array.append(2)
        dyn_array.append(3)
        self.assertEqual(dyn_array[1], 2)

    def test_set(self):
        dyn_array = DynamicArray()
        dyn_array.append(1)
        dyn_array.append(2)
        dyn_array.append(3)
        dyn_array[1] = 5
        self.assertEqual(dyn_array[1], 5)

    @given(strategies.integers())
    def test_append_and_resize(self, values):
        dyn_array = DynamicArray(initial_capacity=2, growth_factor=2)
        dyn_array.append(1)
        dyn_array.append(2)
        self.assertEqual(dyn_array.length, 2)
        self.assertEqual(dyn_array.capacity, 2)
        dyn_array.append(values)
        self.assertEqual(dyn_array[2], values)
        self.assertEqual(dyn_array.length, 3)
        self.assertEqual(dyn_array.capacity, 4)

    def test_remove(self):
        dyn_array = DynamicArray()
        dyn_array.append(1)
        dyn_array.append(2)
        dyn_array.append(3)
        dyn_array.remove(1)
        self.assertEqual(dyn_array.length, 2)
        self.assertEqual(dyn_array[0], 1)
        self.assertEqual(dyn_array[1], 3)

    def test_size(self):
        dyn_array = DynamicArray()
        dyn_array.append(1)
        dyn_array.append(2)
        size = dyn_array.size()
        self.assertEqual(size, 2)

    def test_is_member(self):
        dyn_array = DynamicArray()
        dyn_array.append(1)
        dyn_array.append(2)
        dyn_array.append(3)
        index = dyn_array.is_member(2)
        self.assertEqual(index, 1)
        index = dyn_array.is_member(4)
        self.assertEqual(index, -1)

    def test_reverse(self):
        dyn_array = DynamicArray()
        dyn_array.append(1)
        dyn_array.append(2)
        dyn_array.append(3)
        dyn_array.reverse()
        self.assertEqual(dyn_array[0], 3)
        self.assertEqual(dyn_array[2], 1)

    def test_from_L(self):
        dynamic_array = DynamicArray.from_list(DynamicArray, [12, 99, 37])
        self.assertEqual(dynamic_array[0], 12)
        self.assertEqual(dynamic_array[1], 99)
        self.assertEqual(dynamic_array[2], 37)

    def test_build_L(self):
        dyn_array = DynamicArray()
        dyn_array.append(12)
        dyn_array.append(99)
        dyn_array.append(37)
        lst = dyn_array.to_list()
        self.assertEqual(lst, [12, 99, 37])

    def test_filter(self):
        def is_even(num):
            return num % 2 == 0

        def is_odd(num):
            return num % 2 == 1
        dyn_array = DynamicArray()
        dyn_array.append(1)
        dyn_array.append(2)
        dyn_array.append(3)
        filter_array = dyn_array.filter(is_even)
        self.assertEqual(filter_array.length, 1)
        self.assertEqual(filter_array[0], 2)
        filter_array = dyn_array.filter(is_odd)
        self.assertEqual(filter_array.length, 2)
        self.assertEqual(filter_array[0], 1)
        self.assertEqual(filter_array[1], 3)

    def test_map(self):
        def increment(num):
            return num + 1
        dyn_array = DynamicArray()
        dyn_array.append(1)
        dyn_array.append(2)
        dyn_array.append(3)
        map_array = dyn_array.map(increment)
        self.assertEqual(map_array[0], 2)
        self.assertEqual(map_array[1], 3)
        self.assertEqual(map_array[2], 4)

    def test_reduce(self):
        def sum(num1, num2):
            return num1 + num2
        dyn_array = DynamicArray()
        dyn_array.append(1)
        dyn_array.append(2)
        dyn_array.append(3)
        reduce_array = dyn_array.reduce(sum)
        self.assertEqual(reduce_array.length, 1)
        self.assertEqual(reduce_array[0], 6)
