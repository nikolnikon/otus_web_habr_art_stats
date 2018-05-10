# -*- coding: utf-8 -*-

from os.path import join, dirname
from setuptools import setup, find_packages

setup(
    name='habr_art_stat',
    version='0.0.1',
    description='Приложение для сбора статистики о словах в статьях habr.com',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    author='nikolnikon',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),
    install_requires=[
        'pymorphy2 ~= 0.0',
        'requests ~= 2.0',
        'dateparser ~= 0.0',
        'bs4 ~= 0.0',
    ],
    entry_points={
        'console_scripts': ['habr_art_stat=habr_art_stat:main'],
    },
)