from setuptools import setup, find_packages
setup(
    name='CRDCLib',
    version='0.1.0',
    author='Todd Pihl',
    author_email='todd.pihl@nih.gov',
    description='A collection of functions useful for interactive with parts of CRDC',
    packages=find_packages(),
    classifiers=[
        'Programming Language::Python::3',
        'License::OSI Approved::Apache License 2.0',
        'Operating System::OS Independent'
    ],
    python_requires='>=3.12'
    )