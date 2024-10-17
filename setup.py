from setuptools import setup, find_packages

setup(
    name="smartpi_dht",
    version="0.1.0",
    description="A package to read DHT11/DHT22 temperature and humidity sensors without external libraries.",
    author="ADNRoboticsfr",
    author_email="adnroboticsfr@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
