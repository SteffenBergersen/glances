# -*- coding: utf-8 -*-
#
# This file is part of Glances.
#
# Copyright (C) 2014 Nicolargo <nicolas@nicolargo.com>
#
# Glances is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Glances is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Common objects shared by all Glances modules."""

import os
import sys

# Global information
appname = 'glances'
version = __import__('glances').__version__
psutil_version = __import__('glances').__psutil_version

# PY3?
is_py3 = sys.version_info >= (3, 3)

# Operating system flag
# Note: Somes libs depends of OS
is_bsd = sys.platform.find('bsd') != -1
is_linux = sys.platform.startswith('linux')
is_mac = sys.platform.startswith('darwin')
is_windows = sys.platform.startswith('win')

# Path definitions
work_path = os.path.realpath(os.path.dirname(__file__))
appname_path = os.path.split(sys.argv[0])[0]
sys_prefix = os.path.realpath(os.path.dirname(appname_path))

# Set the plugins path
plugins_path = os.path.realpath(os.path.join(work_path, '..', 'plugins'))
sys_path = sys.path[:]
sys.path.insert(0, plugins_path)


def get_locale_path(paths):
    for path in paths:
        if os.path.exists(path):
            return path

# i18n
gettext_domain = appname
i18n_path = os.path.realpath(os.path.join(work_path, '..', '..', 'i18n'))
user_i18n_path = os.path.join(os.path.expanduser('~/.local'), 'share', 'locale')
sys_i18n_path = os.path.join(sys_prefix, 'share', 'locale')
locale_dir = get_locale_path([i18n_path, user_i18n_path, sys_i18n_path])
