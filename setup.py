

from setuptools import setup

setup(
    name='pyona',
    version='0.1',
    description='Module for accessing ONA data',
    author='Léo Gorman',
    author_email='leomgorman@outlook.com',
    packages=['pyona'],  # same as name
    install_requires=['pandas', 'requests']
)
