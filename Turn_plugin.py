# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Turn_plugin
                                 A QGIS plugin
 This plugin for QGIS allows user to turn group of vector objects around geometric center.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-04-06
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Fadeev Alex
        email                : fadeew.alex@mail.ru
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, Qt
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

# Initialize Qt resources from file resources.py
from .resources import *

# Import the code for the DockWidget
#from .Turn_plugin_dockwidget import Turn_pluginDockWidget
from .MainWindow import Ui_MainTurnDialog
import os.path


class Turn_plugin:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'Turn_plugin_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []

        #print "** INITIALIZING Turn_plugin"

        self.pluginIsActive = False


    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        self.plugin_icon = QIcon(':/plugins/Turn_plugin/icon.png')
        self.action = QAction(self.plugin_icon, "Turn plugin", self.iface.mainWindow())
        self.action.triggered.connect(Turn_plugin.run)

        self.iface.addToolBarIcon(self.action)


    def unload(self):
        """Removes the plugin button and icon from QGIS GUI."""
        self.iface.removeToolBarIcon(self.action)
        self.plugin_icon = None
        self.action = None
        self.mainWindow = None
        self.pluginIsActive = False

    @classmethod
    def run(self):
        """Run method that loads and starts the plugin"""
        self.pluginIsActive = True
        self.mainWindow = Ui_MainTurnDialog()
        self.mainWindow.show()