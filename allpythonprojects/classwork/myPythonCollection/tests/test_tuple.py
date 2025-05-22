import unittest

from myPythonCollection.tuple import Tuple


class TestTuple(unittest.TestCase):
    def test_to_set_tuple_behaviour(self):
        tuples = Tuple(10, 20, 30)
        self.tuples = Tuple(tuples)

    def test_to_get_element(self):
        tuples = Tuple(10, 20, 30)
        self.assertEqual(tuples.item[0], 10)
        self.assertEqual(tuples.item[1], 20)
        self.assertEqual(tuples.item[2], 30)

    def test_to_check_length(self):
        tuples = Tuple(51, 12, 30, 87, 34, 45)
        self.assertEqual(len(tuples.item), 6)

    def test_add_elements_to_tuple(self):
        tuples = Tuple(4, 21, 3)
        new_tuples = tuples.add(40)
        self.assertEqual(new_tuples.to_tuple(), (4, 21, 3, 40))

    def test_remove_from_tuple(self):
        tuples = Tuple(4, 21, 3, 40)
        new_tuples = tuples.remove(40)
        self.assertEqual(new_tuples.to_tuple(), (4, 21, 3))

    def test_to_the_tuple(self):
        tuples = Tuple(53, 2, 13, 4)
        self.assertEqual(tuples.to_tuple(), (53, 2, 13, 4))




if __name__ == '__main__':
    unittest.main()
