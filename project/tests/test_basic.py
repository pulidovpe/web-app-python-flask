# project/tests/test_basic.py

import os
import unittest
import json
from urllib.parse import urlencode

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
   
   def test_about_page(self):
      response = self.app.get('/about', follow_redirects=True)
      self.assertEqual(response.status_code, 200)

   def test_plus_one(self):
      self.dato = { 'x': 2 }
      response = self.app.get('/plus_one' + '?' + urlencode(self.dato))
      res = json.loads(response.data.decode('utf-8'))
      assert res['x'] == 3
   
   def test_square(self):
      self.dato = { 'x': 2 }
      response = self.app.get('/square' + '?' + urlencode(self.dato))
      res = json.loads(response.data.decode('utf-8'))
      assert res['x'] == 4

if __name__ == "__main__":
   unittest.main()
