from setuptools import setup, find_packages

setup(
    name='windows-forensics-tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pywin32',
        'pandas',
        'colorama',
        'browser-history',
        'pyregf'
    ],
    entry_points={
        'console_scripts': [
            'winforensics=forensics.main:main'
        ]
    }
)