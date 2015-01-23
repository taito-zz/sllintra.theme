from Products.CMFCore.utils import getToolByName
from sllintra.theme.tests.base import IntegrationTestCase


def get_css_resource(obj, name):
    return getToolByName(obj, 'portal_css').getResource(name)


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_package_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('sllintra.theme'))

    def test_browserlayer(self):
        from sllintra.theme.browser.interfaces import ISllintraThemeLayer
        from plone.browserlayer import utils
        self.failUnless(ISllintraThemeLayer in utils.registered_layers())

    def test_cssregistry__sll_theme_main__applyPrefix(self):
        resource = get_css_resource(self.portal, '++resource++sllintra.theme/css/main.css')
        self.assertTrue(resource.getApplyPrefix())
        self.assertFalse(resource.getAuthenticated())
        self.assertEqual(resource.getCompression(), 'safe')
        self.assertEqual(resource.getConditionalcomment(), '')
        self.assertTrue(resource.getCookable())
        self.assertTrue(resource.getEnabled())
        self.assertEqual(resource.getExpression(), '')
        self.assertEqual(resource.getMedia(), 'screen')
        self.assertEqual(resource.getRel(), 'stylesheet')
        self.assertEqual(resource.getRendering(), 'link')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__sll_theme_extra__applyPrefix(self):
        resource = get_css_resource(self.portal, '++resource++sllintra.theme/css/extra.css')
        self.assertTrue(resource.getApplyPrefix())
        self.assertFalse(resource.getAuthenticated())
        self.assertEqual(resource.getCompression(), 'safe')
        self.assertEqual(resource.getConditionalcomment(), '')
        self.assertTrue(resource.getCookable())
        self.assertTrue(resource.getEnabled())
        self.assertEqual(resource.getExpression(), '')
        self.assertEqual(resource.getMedia(), 'screen')
        self.assertEqual(resource.getRel(), 'stylesheet')
        self.assertEqual(resource.getRendering(), 'link')
        self.assertIsNone(resource.getTitle())

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-sllintra.theme:default'), u'0')

    def test_uninstall(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sllintra.theme'])
        self.failIf(installer.isProductInstalled('sllintra.theme'))

    def test_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sllintra.theme'])
        from sllintra.theme.browser.interfaces import ISllintraThemeLayer
        from plone.browserlayer import utils
        self.failIf(ISllintraThemeLayer in utils.registered_layers())
