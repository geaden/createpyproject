# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Gennady Denisov.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

import datetime
import os


class Author(object):
    """
    Project author
    """
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Project(object):
    """
    Project class

    Generates information for setup file

    It has several methods, such as:
    * get_setup

    >>> author = Author(name='foo', email='foo@baz.bar')
    >>> project = Project(author=author, name='test')
    >>> project.get_setup() # doctest: +NORMALIZE_WHITESPACE
    {'author': 'foo',
     'description': None,
     'email': 'foo@baz.bar',
     'name': 'test',
     'packages': "['test', 'test.test']",
     'url': 'https://www.bitbucket.org/test'}
    """
    authors = None
    version = None
    description = None
    year = datetime.date.today().year
    date = datetime.date.today().strftime('%m/%d/%Y')

    def __init__(self, author, name=None, path=os.path.dirname(__file__)):
        self.author = author
        self.name = name
        self.path = os.path.join(path, name)
        self.url = 'https://www.bitbucket.org/%s' % self.name

    def get_readme(self):
        return {
            'name': self.name,
            'dec': '=' * len(self.name)
        }

    def get_license(self):
        return {
            'year': self.year,
            'holder': ', '.join(self.authors)
        }

    def get_setup(self):
        return {
            'name': self.name,
            'author': self.author.name,
            'email': self.author.email,
            'description': self.description,
            'packages': str(self.packages),
            'url': self.url
        }

    def get_changes(self):
        return {
            'version': self.version,
            'date': self.date
        }

    @property
    def packages(self):
        return [self.name, self.name + '.test']
