import unittest

from main import hello

class MainTest(unittest.Testcase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello World!")
        
        
if __name__ == "__main__":
    unittest.main()