import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timew-videogamerm", # Replace with your own username
    version="0.0.1",
    author="Mason Withers",
    author_email="N/a",
    description="Wait anount of time",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/videogamerm/Timew",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)