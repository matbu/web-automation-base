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
"""import os
import sys
sys.path.append(os.getcwd())

_index_url = "https://10.10.47.81"
_selenium = "webdriver"
_navigator = "chrome"
_timeout = "0"

class Common(object):
    """ common class for globals variables """

    def __init__(self):
        self.index_url = _index_url
        self.navigator = _navigator
        self.timeout = _timeout



