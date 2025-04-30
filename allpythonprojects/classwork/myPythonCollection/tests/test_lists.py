import unittest

from myPythonCollection.lists import Lists


class TestLists(unittest.TestCase):
    def test_to_check_lists_exist(self):
        lists = Lists()
        self.assertEqual(lists.item, [])

    def test_to_append_elements_in_a_list(self):
        lists = Lists()
        lists.append_element(23)
        lists.append_element(5)
        self.assertEqual(lists.item, [23, 5])

    def test_to_get_element_in_a_list(self):
        lists = Lists()
        lists.append_element(2)
        lists.append_element(35)
        lists.get(1)
        self.assertEqual(lists.item[1], 35)

    def test_to_set_element_in_a_list(self):
        lists = Lists()
        lists.append_element(23)
        lists.append_element(12)
        lists.set_element(1, 45)
        self.assertEqual(lists.item[1],  45)

    def test_to_check_length_of_a_list(self):
        lists = Lists()
        lists.append_element(32)
        lists.append_element(51)
        lists.append_element(3)
        self.assertEqual(lists.size, 3)

    def test_to_check_clear(self):
        lists = Lists()
        lists.append_element(23)
        lists.append_element(5)
        lists.clear()
        self.assertEqual(lists.item, [])

    # def test_to_reverse_elements(self):
    #     lists = Lists()
    #     lists.append_element(23)
    #     lists.append_element(5)
    #     lists.reverse()
    #     self.assertEqual(lists.item, [23, 5])



if __name__ == '__main__':
    unittest.main()
