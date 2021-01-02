#!/usr/bin/env python3
import os.path
from setuptools import setup

with open('README.rst', 'rb') as file:
    readme = file.read().decode('utf8')
    
setup(
    name='nwe',
    version='1.0.4',
    url='https://github.com/narutolavo/nwe',
    license='MIT License',
    author='Narutolavo',
    author_email='narutoolavo@outlook.com',
    keywords='News Web Easy, Jisho, Anki, Japonês',
    description='Criar Cartões do anki e pdf, do site News Web Easy ',
    long_description=readme,
    packages=['nwe'],
    install_requires=['googletrans==4.0.0rc1', 'beautifulsoup4', 'reportlab', 'requests'],
     entry_points={
        'gui_scripts': [
            'nwe = nwe:__main__',
        ]
    },
    classifiers=['Development Status :: 5 - Production/Stable',
                     'Intended Audience :: Education',
                     'Intended Audience :: End Users/Desktop',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: POSIX',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: MacOS :: MacOS X',
                     'Topic :: Education',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7',
                     'Programming Language :: Python :: 3.8'],
                     )