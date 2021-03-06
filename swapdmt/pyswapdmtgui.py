#########################################################################
#
# Copyright (c) 2011 Daniel Berenguer <dberenguer@usapiens.com>
#
# This file is part of the panStamp project.
#
# panStamp  is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# panStamp is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with panLoader; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301
# USA
#
#########################################################################
__author__  = "Daniel Berenguer"
__date__    = "$Aug 25, 2011$"
#########################################################################

from SwapManager import SwapManager

import os
import sys


if __name__ == "__main__":
    # Path to the SWAP config file
    settings = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "config", "settings.xml")

    # Start SWAP manager tool
    manager = SwapManager(settings)

