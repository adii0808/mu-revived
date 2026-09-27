"""
Copyright (c) 2015-2017 Nicholas H.Tollervey and others (see the AUTHORS file).

Based upon work done for Puppy IDE by Dan Pope, Nicholas Tollervey and Damien
George.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from importlib.resources import files
from PyQt6.QtGui import QPixmap, QIcon, QMovie
from PyQt6.QtCore import QDir
import os


# The following lines add the images and css directories to the search path.
_RESOURCES = files(__name__)


def resource_filename(package, resource):
    """
    Return a filesystem path to a resource bundled with Mu.

    Replacement for the removed pkg_resources.resource_filename. Mu is always
    installed as a regular (non-zipped) package so the traversable is a real
    path on disk.
    """
    return str(_RESOURCES.joinpath(resource))


def resource_string(package, resource):
    """Return the bytes content of a bundled resource."""
    return _RESOURCES.joinpath(resource).read_bytes()


QDir.addSearchPath("images", resource_filename(__name__, "images"))
QDir.addSearchPath("css", resource_filename(__name__, "css"))


def path(name, resource_dir="images/", ext=""):
    """Return the filename for the referenced image."""
    return resource_filename(__name__, resource_dir + name + ext)


def load_icon(name):
    """Load an icon from the resources directory."""
    svg_path = path(name, ext=".svg")
    if os.path.exists(svg_path):
        svg_icon = QIcon(svg_path)
        if svg_icon:
            return svg_icon
    return QIcon(path(name))


def load_pixmap(name, size=None):
    """Load a pixmap from the resources directory."""
    if size is not None:
        icon = load_icon(name)
        return icon.pixmap(size)
    return QPixmap(path(name))


def load_movie(name):
    """Load an animated GIF from the resources directory."""
    return QMovie(path(name))


def load_stylesheet(name):
    """Load a CSS stylesheet from the resources directory."""
    return resource_string(__name__, "css/" + name).decode("utf8")


def load_font_data(name):
    """
    Load the (binary) content of a font as bytes
    """
    return resource_string(__name__, "fonts/" + name)
