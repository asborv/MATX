# Package for [Matematikk X](https://www.udir.no/kl06/mat2-01)

--------------------------------------------------------------

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
Explanation found [here](https://stackoverflow.com/questions/6590688/is-it-bad-to-have-my-virtualenv-directory-inside-my-git-repositor)
