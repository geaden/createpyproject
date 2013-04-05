# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Gennady Denisov.
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

import os
import argparse
from config import DESCRIPTION
from models import Author, Project
from utils import create_package, get_template


def create_project(path,
                   version,
                   name='pyproject',
                   athname='Gennady Denisov',
                   athemail='denisovgena@gmail.com',
                   description=DESCRIPTION,
                   bin=False,
                   create=False):
    author = Author(athname, athemail)
    project = Project(
        author=author, name=name,
        path=path, create=create)
    project.authors = []
    project.authors.append(project.author.name)
    project.description = description
    if version:
        project.version = version
    if create:
        path = project.path
    if bin:
        os.mkdir(os.path.join(path, 'bin'))
    os.mkdir(os.path.join(path, 'docs'))
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
    parser = argparse.ArgumentParser(description='Creates project structure.')
    parser.add_argument('name', help='project name')
    parser.add_argument('destination', type=str, help='path to project')
    parser.add_argument('-b', '--bin', help='use or not bin folder',
                        action="store_true")
    parser.add_argument('-c', '--create', help='create project root folder',
                        action="store_true")
    parser.add_argument('-v', '--version', metavar='V', type=str, help='project version')
    args = parser.parse_args()
    name = args.name
    dest = args.destination
    version = args.version
    bin = args.bin
    if bin:
        bin = True
    else:
        bin = False
    create = False
    if args.create:
        create = True
    dest = os.path.abspath(dest)
    project = create_project(
        path=dest, name=name,
        bin=bin, create=create,
        version=version)
    create_stuff(project)


if __name__ == '__main__':
    main()
