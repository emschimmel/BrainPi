from setuptools import setup, find_packages

setup(
    name="AgendaPi",
    version="0.1",
    packages=find_packages(),
    install_requires = [
        'thrift',
        'datetime',
        'pyicloud'
    ],
    entry_points={
        'setuptools.installation': [
            'eggsecutable = src.__main__:main'
        ],
        'console_scripts': [
            'AgendaPi = AgendaPi.src.__main__:main'
        ]
    },
    package_data={'': ['../../config.py']},
    include_package_data=True,
)