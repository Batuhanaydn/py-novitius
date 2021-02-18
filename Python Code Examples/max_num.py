import unittest


def get_char(c):
    return chr(c)
    
    
class TestGetChar(unittest.TestCase):
    def test_get_char_should_return_capital_a_when_given_c_is_65(self):
        self.assertEqual(get_char(65), 'A')

print(get_char(65))
