"""BRMFlask is a unified website generator."""
from setuptools import setup
from brmflask.settings import BaseConfig

setup(
    name='BRMFlask',
    version=BaseConfig.VERSION,
    url='http://github.com/brmullikin/brmflask',
    license='MIT',
    author='B. R. Mullikin',
    author_email='ben@brmullikin.com',
    description='Private Flask App',
    long_description=__doc__,
    packages=['brmflask'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-Compress',
        'flask_caching',
        'coloredlogs',
        'htmlmin',
        'Markdown',
        'smartypants',
        'pygments'
    ],
    tests_require=[
        'pytest',
        'pytest-flask',
        'pytest-cov',
        'pep8',
        'flake8-pep257',
        'flask-debugtoolbar'
    ]
)
