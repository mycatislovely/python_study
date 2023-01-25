import unittest
import rome_number as lib


class TestRomeNumber(unittest.TestCase):

    def test_7(self):
        self.assertEqual('VII', lib.rome_number(7))

    def test_multiple(self):
        for n, r in [(3, 'III'), (15, 'XV'), (1230, 'MCCXXX'), (78, 'LXXVIII'), (1, 'I'), 
                     (412, 'CDXII'), (105, 'CV'), (1700, 'MDCC'), (3911, 'MMMCMXI')]:
            with self.subTest(test_name=n):
                self.assertEqual(r, lib.rome_number(n))
            
           
if __name__ == "__main__":
    unittest.main()
    