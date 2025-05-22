import unittest

from myPythonCollection.queue import MyQueueClass


class TestQueue(unittest.TestCase):
    def test_is_empty(self):
        queue = MyQueueClass()
        queue.is_empty = True
        self.assertTrue(queue.is_empty)

    def test_to_add_element_to_the_queue(self):
        queue = MyQueueClass()
        queue.add_element_to_queue(25)
        queue.add_element_to_queue(7)
        self.assertEqual(len(queue.queue), 2)

    def test_to_remove_element_from_the_queue(self):
        queue = MyQueueClass()
        queue.add_element_to_queue(6)
        queue.remove_an_element()
        self.assertEqual(len(queue.queue), 0)

    def test_to_get_front_element(self):
        queue = MyQueueClass()
        queue.add_element_to_queue(2)
        queue.add_element_to_queue(7)
        queue.get_front_element()
        self.assertEqual(queue.queue[0], 2)

    def test_to_get_back_element(self):
        queue = MyQueueClass()
        queue.add_element_to_queue(12)
        queue.add_element_to_queue(7)
        queue.get_front_element()
        self.assertEqual(queue.queue[1], 7)

    def test_to_check_the_length_of_the_queue(self):
        queue = MyQueueClass()
        queue.add_element_to_queue(6)
        queue.add_element_to_queue(17)
        self.assertEqual(len(queue.queue), 2)




if __name__ == '__main__':
    unittest.main()
