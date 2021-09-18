#!/bin/python3
# -*- coding: utf-8 -*-
#
# Run all test cases for Finnish grammar rules.

import unittest


def run_test_suite():
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='',
                            pattern='*_test.py')

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    run_test_suite()
    
