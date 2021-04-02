# Package for [Matematikk X](https://www.udir.no/kl06/mat2-01)

-------------------------------------------------------------

## Setup

### Initialisation of virtual environment

The virtual environment for this repository is ignored by git. Therefore you must setup one yourself, as such:

1. Navigate to the root directory of this repository.
1. Initialise virtual environment (for Windows): `python -m venv env`.

### Installing packages

This repository is shipped with a `requirements.txt`-file.
Run `pip install -r requirements.txt` to install all packages needed.

**Important notice:**
When new packages are implemented, add them to `requirements.txt`, by running `pip freeze > requirements.txt` (Windows).
Explanation found [here](https://stackoverflow.com/questions/6590688/is-it-bad-to-have-my-virtualenv-directory-inside-my-git-repositor).
Walkthrough of module setup in [this blog post](https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f).

## Testing

Test files are located in the directory `tests`. In order to run tests, use command `python setup.py pytest` (verify this).

## Build

When the library is ready for build, run `python -m build` ([explanation](https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives)). This creates a `.whl`-file in `/dist`.

## Installation and importing

Once the library has been built, it is ready for installing. This can be done with the command `pip install /path/to/wheelfile.whl`, if the package is not published to [PyPi](https://pypi.org/) (There are no plans to do this as of now).
