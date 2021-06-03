import unittest
import leapyear

class TestCase(unittest.TestCase):
	def test_div4(self):
		self.assertEqual(leapyear.leapyear(2004), True)
		pass
	def test_div100(self):
		self.assertEqual(leapyear.leapyear(2100), False)
		pass
	def test_div400(self):
		self.assertEqual(leapyear.leapyear(2000), True)
		pass