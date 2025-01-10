from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHER_NAME = 'Ankur Dwivedi'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHER_NAME,
    author_email = 'ankurkumardwivedi779@gmail.com',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = [SRC_REPO],
    python_requires = '>=3.12',
    install_requires = LIST_OF_REQUIREMENTS
)