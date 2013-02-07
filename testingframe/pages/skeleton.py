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

    Description : skeleton pages module.
"""

import os
import sys
sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By

from common.page import Page

class SkeletonPage(Page):
    """ skeleton of your web pages under test """

    _page_title_locator = (By.ID, 'page-title')
    _value = None
    _locator = None

    @property
    def page_title(self):
        return self.selenium.find_element(*self._page_title_locator).text

    @property
    def header_region(self):
        """ call here specific header check/test function """
        pass

    @property
    def footer_region(self):
        """ call here specific footer check/test function """
        pass

    @property
    def specific_region(self):
        """ call here specific region testing function """
        pass

    @property
    def input_value(self):
        """ call webdriver function for input value in a text form """
        input_field = self.selenium.find_element(*self._locator)
        input_field.clear()
        input_field.send_keys(self._value)

    @property
    def click_element(self):
        """ click on a element """
        self.selenium.find_element(*self._locator).click()



