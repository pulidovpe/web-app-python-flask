# project/tests/test_basic.py

import os
import unittest

from project import app

#TEST_DB = 'test.db'

class BasicTests(unittest.TestCase):

   ############################
   #### setup and teardown ####
   ############################

   # executed prior to each test
   def setUp(self):
      app.config['TESTING'] = True
      app.config['WTF_CSRF_ENABLED'] = False
      app.config['DEBUG'] = False
      self.app = app.test_client()

   # executed after each test
   def tearDown(self):
      pass

   ###############
   #### tests ####
   ###############

   def test_main_page(self):
      response = self.app.get('/', follow_redirects=True)
      self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
   unittest.main()
