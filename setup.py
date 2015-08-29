from setuptools import setup

setup(name='sync',
    description='Sync files of 2 different directories',
    version='0.1.0',
    author='Harsha Srinivas',
    author_email='95harsha95@gmail.com',
    packages=['sync'],
    entry_points={
        'console_scripts': ['sync=sync:main'],
    },
    url='https://github.com/harshasrinivas/sync/',
    keywords=[ 'CLI', 'python'],
    classifiers=[
        'Operating System :: POSIX',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
  ],)
