from pickler import list_pickler, unpickler
import unittest

class PickleTests(unittest.TestCase):
    def setUp(self):
        self.my_list = [1,2,3,4,5]
        self.file_name = "pickle_test.p"
    def test_original_and_unpickled_list_same(self):
        list_pickler(self.my_list,self.file_name)
        unpickled_list = unpickler(self.file_name)
        unpickled_list = [5,4,3,2,1]
        self.assertEqual(self.my_list, unpickled_list)

unittest.main()