from setuptools import setup, find_packages

long_description = open("README.md", "r").read()

requirements = [
]

setup(
    name="GlueGov",
    version="0.1",
    license="mit",
    description="API providing geo based location correlated from the UK Government",
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
)
