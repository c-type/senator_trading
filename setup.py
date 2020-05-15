from setuptools import setup

def readme():
      with open('README.rst') as f:
            return f.read()

setup(name='senator_trading',
      version='0.3',
      description='Reads in publicly available stock trading information of senators',
      url='https://github.com/c-type/senator_trading',
      author='ctype',
      author_email='ctypecodes@gmail.com',
      license='MIT',
      packages=['senator_trading'],
      install_requires=[
          'pandas', 'numpy', 'datetime', 'requests', 'matplotlib'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)


