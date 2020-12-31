from setuptools import setup, find_packages

setup(
    name = 'awesomecode',
    version='1.0.0',
    install_requires=[
        'pytest'
        , 'cython'
        , 'numpy'
        ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            ''
        ]
    }
)