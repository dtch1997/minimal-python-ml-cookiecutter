from distutils.core import setup

setup(
    name="{{cookiecutter.package_name}}",
    version="{{cookiecutter.version}}",
    description="{{cookiecutter.package_short_description}}",
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    packages=["{{cookiecutter.package_name}}"],
)