import setuptools
import linux_profile

version = linux_profile.__version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="linux-profile",
    version=version,
    author="Fernando Celmer",
    author_email="email@fernandocelmer.com",
    description="Python Linux Profile",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MyLinuxProfile/linux-profile-pypi",
    license="MIT",
    packages=[
        'linux_profile',
    ],
    include_package_data=True,
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    zip_safe=False,
    platforms="linux"
)
