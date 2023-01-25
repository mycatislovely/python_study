
import unittest


d = {'M':1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

def rome_to_decimal(f):
    n = 0
    p = 0
    for c in reversed(f):
        v = d[c] 
        if v >= p:
            n += v
        else:
            n -= v
        p = v
    return n
    
class TestRomeToDecimal(unittest.TestCase):

    def test_7(self):
        self.assertEqual(7, rome_to_decimal('VII'))

    def test_multiple(self):
        for n, r in [(3, 'III'), (15, 'XV'), (1230, 'MCCXXX'), (78, 'LXXVIII'), (1, 'I'), 
                     (412, 'CDXII'), (105, 'CV'), (1700, 'MDCC'), (3911, 'MMMCMXI')]:
            with self.subTest(test_name=r):
                self.assertEqual(n, rome_to_decimal(r))

if __name__ == "__main__":
    unittest.main()    
# print(rome_to_decimal(input()))


      