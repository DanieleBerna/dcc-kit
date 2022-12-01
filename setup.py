import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dcckit",
    version="0.0.6",
    author="Daniele Bernardini",
    author_email="bdcreations@gmail.com",
    description="A package for dealing with DCC softwares and perform operations on game assets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DanieleBerna/dcc-kit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 3 - Alpha"
    ],
    python_requires='>=3.7',
)
