# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from yoloelections.p5theme.testing import YOLOELECTIONS_P5THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that yoloelections.p5theme is properly installed."""

    layer = YOLOELECTIONS_P5THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if yoloelections.p5theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'yoloelections.p5theme'))

    def test_browserlayer(self):
        """Test that IYoloelectionsP5ThemeLayer is registered."""
        from yoloelections.p5theme.interfaces import (
            IYoloelectionsP5ThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IYoloelectionsP5ThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = YOLOELECTIONS_P5THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['yoloelections.p5theme'])

    def test_product_uninstalled(self):
        """Test if yoloelections.p5theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'yoloelections.p5theme'))

    def test_browserlayer_removed(self):
        """Test that IYoloelectionsP5ThemeLayer is removed."""
        from yoloelections.p5theme.interfaces import \
            IYoloelectionsP5ThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IYoloelectionsP5ThemeLayer, utils.registered_layers())
