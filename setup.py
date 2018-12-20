import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Katjas_kd_tree",
    version="0.0.3",
    author="Katja Della Libera",
    author_email="katja.dellalibera@minerva.kgi.edu",
    description="An implementation of KD trees",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/katjadellalibera/KD-tree-implementation",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy"]
)
