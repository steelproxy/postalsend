from setuptools import setup, find_packages

setup(
    name="postalsend",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'requests>=2.31.0',
    ],  # Dependencies (if any)
    author="Collin Rodes",
    author_email="steelproxy@protonmail.com",
    description="A library to send messages with the Postal server API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/steelproxy/postal-sender-lib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)