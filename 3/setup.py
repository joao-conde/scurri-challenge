import os
import setuptools

setuptools.setup(
    name = "postcodes",
    version = "1.0.0",
    author = "João Conde",
    author_email = "joaodiasconde@gmail.com",
    description = "Postal code related utilities",
    keywords = "postcodes validator formatter",
    packages = [
        "postcodes",
        "postcodes.test"
    ],
    package_dir = {
        "" : os.path.normpath("src")
    },
    test_suite = "postcodes.test",
    classifiers = [
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ]
)
