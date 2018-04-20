import unittest
from hw00 import greet

class TestPrints(unittest.TestCase):

	def testGreeting(self):
		self.assertEqual(greet(), "Hello, World!")

if __name__ == '__main__':
	unittest.main()
