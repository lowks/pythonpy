from distutils.core import setup
import os

setup(
    name='pythonpy',
    version='0.1.8dev',
    description='Command line utility for Python',
    scripts=[os.path.join('bin', 'pythonpy')],
    license='MIT',
    long_description=open('README.txt').read(),
)
