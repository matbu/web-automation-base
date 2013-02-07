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

    Description : Specific test module for Login page.
"""

import os
import sys
sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By

from pages.skeleton import SkeletonPage



class LoginPage(SkeletonPage):
    """ here specific code for your pages (login for example) """

    _page_title = 'Wallix'
    _login_url = 'accounts/login/'

    _login_id = (By.ID, 'user_name')
    _pwd_id = (By.ID, 'passwd')
    _submit_bouton = (By.ID, 'SubmitLogin')

    def go_to_login_page(self):
        self.selenium.get(self.testsetup.index_url + '/' + self._login_url)
        self.is_the_current_page

    def log_in(self, username='admin'):
        # get here test data ... 
        # ie : credentials = self.testsetup.credentials[user]
        self.input_text(username, self._login_id)
        # find the best way to do that. in skeleton or not that's the question
        self._value = username
        self._locator = self._pwd_id
        self.input_value

        self.click_element()        

    def input_text(self, value, locator):
        """ call webdriver function for input value in a text form """
        input_field = self.selenium.find_element(*locator)
        input_field.clear()
        input_field.send_keys(value)

    def click_element(self):
        """ click on a element """
        self.selenium.find_element(*self._submit_bouton).click()

