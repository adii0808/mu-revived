"""
Print Mu's dependencies from pyproject.toml, excluding the PyQt6 packages.

Used where PyQt6 comes from the operating system rather than PyPI (e.g.
Raspberry Pi OS / Debian's python3-pyqt6 packages), so pip doesn't try to
replace it:

    python utils/non_qt_requirements.py [extra ...] > requirements.txt
    pip install -r requirements.txt
    pip install --no-deps .
"""

import re
import sys
import tomllib
from pathlib import Path

PYPROJECT = Path(__file__).resolve().parent.parent / "pyproject.toml"


def main(extras):
    project = tomllib.loads(PYPROJECT.read_text(encoding="utf-8"))["project"]
    requirements = list(project["dependencies"])
    for extra in extras:
        requirements.extend(project["optional-dependencies"][extra])
    for requirement in requirements:
        name = re.split(r"[\s<>=!~;\[]", requirement, maxsplit=1)[0]
        if name.lower().startswith("pyqt6"):
            continue
        if name.lower() == "mu-editor":  # self-referencing extras
            continue
        print(requirement)


if __name__ == "__main__":
    main(sys.argv[1:])
