# Copyright (c) {{ cookiecutter.year }}, {{ cookiecutter.full_name }}
#
# Distributed under the 3-clause BSD license, see accompanying file LICENSE
# or {{ cookiecutter.url }} for details.

from __future__ import annotations

from setuptools import setup  # isort:skip

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension  # isort:skip

# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

ext_modules = [
    Pybind11Extension(
        "{{ cookiecutter.project_slug }}._core",
        ["src/main.cpp"],
        cxx_std=11,
    ),
]


setup(
    ext_modules=ext_modules,
)
