from setuptools import setup, find_packages

setup(
    name="project_src",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ],
    scripts=['./bin/test_script']
)
