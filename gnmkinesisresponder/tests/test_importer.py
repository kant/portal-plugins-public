import unittest2
from mock import MagicMock, patch
import os.path
from boto import kinesis
from datetime import datetime
import logging
from django.core.management import execute_manager

logging.basicConfig(level=logging.DEBUG)

import django_test_settings as django_test_settings

os.environ["DJANGO_SETTINGS_MODULE"] = "django_test_settings"
if(os.path.exists(django_test_settings.DATABASES['default']['NAME'])):
    os.unlink(django_test_settings.DATABASES['default']['NAME'])

execute_manager(django_test_settings,['manage.py','syncdb'])
execute_manager(django_test_settings,['manage.py','migrate'])


class TestImporter(unittest2.TestCase):
    def test_make_pluto_holding_image(self):
        from gnmkinesisresponder.master_importer import MasterImportResponder
        import json

        conn = kinesis.connect_to_region('eu-west-1')
        r = MasterImportResponder(conn,"test_stream","noshard")

        jsondata = r.make_pluto_holding_image("https://path/to/some/image.jpg")
        decoded = json.loads(jsondata)

        self.assertEqual(decoded,{'url_16x9': "https://path/to/some/image.jpg",
                                  'id_16x9': "",
                                  'filename_16x9': "image.jpg"})

    def test_process(self):
        from gnmkinesisresponder.master_importer import MasterImportResponder

        testdatapath = os.path.realpath(os.path.dirname(__file__)) + "/data/atom_response.json"
        conn = kinesis.connect_to_region('eu-west-1')
        r = MasterImportResponder(conn,"test_stream","noshard")

        with open(testdatapath,"r") as f:
            content = f.read()

        with patch('gnmvidispine.vs_item.VSItem.createPlaceholder') as mockcreate:
            r.process(content,datetime.now())

            mockcreate.assert_called_once()