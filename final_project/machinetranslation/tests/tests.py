import unittest
from translator import english_to_french, french_to_english

class TestFrenchToEnglishTranslation(unittest.TestCase):
    # test function to test equality of two value
    def test_yes(self):
        testString = 'Oui'
        message = 'Result should not be empty'
        self.assertNotEqual(french_to_english(testString), '', message)
    
    def test_bonjour(self):
        testString = 'Bonjour'
        message = 'Bounjour string test failed.'
        self.assertEqual(french_to_english(testString), 'Hello', message)

class TestEnglishToFrenchTranslation(unittest.TestCase):
    # test function to test equality of two value
    def test_yes(self):
        testString = 'Yes'
        message = 'Result should not be empty'
        self.assertNotEqual(english_to_french(testString), '', message)
    
    def test_hello(self):
        testString = 'Hello'
        message = 'Hello string test failed.'
        self.assertEqual(english_to_french(testString), 'Bonjour', message)
  
if __name__ == '__main__':
    unittest.main()