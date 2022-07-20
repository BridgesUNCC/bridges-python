import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bridges",
    version="3.4.0",
    author="BRIDGES",
    author_email="bridges.uncc@gmail.com",
    description="Bridging Real-world Infrastructure Designed to Goal-align, Engage, and Stimulate, an NSF TUES",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BridgesUNCC/bridges-python",
    packages=setuptools.find_packages(exclude=("tests")),
    python_requires='>3.5.2',
    install_requires=[
        'requests>=2.21.0',
        'webcolors>=1.8.1',
        'python-socketio[client]>=4.3.0',
        'SPARQLWrapper>=1.8.4',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
