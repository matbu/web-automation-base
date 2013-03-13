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

import string
import random

class RandomString(object):

    def __init__(self, encoding='utf-8'):
        self.aDict = ['']
        # generate alphabet dict
        for letters in string.printable:
            self.aDict += letters

    def _get_random_number(self):
        return random.randint(0,100)

    def _get_size_number(self, min=1, max=10):
        return random.randint(1,10)

    def get_fake_word(self):
        word = ''
        for i in range(self._get_size_number()):
            w = self._get_random_number()
            try:
                word += self.aDict[w]
            except IndexError:
                print "execption with: ",w
                return None
        return word

