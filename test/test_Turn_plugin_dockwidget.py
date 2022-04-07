# coding=utf-8
"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'fadeew.alex@mail.ru'
__date__ = '2022-04-06'
__copyright__ = 'Copyright 2022, Fadeev Alex'

import unittest

from qgis.PyQt.QtGui import QDockWidget

from Turn_plugin_dockwidget import Turn_pluginDockWidget

from utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class Turn_pluginDockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = Turn_pluginDockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test we can click OK."""
        pass

if __name__ == "__main__":
    suite = unittest.makeSuite(Turn_pluginDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

