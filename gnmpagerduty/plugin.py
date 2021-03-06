import logging

from portal.pluginbase.core import Plugin, implements
from portal.generic.plugin_interfaces import (IPluginURL, IPluginBlock, IAppRegister,)


log = logging.getLogger(__name__)

class GnmpagerdutyPluginURL(Plugin):
    """ Adds a plugin handler which creates url handler for the index page """
    implements(IPluginURL)

    def __init__(self):
        self.name = "Gnmpagerduty App"
        self.urls = 'portal.plugins.gnmpagerduty.urls'
        self.urlpattern = r'^gnmpagerduty/'
        self.namespace = r'gnmpagerduty'
        self.plugin_guid = '455bd5h0-37e5-41db-9ad4-8e26927a1dc8'
        log.debug("Initiated Gnmpagerduty App")

pluginurls = GnmpagerdutyPluginURL()

class GnmpagerdutyAdminNavigationPlugin(Plugin):
    implements(IPluginBlock)

    def __init__(self):
        self.name = "NavigationAdminPlugin"
        self.plugin_guid = 'a592ba56-f5b1-71a1-af5d-efa50e2e15ca'
        log.debug('Initiated navigation plugin')

    def return_string(self, tagname, *args):
        return {'guid': self.plugin_guid, 'template': 'gnmpagerduty/menu_nav.html'}

navplug = GnmpagerdutyAdminNavigationPlugin()

class GnmpagerdutyRegister(Plugin):
    implements(IAppRegister)

    def __init__(self):
        self.name = "Gnmpagerduty Registration App"
        self.plugin_guid = '83bac670-61c2-4162-8a67-7da2f4975522'
        log.debug('Register the App')

    def __call__(self):
        from __init__ import __version__ as versionnumber
        _app_dict = {
                'name': 'GNM PagerDuty',
                'version': '1.0.0',
                'author': 'Dave Allison and Andy Gallagher',
                'author_url': 'www.theguardian.com/',
                'notes': 'Allows alerts to be sent to PagerDuty when storages get too full'}
        return _app_dict

gnmpagerdutyplugin = GnmpagerdutyRegister()

class GnmpagerdutyAdminPlugin(Plugin):
    implements(IPluginBlock)

    def __init__(self):
        self.name = "AdminLeftPanelBottomPanePlugin"
        self.plugin_guid = '285f8224-de4a-14d5-99ff-60032890073c'
        log.debug('initiated GNMpagerduty admin panel')

    def return_string(self,tagname,*args):
        return {'guid': self.plugin_guid, 'template': 'gnmpagerduty/navigation.html'}

adminplug = GnmpagerdutyAdminPlugin()



