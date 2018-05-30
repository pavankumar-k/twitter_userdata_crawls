# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    package_data={
        'twitter': ['resources/*.txt']
    },
    entry_points={
        'scrapy': ['settings = twitter.settings']
    },
    zip_safe=False,
)
