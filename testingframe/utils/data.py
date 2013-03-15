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

    Product name: testingFramework
    Copyright (C) mbu 2012
    Author(s): Mathieu BULTEL

    Description : class for testing datas management.
"""

import os
import sys
sys.path.append(os.getcwd())

import yaml

class Data(object):
    """ Class fo testing datas management """

    def __init__(self, filename):
        """ here load file with name """ 
        try:
            f = open(filename, 'r')
            self.data = f.read()
            f.close()
        except IOError:
            print "error, the file ",file," does not exist"
        return None

    def get_all_value(self):
        """ return all data """
        return self._load_yaml()

    def get_value(self, key):
        """ return one specific value """
        return self._load_yaml_by_key(key)

    def _load_yaml(self):
        """ load yaml to python """
        data_yaml = yaml.load(self.data)
        return data_yaml

    def _load_yaml_by_key(self, key):
        """ load yaml by key : return line key """
        lines = self.data.splitlines()
        for line in lines:
            if key in line and '#' not in line:
                line_key = line
                break            
        key_ml = yaml.load(line_key)
        return key_ml    

