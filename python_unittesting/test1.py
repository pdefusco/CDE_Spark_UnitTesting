# your code below:
import unittest

def myFunction(val):
    if val < 10:
        output = 'low'
    elif val < 50:
        output = 'medium'
    else:
        output = 'high'
    return output

class MyUnitTest(unittest.TestCase):

  # Write your code below:
  def test_row_1(self):
    self.assertEqual(myFunction(1), 'low', 'The output value is low!')

  def test_row_50(self):
    self.assertEqual(myFunction(50), 'medium', 'The output value is medium!')

  def test_row_60(self):
    self.assertEqual(myFunction(60), 'high', 'The output value is high!')

unittest.main()
