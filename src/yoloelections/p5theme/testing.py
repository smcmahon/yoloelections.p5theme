# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import yoloelections.p5theme


class YoloelectionsP5ThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=yoloelections.p5theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'yoloelections.p5theme:default')


YOLOELECTIONS_P5THEME_FIXTURE = YoloelectionsP5ThemeLayer()


YOLOELECTIONS_P5THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(YOLOELECTIONS_P5THEME_FIXTURE,),
    name='YoloelectionsP5ThemeLayer:IntegrationTesting'
)


YOLOELECTIONS_P5THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(YOLOELECTIONS_P5THEME_FIXTURE,),
    name='YoloelectionsP5ThemeLayer:FunctionalTesting'
)


YOLOELECTIONS_P5THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        YOLOELECTIONS_P5THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='YoloelectionsP5ThemeLayer:AcceptanceTesting'
)
