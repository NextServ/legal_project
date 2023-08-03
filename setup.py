from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in legal_project/__init__.py
from legal_project import __version__ as version

setup(
	name="legal_project",
	version=version,
	description="Extends existing Project Management module to accommodate requirements of a law firm",
	author="Xurpas",
	author_email="ton@xurpas.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
