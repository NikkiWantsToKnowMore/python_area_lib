from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="area_of_a_figure_lib",
    version="0.1.0",
    author="Nikita Gromov",
    author_email="email@example.com",
    description="A library for calculating areas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/examplename/area_of_a_figure_lib",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)