import unittest

def segment_intersection(a1, b1, a2, b2):
    a = max(a1, a2)
    b = min(b1, b2)
    if a > b:
        return None
    elif a < b:
        return a, b
    else:    
        return a


class TestSegmentIntersection(unittest.TestCase):

    def test_do_not_intersect(self):
        self.assertIsNone(segment_intersection(1, 3, 5, 6))
        self.assertIsNone(segment_intersection(-12, -8, -7, -1))
         
    def test_segments_touch(self):
        self.assertEqual(3, segment_intersection(1, 3, 3, 6))
        self.assertEqual(3, segment_intersection(3, 6, 1, 3))
        self.assertEqual(-8, segment_intersection(-12, -8, -8, -1))   
        self.assertEqual(-8, segment_intersection(-8, -3, -12, -8))   

    def test_segments_intersect(self):
        self.assertEqual((3, 5), segment_intersection(1, 5, 3, 6))
        self.assertEqual((3, 5), segment_intersection(3, 6, 1, 5))
        self.assertEqual((-9, -8), segment_intersection(-12, -8, -9, -1))   
        self.assertEqual((-9, -8), segment_intersection(-9, -1, -12, -8))   
      
 
if __name__ == "__main__":
    unittest.main() 
