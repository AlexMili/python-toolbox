import setuptools

setuptools.setup(
    name="Toolbox",
    version="0.1.0",
    author="AlexMili",
    description="Some python functions",
    url="https://github.com/AlexMili/python-toolbox",
    packages=setuptools.find_packages(),
    package_data={'resources': ['*']},
    include_package_data=True,
    install_requires=[
        "pandas",
        "opencv-python",
        "matplotlib",
        "Pillow"
    ],
    python_requires=">=3.8",
)
