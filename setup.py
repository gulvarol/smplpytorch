import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [
    "opencv-python",
    "matplotlib",
    "numpy"]

setuptools.setup(
    name="smpl-pytorch",
    version="0.0.7",
    author="Gul Varol",
    author_email="gulvarols@gmail.com",
    python_requires=">=3.5.0",
    install_requires=REQUIREMENTS,
    description="SMPL human body layer for PyTorch is a differentiable PyTorch layer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gulvarol/smpl-pytorch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
