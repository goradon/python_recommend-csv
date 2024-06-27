try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


setup(
    name='python_recommend-csv',
    version='1.0.0',
    packages=['gorabot', 'gorabot.models', 'gorabot.controller', 'gorabot.views'],
    # You could use find_packages if setuptools is installed. 
    # packages=find_packages(),
    package_data={ 'gorabot': ['templates/*.txt'] },
    url='',
    license='',
    author='goradon',
    author_email='',
    # You can specify install_requires if setuptools is installed
    # install_requires=['termcolor==1.1.0'],
    long_description=open('README.txt').read(),
)
