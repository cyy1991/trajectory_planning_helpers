import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='trajectory-planning-helpers',
    version='0.18',
    author="Alexander Heilmeier, Tim Stahl",
    author_email="alexander.heilmeier@tum.de, stahl@ftm.mw.tum.de",
    description="Useful functions used for path and trajectory planning at TUM/FTM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ])
