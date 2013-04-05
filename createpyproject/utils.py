# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Gennady Denisov.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.


import os
from config import CODING_INFO


def get_template(name, path='templates'):
    fl = os.path.join(os.path.dirname(__file__), path, name + '.txt')
    with open(fl, 'r') as f:
        s = f.read()
    return s


def create_package(pth):
    with open(os.path.join(pth, '__init__.py'), 'w') as f:
        f.write(('%s' % CODING_INFO))
