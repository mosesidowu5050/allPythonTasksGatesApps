import unittest

from myPythonCollection.array import ArrayClass


class TestArray(unittest.TestCase):
    def test_to_check_array_exist(self):
        array = ArrayClass()
        self.assertEqual(array.array, [0, 0, 0, 0])

    def test_to_check_array_append(self):
        array = ArrayClass()
        array.append(1)
        array.append(12)
        array.append(23)
        self.assertEqual(array.array, [1, 12, 23, 0])

    def test_to_get_element_in_an_array(self):
        array = ArrayClass()
        array.append(22)
        array.append(7)
        array.get(0)
        self.assertEqual(array.array, [22, 7, 0, 0])

    def test_length(self):
        array = ArrayClass()
        array.append(22)
        array.append(7)
        array.append(12)
        array.append(23)
        array.append(6)
        array.append(11)
        array.append(2)
        self.assertEqual(array.actual_elements, 7)

    def test_that_resize_elements(self):
        array = ArrayClass()
        array.append(22)
        array.append(7)
        array.append(12)
        array.resize()
        self.assertEqual(array.capacity, 8)

    def test_to_remove_elements(self):
        array = ArrayClass()
        array.append(22)
        array.append(7)
        array.remove(0)
        self.assertEqual(array.actual_elements, 1)




if __name__ == '__main__':
    unittest.main()
