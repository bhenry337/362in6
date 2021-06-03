import unittest
import leapyear

class TestCase(unittest.TestCase):
	def test_div4(self):
		self.assertEqual(leapyear.leapyear(2004), True)
		pass