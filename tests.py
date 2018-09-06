import unittest

from missingnumbers  import numbers


class LookTestCase (unittest.TestCase):
 def setUp(self):
    pass                                              
 def test_missing_numbers_works(self):
  response = numbers()                      
  self.assertEqual(len(response),9)          
                                             



if '__name__' == '__main__' :
 unittest.main()