from distutils.core import setup
import os

setup(
    name='pythonpy',
    version='0.1.3',
    packages=['pythonpy',],
    scripts=[os.path.join('bin', 'pythonpy')],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)
