import unittest
import transpond_matrix as lib


class TestTranspondMatrix(unittest.TestCase):

    def test_empty_matrix(self):
        self.assertEqual([], lib.transpond_matrix([]))
        
        
    def test_one_element(self):
        self.assertEqual([[25]], lib.transpond_matrix([[25]]))  
        
    def test_vertical_matrix(self):
        self.assertEqual([[1, 3, 5], [2, 4, 6]], lib.transpond_matrix([[1, 2], [3, 4], [5, 6]]))

    def test_word_matrix(self):
        self.assertEqual([['a', 'b', 'c'], ['d', 'x', 'z']], 
        lib.transpond_matrix([['a', 'd'], ['b', 'x'], ['c', 'z']])) 

    def test_one_line_matrix(self):
        self.assertEqual([[1], [2], [3]], lib.transpond_matrix([[1, 2, 3]]))   

    def test_one_column_matrix(self):
        self.assertEqual([[1, 2, 3]], lib.transpond_matrix([[1], [2], [3]]))    

    def test_square_matrix(self):
        self.assertEqual([[1, 3], [2, 4]], lib.transpond_matrix([[1, 2], [3, 4]]))         

        
                     
if __name__ == "__main__":
    unittest.main()
    