from unittest import TestCase

from main.common.util import file_util

class TestFileUtil(TestCase):

    def test_get_webapp_dir(self):
        print(file_util.get_webapp_dir())
    
    def test_get_tmp_dir(self):
        print(file_util.get_tmp_dir())
