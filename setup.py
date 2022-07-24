import linux_profile

from setuptools import find_packages
from setuptools import setup

version = linux_profile.__version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

test_requirements = [
    "pytest"
]

setup(
    name="linux-profile",
    version=version,
    author="Fernando Celmer",
    author_email="email@fernandocelmer.com",
    description="Python Linux Profile",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MyLinuxProfile/linux-profile-pypi",
    license="MIT",
    packages=find_packages(
        exclude=[
            "tests"
        ]
    ),
    tests_require=test_requirements,
    include_package_data=True,
    zip_safe=False,
    platforms="linux",
    python_requires=">=3.9",
    setup_requires=["setuptools >= 40.8.0"],
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 3.9",
    ]
)
