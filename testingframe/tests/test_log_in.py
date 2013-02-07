"""
    Copyright 2011 Software Freedom Conservancy.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Product name: testFramework
    Copyright (C) mbu 2012
    Author(s): Mathieu BULTEL

    Description : Unit test template for test automation project.
"""

import os
import sys
sys.path.append(os.getcwd())

from pages.login import LoginPage
from common.common import Common

import unittest

class test_log_in(unittest.TestCase):
    """
        Log in testing (test demo)
    """

    def setUp(self):
        """ init test """
        print "load here your test data, yaml base"
        self.testSetup = Common()

    def test_log_in(self):
        """ test log page """
        login_page = LoginPage(self.testSetup)
        login_page.go_to_login_page()

        login_page.log_in()        

    def tearDown(self):
        """ Tear Down of your test """
        pass    

if __name__ == '__main__':
    unittest.main()




