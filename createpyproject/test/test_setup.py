# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Gennady Denisov.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

import unittest
import doctest
from createpyproject.models import Project


if __name__ == '__main__':
    # suite is a unittest.TestSuite()
    tests = unittest.TestSuite()
    tests.addTests(doctest.DocTestSuite(Project))
    runner = unittest.TextTestRunner()
    runner.run(tests)