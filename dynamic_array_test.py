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
