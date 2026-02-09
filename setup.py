from setuptools import setup, find_packages

setup(
    name="cv-optimizer",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        "console_scripts": [
            "cv-optimize=cv_optimizer.main:main"
        ]
    },
)
