from setuptools import setup, find_packages

setup(
    name="smartpi_dht",
    version="0.1.0",
    description="A package to read DHT11/DHT22 temperature and humidity sensors on Smart Pi One.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "Adafruit_DHT",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
