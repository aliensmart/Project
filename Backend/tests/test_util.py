from unittest import TestCase
from app import util


class TestUtil(TestCase):

    def testGetPrice(self):
        response = util.get_price("ibm")
        self.assertIsInstance(response, float, "API call returns a float")

    def testHashPass(self):
        testoutput = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
        test = util.hash_password("password")
        self.assertEqual(test, testoutput, "hash_pass returns correct output")
