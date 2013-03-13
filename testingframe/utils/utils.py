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

class Utils(object):
    """ this class give some tools for test framework """

    def get_function_by_pattern(self, obj, pattern):
        """ get all function of an object matching with pattern variable """
        func = []
        funcs = dir(obj)
        func = [i for i in funcs if pattern in i]
        return func



