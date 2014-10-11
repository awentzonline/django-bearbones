#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


name = 'django-bearbones'
package = 'bearbones'
description = 'A bare-bones static-y CMS.'
url = 'https://github.com/awentzonline/django-bearbones'
author = 'Adam Wentz'
author_email = 'floppya@gmail.com'
license = 'MIT'
requires = [
    'Django==1.6',
    'django-polymorphic',
    'south',
]


def get_version(package):
    '''
    Return package version as listed in `__version__` in `init.py`.
    '''
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("""^__version__ = ['\']([^'\']+)['\']""", init_py, re.MULTILINE).group(1)


def get_packages(package):
    '''
    Return root package and all sub-packages.
    '''
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    '''
    Return all files under the root package, that are not in a
    package themselves.
    '''
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    args = {'version': get_version(package)}
    print 'You probably want to also tag the version now:'
    print '  git tag -a %(version)s -m \'version %(version)s\'' % args
    print '  git push --tags'
    sys.exit()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['bearbones']
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name=name,
    version=get_version(package),
    url=url,
    license=license,
    description=description,
    author=author,
    author_email=author_email,
    packages=get_packages('bearbones'),
    package_data=get_package_data(package),
    install_requires=requires,
    tests_require=['pytest-django'],
    cmdclass={'test': PyTest}
)
