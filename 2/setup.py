import os
import setuptools

setuptools.setup(
    name = "postcodes",
    version = "1.0.0",
    author = "João Conde",
    author_email = "joaodiasconde@gmail.com",
    description = "Postcode utilities",
    keywords = "postcodes shipping",
    packages = [
        "postcode",
        "postcode.test"
    ],
    package_dir = {
        "" : os.path.normpath("src")
    },
    test_suite = "postcode.test",
    classifiers = [
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7"
    ]
)
