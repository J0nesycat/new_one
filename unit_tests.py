import unittest

number=2
word='shecodes'
string=''
num_string=['1','2','3','4','5',None ,'6','7','8','9','10'] 

class TestMath(unittest.TestCase):
    
    def test_plus(self):
    
        self.assertEqual(4,2+2)
        
    def test_word(self):
    
        self.assertEqual(word.count('e'),number)
        
    def test_len(self):
        
        self.assertEqual(len(string),0)
        
    
    def test_null(self):
    
        for i in num_string:
            self.assertIsNotNone(i) 
            
            
            
if __name__ == '__main__':
    unittest.main()
