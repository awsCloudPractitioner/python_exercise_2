import unittest
from searchfromend import kth_element_from_end


class TestSearchFromEnd(unittest.TestCase):

    def test_kth_element_from_end(self):
        # positive tests
        self.assertEqual(kth_element_from_end([10, 20, 30, 40], 3), 20)
        self.assertEqual(kth_element_from_end([6, 5, 4, 3, 2, 1], 5), 5)
        self.assertEqual(kth_element_from_end(['a', 'b', 'c', 'd', 'e'], 2), 'd')

    def test_error(self):
        with self.assertRaises(Exception): kth_element_from_end([10, 20, 30], 4)
        with self.assertRaises(Exception): kth_element_from_end([], 2)


if __name__ == '__main__':
    unittest.main()
