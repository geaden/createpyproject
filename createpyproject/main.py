# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Gennady Denisov.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

import os
from createpyproject.config import DESCRIPTION
from createpyproject.models import Author, Project
from createpyproject.utils import create_package, get_template


def create_project(path,
                   name='pyproject',
                   athname='Gennady Denisov',
                   athemail='denisovgena@gmail.com',
                   description=DESCRIPTION,
                   bin=False):
    author = Author(athname, athemail)
    project = Project(author=author, name=name, path=path)
    project.authors = []
    project.authors.append(project.author.name)
    project.description = description
    os.mkdir(project.path)
    if bin:
        os.mkdir(os.path.join(project.path, 'bin'))
    os.mkdir(os.path.join(project.path, 'docs'))
    # Create main module
    mm = os.path.join(project.path, project.name)
    os.mkdir(mm)
    create_package(mm)
    # Create tests
    t = os.path.join(mm, 'test')
    os.mkdir(t)
    create_package(t)
    return project


def create_setup(project):
    setup = get_template('setup')
    info = project.get_setup()
    with open(os.path.join(project.path, 'setup.py'), 'w') as f:
        f.write(setup % info)


def create_txt(project):
    # README
    readme = get_template('readme')
    info = project.get_readme()
    with open(os.path.join(project.path, 'README.txt'), 'w') as f:
        f.write(readme % info)

    # LICENSE
    lic = get_template('license')
    info = project.get_license()
    with open(os.path.join(project.path, 'LICENSE.txt'), 'w') as f:
        f.write(lic % info)

    # CHANGES
    ch = get_template('changes')
    info = project.get_changes()
    with open(os.path.join(project.path, 'CHANGES.txt'), 'w') as f:
        f.write(ch % info)

    # MANIFEST.in
    m = get_template('manifest')
    with open(os.path.join(project.path, 'MANIFEST.in'), 'w') as f:
        f.write(m)


def create_stuff(project):
    create_setup(project)
    create_txt(project)


def main():
    name = raw_input('Enter project name: ')
    dest = raw_input('Enter destination path: ')
    bin = raw_input('Use bin (y/n): ')
    if bin == 'y':
        bin = True
    else:
        bin = False
    dest = os.path.abspath(dest)
    project = create_project(path=dest, name=name, bin=bin)
    create_stuff(project)


if __name__ == '__main__':
    main()
