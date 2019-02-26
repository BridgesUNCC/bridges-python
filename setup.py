import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bridges",
    version="2.4.1.3",
    author="BRIDGES",
    author_email="bridges.uncc@gmail.com",
    description="Bridging Real-world Infrastructure Designed to Goal-align, Engage, and Stimulate, an NFS TUES",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krs-world/bridges-python",
    packages=setuptools.find_packages(exclude=("tests")),
    python_requires='>3.5.2',
    install_requires=[
        'requests>=2.21.0',
        'webcolors>=1.8.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
