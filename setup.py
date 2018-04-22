import os
from codecs import open

from setuptools import setup, find_packages

project_path = os.path.abspath(os.path.dirname(__file__))

try:
    # Get the long description from the README file
    with open(os.path.join(project_path, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    # When installing dependencies inside a container,
    # this file probably won't be there
    long_description = ''

requirements = [
    'Django==2.0.4',
]

if bool(int(os.getenv('PRODUCTION', 0))):
    requirements += ['gunicorn']


setup(
    name='Django Secret Key Generator',
    version='1.0.0',
    long_description=long_description,
    classifiers=[],
    packages=find_packages(),
    install_requires=requirements,
    extra_requires={
        'test': ['coverage'],
    },
)
