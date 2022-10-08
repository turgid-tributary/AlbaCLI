from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="alba-cli",
    version="1.0.0",
    author="Joe MacInnes",
    author_email="jarnance@amazon.com",
    description="AWS Embedded Metrics Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/turgid-tributary/AlbaCLI",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=[],
    entry_points="""\
    [console_scripts]
    alba = alba_cli.main:main
    """,
    test_suite="test",
    python_requires=">=3.6",
)
