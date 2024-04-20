import unittest
from hypothesis import given, strategies

from dynamic_array import DynamicArray


class TestDynamicArray(unittest.TestCase):

    def test_init(self):
        dyn_array = DynamicArray(initial_capacity=5, growth_factor=2)
        self.assertEqual(dyn_array.capacity, 5)
        self.assertEqual(dyn_array.length, 0)
        self.assertEqual(dyn_array.growth_factor, 2)

    @given(strategies.integers(), strategies.integers())
    def test_get(self, value1, value2):
        dyn_array = DynamicArray()
        dyn_array.append(value1)
        dyn_array.append(value2)
        self.assertEqual(dyn_array[0], value1)
        self.assertEqual(dyn_array[1], value2)

    @given(strategies.integers(), strategies.integers())
    def test_set(self, value1, value2):
        dyn_array = DynamicArray()
        dyn_array.append(value1)
        dyn_array[0] = value2
        self.assertEqual(dyn_array[0], value2)

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

    @given(strategies.integers(), strategies.integers())
    def test_remove(self, value1, value2):
        dyn_array = DynamicArray()
        dyn_array.append(value1)
        dyn_array.append(value2)
        dyn_array.remove(value1)
        self.assertEqual(dyn_array.length, 1)
        self.assertEqual(dyn_array[0], value2)

    @given(strategies.integers(), strategies.integers())
    def test_size(self, value1, value2):
        dyn_array = DynamicArray()
        dyn_array.append(value1)
        dyn_array.append(value2)
        size = dyn_array.size()
        self.assertEqual(size, 2)

    @given(strategies.integers(), strategies.integers())
    def test_is_member(self, value1, value2):
        dyn_array = DynamicArray()
        dyn_array.append(value1)
        dyn_array.append(value2)
        index = dyn_array.is_member(value1)
        self.assertEqual(index, 0)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_reverse(self, value1, value2, value3):
        dyn_array = DynamicArray()
        dyn_array.append(value1)
        dyn_array.append(value2)
        dyn_array.append(value3)
        dyn_array.reverse()
        self.assertEqual(dyn_array[0], value3)
        self.assertEqual(dyn_array[2], value1)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_from_L(self, value1, value2, value3):
        my_list = [value1, value2, value3]
        dynamic_array = DynamicArray.from_list(DynamicArray, my_list)
        self.assertEqual(dynamic_array[0], value1)
        self.assertEqual(dynamic_array[1], value2)
        self.assertEqual(dynamic_array[2], value3)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_build_L(self, value1, value2, value3):
        dyn_array = DynamicArray()
        dyn_array.append(value1)
        dyn_array.append(value2)
        dyn_array.append(value3)
        lst = dyn_array.to_list()
        self.assertEqual(lst, [value1, value2, value3])

    def test_filter(self):
        def is_even(num):
            return num % 2 == 0

        dyn_array = DynamicArray()
        dyn_array.append(1)
        dyn_array.append(2)
        dyn_array.append(3)
        dyn_array.append(4)
        dyn_array.filter(is_even)
        self.assertEqual(dyn_array.length, 2)
        self.assertEqual(dyn_array[0], 2)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_map(self, value1, value2, value3):
        def increment(num):
            return num + 1

        dyn_array = DynamicArray()
        dyn_array.append(value1)
        dyn_array.append(value2)
        dyn_array.append(value3)
        dyn_array.map(increment)
        self.assertEqual(dyn_array[0], value1 + 1)
        self.assertEqual(dyn_array[1], value2 + 1)
        self.assertEqual(dyn_array[2], value3 + 1)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_reduce(self, value1, value2, value3):
        def sum(num1, num2):
            return num1 + num2

        dyn_array = DynamicArray()
        dyn_array.append(value1)
        dyn_array.append(value2)
        dyn_array.append(value3)
        dyn_array.reduce(sum)
        self.assertEqual(dyn_array.length, 1)
        self.assertEqual(dyn_array[0], value1 + value2 + value3)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_iterator(self, value1, value2, value3):
        dyn_array = DynamicArray()
        dyn_array.append(value1)
        dyn_array.append(value2)
        dyn_array.append(value3)
        iterator = dyn_array.__iter__()
        self.assertEqual(iterator.__next__(), value1)
        self.assertEqual(iterator.__next__(), value2)
        self.assertEqual(iterator.__next__(), value3)

    @given(strategies.integers(), strategies.integers())
    def test_empty(self, value1, value2):
        e = DynamicArray.empty()
        a = DynamicArray.from_list(DynamicArray, [value1, value2])
        a.concat(e)
        lst1 = a.to_list()
        a = DynamicArray.from_list(DynamicArray, [value1, value2])
        e.concat(a)
        lst2 = e.to_list()
        self.assertEqual(a.to_list(), lst1)
        self.assertEqual(a.to_list(), lst2)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_concat(self, value1, value2, value3):
        array_a = DynamicArray.from_list(DynamicArray, [value1])
        array_b = DynamicArray.from_list(DynamicArray, [value2])
        array_c = DynamicArray.from_list(DynamicArray, [value3])
        array_a.concat(array_b)
        array_a.concat(array_c)
        lst1 = array_a.to_list()
        array_a = DynamicArray.from_list(DynamicArray, [value1])
        array_b = DynamicArray.from_list(DynamicArray, [value2])
        array_c = DynamicArray.from_list(DynamicArray, [value3])
        array_b.concat(array_c)
        array_a.concat(array_b)
        lst2 = array_a.to_list()
        self.assertEqual(lst1, lst2)
