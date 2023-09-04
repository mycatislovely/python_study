import unittest

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

class TestIsAnagram(unittest.TestCase):

    def test_empty_strings(self):
        self.assertTrue(is_anagram('', ''))
        
    def test_positive(self):
        self.assertTrue(is_anagram('кот', 'кто'))
        
    def test_any_case(self):
        self.assertTrue(is_anagram('AbaCa', 'AcaBa'))   
        
    def test_negative(self):
        self.assertFalse(is_anagram('gbaba', 'acada'))  

if __name__ == "__main__":
    unittest.main()



