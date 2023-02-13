import unittest
from merge_sort import *

def merge_sort_part_returning(a, left, right):
        merge_sort_part(a, left, right)
        return a

class TestMergeSort(unittest.TestCase):

    def test_merge_empty(self):  
        self.assertEqual([], merge([], 0, 0, 0))   
        self.assertEqual([], merge([1, 5, 7], 0, 0, 0))   
        self.assertEqual([], merge([1, 5, 7], 1, 1, 1))   
        self.assertEqual([], merge([1, 5, 7], 2, 2, 2))   
         
    def test_merge_one(self):  
        self.assertEqual([1], merge([1], 0, 0, 1))    
        self.assertEqual([1], merge([1], 0, 1, 1))    
        self.assertEqual([1], merge([1, 2, 3], 0, 0, 1))    
        self.assertEqual([1], merge([1, 2, 3], 0, 1, 1))    
        self.assertEqual([2], merge([1, 2, 3], 1, 1, 2))    
        self.assertEqual([2], merge([1, 2, 3], 1, 2, 2))    
        self.assertEqual([3], merge([1, 2, 3], 2, 2, 3))    
        self.assertEqual([3], merge([1, 2, 3], 2, 3, 3))    

    def test_merge_several(self):  
        self.assertEqual([1, 2, 10, 20, 100, 200], merge([1, 10, 100, 2, 20, 200], 0, 3, 6)) 
        self.assertEqual([1, 2, 10, 20, 100, 200], merge([2, 20, 200, 1, 10, 100], 0, 3, 6)) 
        self.assertEqual([1, 2, 3, 10, 20, 30], merge([10, 20, 30, 1, 2, 3], 0, 3, 6)) 
        self.assertEqual([1, 2, 10, 20], merge([100, 1, 10, 2, 20, 0], 1, 3, 5)) 
       
      
    def test_merge_sort_part_empty(self):  
        self.assertEqual([], merge_sort_part_returning([], 0, 0)) 
        self.assertEqual([3,2, 1], merge_sort_part_returning([3, 2, 1], 2, 2)) 
        self.assertEqual([3, 2, 1], merge_sort_part_returning([3, 2, 1], 1, 1)) 

    def test_merge_sort_part_one(self):  
        self.assertEqual([3], merge_sort_part_returning([3], 0, 1)) 
        self.assertEqual([3, 2, 1], merge_sort_part_returning([3, 2, 1], 0, 1)) 
        self.assertEqual([3, 2, 1], merge_sort_part_returning([3, 2, 1], 1, 2)) 
        self.assertEqual([3, 2, 1], merge_sort_part_returning([3, 2, 1], 2, 3)) 
        
 
    def test_merge_sort_part_several(self):  
        self.assertEqual([1, 2, 3, 4, 5], merge_sort_part_returning([1, 2, 3, 4, 5], 0, 5))       
        self.assertEqual([1, 2, 3, 4, 5], merge_sort_part_returning([5, 4, 3, 2, 1], 0, 5))       
        self.assertEqual([3, 4, 5, 2, 1], merge_sort_part_returning([5, 4, 3, 2, 1], 0, 3))       
        self.assertEqual([5, 2, 3, 4, 1], merge_sort_part_returning([5, 4, 3, 2, 1], 1, 4))       
        self.assertEqual([5, 4, 1, 2, 3], merge_sort_part_returning([5, 4, 3, 2, 1], 2, 5))       
        

    def test_merge_sort(self):
        a = []
        merge_sort(a)
        self.assertEqual([], a) 
        a = [1]
        merge_sort(a)
        self.assertEqual([1], a) 
        a = [1, 3, 2]
        merge_sort(a)
        self.assertEqual([1, 2, 3], a) 
        
if __name__ == "__main__":
    unittest.main() 


    
   
    
    
    
    
    
    
    
    
    
    
