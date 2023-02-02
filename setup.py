from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sadbhavna_donatekart/__init__.py
from sadbhavna_donatekart import __version__ as version

setup(
	name="sadbhavna_donatekart",
	version=version,
	description="this app for sadbhavna donatekart",
	author="Sanskar Technolab",
	author_email="nilesh@sanskartechnolab.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
