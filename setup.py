from setuptools import setup, find_packages
import pathlib

thispath = pathlib.Path(__file__).parent.resolve()
long_description = thispath / "README.md"

setup(
    name="CRDCLib",
    version="0.0.1",
    description="Random routines I use in CRDC work",
    long_description=long_description,
    url="https://github.com/pihltd/CRDCLib",
    author="Todd Pihl",
    author_email="todd.pihl@gmail.com",
    classifiers=[
        "Developement Status ::  3 - Alpha"
        "License :: OSI Approved :: Apache 2.0"
        "Programming Language :: Python :: 3"
    ],
    package_dir={"": "src/CRDCLib"},
    packages=find_packages(where="src/CRDCLib"),
    python_requires=">=3.6",
    install_requires=["requests", "pyyaml"],
    project_urls={
        "Source": "https://github.com/pihltd/CRDCLib",
        "Issues": "https://github.com/pihltd/CRDCLib/issues"
    }
)
