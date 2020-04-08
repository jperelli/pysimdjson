#!/usr/bin/env python
import os
import os.path

from setuptools import setup, find_packages, Extension


root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), 'rb') as readme:
    long_description = readme.read().decode('utf-8')


class DelayedInclude:
    def __str__(self):
        import pybind11
        return pybind11.get_include()


setup(
    name='pysimdjson',
    packages=find_packages(),
    version='2.0.0',
    description='simdjson bindings for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Tyler Kennedy',
    author_email='tk@tkte.ch',
    url='http://github.com/TkTech/pysimdjson',
    keywords=['json', 'simdjson', 'simd'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
    ],
    python_requires='>3.4',
    extras_require={
        'build': [
            'pybind11'
        ],
        'dev': [
            'm2r',
            'sphinx',
            'ghp-import',
            'bumpversion',
            'pytest',
            'pytest-benchmark'
        ],
        'benchmark': [
            'orjson',
            'python-rapidjson',
            'simplejson',
        ]
    },
    ext_modules=[
        Extension(
            'csimdjson',
            [
                'simdjson/binding.cpp',
                'simdjson/simdjson.cpp'
            ],
            include_dirs=[
                DelayedInclude()
            ],
            language='c++',
            extra_compile_args=[
                '-std=c++17'
            ]
        )
    ]
)
