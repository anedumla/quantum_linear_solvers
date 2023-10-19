from setuptools import find_packages, setup

name = "quantum_linear_solvers"
version = "0.1.1"
description = (
    "Quantum linear solvers package for qiskit"
)

with open("README.md") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    install_requires = f.read()

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    install_requires=install_requires,
    packages=find_packages(),
    use_scm_version=True,
    include_package_data=True,
    license="Apache License 2.0",
    python_requires='>=3.7, <4',
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Physics",
    ],
)
