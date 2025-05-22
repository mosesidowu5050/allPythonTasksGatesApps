import unittest

from myPythonCollections.stack import Stack


class TestStack(unittest.TestCase):
    def test_that_push_into_the_stack(self):
        stacks = Stack()
        self.assertEqual(len(stacks.stack), 0)  # add assertion here
        stacks.push(10)
        self.assertEqual(len(stacks.stack), 1)
        stacks.push(20)
        self.assertEqual(len(stacks.stack), 2)

    def test_that_peek_element(self):
        stacks = Stack()
        stacks.push(10)
        stacks.peek()
        self.assertEqual(len(stacks.stack), 1)

    def test_that_pop_element(self):
        stacks = Stack()
        stacks.push(10)
        stacks.push(20)
        stacks.pop()
        self.assertEqual(len(stacks.stack), 1)

    def test_that_clear_all_element(self):
        stacks = Stack()
        stacks.push(20)
        stacks.push(45)
        stacks.clear()
        self.assertEqual(len(stacks.stack), 0)

    def test_that_remove_an_element(self):
        stacks = Stack()
        stacks.push(34)
        stacks.push(45)
        stacks.push(87)
        stacks.remove(34)
        self.assertEqual(len(stacks.stack), 2)


    def test_that_check_if_its_empty(self):
        stacks = Stack()
        stacks.push(56)
        stacks.push(78)
        stacks.is_empty = True
        self.assertTrue(stacks.is_empty)

    def test_to_set_elements_in_stack(self):
        stacks = Stack()
        stacks.push(67)
        stacks.push(84)
        stacks.set_element(0, 54)
        self.assertEqual(stacks.stack, [54, 84])

    def test_that_check_index(self):
        stacks = Stack()
        stacks.push(97)
        stacks.push(45)
        stacks.push(84)
        stacks.check_index(0)
        self.assertEqual(stacks.stack, [97, 45, 84])

    def test_to_check_length(self):
        stacks = Stack()
        stacks.push(97)
        stacks.push(45)
        stacks.length()
        self.assertEqual(len(stacks.stack), 2)


if __name__ == '__main__':
    unittest.main()
