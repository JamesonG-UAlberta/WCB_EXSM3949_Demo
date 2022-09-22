import unittest
import myfunction

class TEST_myfunction(unittest.TestCase):
    def test_two_times(self):
        result = myfunction.two_times(2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
#assertNotEqual
#assertTrue
#assertFalse

