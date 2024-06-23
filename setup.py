from setuptools import find_packages, setup

setup(
    name='applepylog',
    packages=find_packages(include=['applepylog']),
    version='0.1.0',
    description='A simple logger for basic projects',
    author='Chris Yeomans',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest~=8.2.2'],
)