import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mfrc522",
    version="0.0.7",
    author="MountainPine",
    author_email="hi@mptw.me",
    description="A library to integrate the MFRC522 RFID readers with the Orange Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MountainPineTW/MFRC522-python-OPi",
    packages=setuptools.find_packages(),
    install_requires=[
        'OPi.GPIO==0.5.2',
        'spidev'
        ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: POSIX :: Linux",
        'Topic :: System :: Hardware',
    ],
)
