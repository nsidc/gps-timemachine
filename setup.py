from setuptools import setup, find_packages

setup(name='gps-timemachine',
      version='0.2.3',
      description='Adjust GPS datetimes to UTC.',
      url='git@bitbucket.org:nsidc/gps-timemachine.git',
      author='NSIDC Development Team',
      author_email='programmers@nsidc.org',
      license='MIT',
      packages=find_packages(exclude=('tasks',)))
