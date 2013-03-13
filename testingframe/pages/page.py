#! /usr/bin/env python
# -*- coding: UTF-8 -*-
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

    Description : Standard testing function of web pages.
"""

import os
import time
import sys
sys.path.append(os.getcwd())

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import event_firing_webdriver

class Page(object):
    """ Template Testing Web Page, simple checker function """
    _load_time = 0

    def __init__(self, testsetup):
        self.testsetup = testsetup
        self.base_url = testsetup.index_url
        self.selenium = testsetup.selenium
        self.timeout = testsetup.timeout

    def is_the_current_page(self):
        if self._page_title:
            WebDriverWait(self.selenium, self.timeout).until(lambda s: s.title)
        return True

    def is_element_visible(self, locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except:
            return False

    def is_element_clickable(self, locator):
        try:
            return expected_conditions.element_to_be_clickable(*locator)
        except:
            return False


    def is_element_present(self, *locator):
        self.selenium.implicitly_wait(0)
        try:
            self.selenium.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            self.selenium.implicitly_wait(self.testsetup.default_implicit_wait)

    def wait_search_result_visible(self, *locator):
        try:
            WebDriverWait(self.selenium, self.timeout).until(expected_conditions.presence_of_element_located(*locator))
            return time.time()-self._load_time
        except:
            print "Timeout : ", time.time()-self._load_time
            return False

