from setuptools import setup, find_packages

setup(
    name="AdminConsole",
    version="0.1",
    packages=find_packages(),
    install_requires = [
        'Cython==0.26.1',
        'kivy',
        'pygame'
    ]

)