from setuptools import find_packages, setup

# Read version from the __init__ file
def get_version_from_source(filename):
    import ast

    version = None
    with open(filename) as f:
        for line in f:
            if line.startswith("__version__"):
                version = ast.parse(line).body[0].value.s
                break
        else:
            raise ValueError("No version found in %r." % filename)
    if version is None:
        raise ValueError(filename)
    return version


import yaml

with open("project.pp1.yaml") as f:
    data = yaml.load(f, Loader=yaml.Loader)

install_requires = data["install_requires"]
tests_require = data["tests_require"]

console_scripts = [f"{k} = {v}" for k, v in data["console_scripts"].items()]
package_name = data["package_name"]
packages = data["modules"]
main_package = packages[0]
version = get_version_from_source(f"src/{main_package}/__init__.py")

# setup package
params = dict(
    name=package_name,
    author=data["author"],
    author_email=data["author_email"],
    url=data["url"],
    tests_require=tests_require,
    install_requires=install_requires,
    package_dir={"": "src"},
    packages=find_packages("./src"),
    long_description="",
    version=version,
    entry_points={"console_scripts": console_scripts},
)

setup(**params)

# sigil 2f717c3d4b5b72c26e2cc7a387610790
