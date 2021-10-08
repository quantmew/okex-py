
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="okex-py",
    version="0.0.1",
    author="Jun Wang",
    author_email="jstzwj@aliyun.com",
    description="OKEX python sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quantmew/okex-py",
    project_urls={
        "Bug Tracker": "https://github.com/quantmew/okex-py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
)