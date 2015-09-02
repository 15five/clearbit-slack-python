import os
from setuptools import setup

import clearbit_slack


with open("README.rst") as fd:
    README = fd.read()


with open("LICENSE") as fd:
    LICENSE = fd.read()


setup(
    name='clearbit-slack-python',
    version=clearbit_slack.__version__,
    description='Push Clearbit Person and Company data into a Slack channel',
    license=LICENSE,
    long_description=README,
    author=clearbit_slack.__author__,
    author_email=clearbit_slack.__email__,
    url='https://github.com/15five/clearbit-slack-python',
    packages=['clearbit_slack'],
    test_suite='tests',
    keywords=['Clearbit', 'Slack', 'customer', 'data'],
    install_requires=[
        'slacker>=0.7.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Communications :: Chat',
    ],
)

