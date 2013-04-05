from distutils.core import setup

setup(
    name='createpyproject',
    version='0.1.0',
    author='Gennady Denisov',
    author_email='denisovgena@gmail.com',
    packages=['createpyproject', 'createpyproject.test'],
    url='https://www.bitbucket.org/createpyproject',
    license='LICENSE.txt',
    description='My project to create pypy project',
    long_description=open('README.txt').read(),
)