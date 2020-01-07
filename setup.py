from setuptools import setup, find_packages
from os import path

REPO_URL = "https://github.com/{ORG_NAME}/{PROJECT_NAME}"

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as readme:
    markdown_description = readme.read()

setup(
    name='{PROJECT_NAME}',
    version='v0.0.1',
    packages=find_packages(exclude=["tests", "tests.*"]),
    url=REPO_URL,
    license='GPL-3.0',
    # setup_requires=[],
    # install_requires=[],
    # tests_require=["pytest>=5.0.0,<6.0.0"],
    zip_safe=True,
    python_requires=">=3.5",

    # Metadata for PyPI
    author='{ORG_NAME}',
    author_email='',
    description='Example description',
    keywords="keyword-1 keyword-2 keyword-n",
    project_urls={
        "Bug Tracker": "https://github.com/{ORG_NAME}/{PROJECT_NAME}/issues",
        "Documentation": "https://github.com/{ORG_NAME}/{PROJECT_NAME}/blob/master/README.md",
        "Source Code": "https://github.com/{ORG_NAME}/{PROJECT_NAME}",
        "Download ZIP": "https://api.github.com/repos/{ORG_NAME}/{PROJECT_NAME}/zipball"
    },
    long_description=markdown_description,
    long_description_content_type='text/markup'
)
