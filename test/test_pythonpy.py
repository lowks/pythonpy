import unittest
from subprocess import check_output

class TestPythonPy(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(check_output(['pythonpy']),'')
        
    def test_numbers(self):
        self.assertEqual(check_output(['pythonpy', '3 * 4.5']),'13.5\n')


if __name__ == '__main__':
    unittest.main()
