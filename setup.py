from setuptools import find_packages, setup

setup(
  name="matx",
  packages=find_packages(include=["matx"]),
  version="0.1.0",
  description="Module for Matematikk X",
  author="Asbjørn Olav Orvedal",
  author_email="asbjorn.orvedal@gmail.com",
  license="MIT",
  install_requires=[],
  setup_requires=["pytest-runner", "wheel"],
  tests_require=["pytest"],
  test_suite="tests"
)