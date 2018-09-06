import unittest

from challenge3 import missingnumbers


class LookTestCase (unittest.TestCase):
 def setUp(self):
    pass                                              
 def test_missing_numbers_works(self):               
  response = missingnumbers.numbers()                      
  self.assertEqual(len(response),2)          
                                             



if '__name__' == '__main__' :
 unittest.main()                                            