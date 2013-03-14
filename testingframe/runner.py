#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    Product name: pyGui
    Copyright (C) mbu 2013
    Author(s): Mathieu BULTEL

    Description : Generic runner for tests
"""

import os
import sys
import common.common
import unittest
import tests

from utils.data import Data

class Runner(object):
    """ class for manage test requirements and run test"""

    tests = []
    tests_path = "tests/"

    def __init__(self, filename="test_requirements.yml"):
        """ call here the utils module for yaml loading """
        data = Data(filename)
        self.requirements = data.get_all_value()

    # Test part : 
    def get_all_tests(self):
        """ get all tests """
        test = os.listdir(self.tests_path)
        self.tests = ['tests.'+i.replace('.py','') for i in test if "test_" in i and not "pyc" in i and not "py~" in i]
        return self.tests

    def get_test_by_file(self):
        """ get only selected tests """
        pass

    def get_test_by_name(self):
        """ get only selected tests """
        pass

    # Test launch part:
    def _import_test(self):
        """ import test """
        if self.tests != []:
            map(__import__,self.tests)

    def set_suite(self):
        """ Set suite for """
        suite = unittest.TestSuite()
        self._import_test()
        if self.tests != []:
            for mod in [sys.modules[modname] for modname in self.tests]:
                suite.addTest(unittest.TestLoader().loadTestsFromModule(mod))
            unittest.TextTestRunner(verbosity=2).run(suite)
        return False

    # Requirements part:
    def set_globals(self):
        """ Set globals variables """
        self.step_keys = self.requirements.keys()
        for step in self.step_keys:
            for value in self.requirements[step]:
                properties = setattr(common.common, '_'+value, self.requirements[step][value])
            self.set_suite()

if __name__ == '__main__':

    # Create a Runner instance
    runner = Runner()
    if len(sys.argv) > 1:
        print "TODO : manage test file and test name in command line"
    # We work with all tests
    runner.get_all_tests()
    # Launch with globals setting
    runner.set_globals()

