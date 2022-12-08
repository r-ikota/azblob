from setuptools import setup

setup(
    name="azblob",
    version="0.1.0",
    description="",
    url="https://github.com/r-ikota",
    packages=["azblob"],
    package_dir={"azblob": "azblob"},
    author="Ryo Ikota",
    author_email="r.ikota.mt@gmail.com",
    entry_points={"console_scripts": ["azb=azblob.azb_cli:main",],},
    license="BSD",
    keywords="note-system, markdown",
)
