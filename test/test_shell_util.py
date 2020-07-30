from unittest import TestCase

from main.common.util import file_util, shell_util

class TestShellUtil(TestCase):

    def test_run_cmd(self):
        shell_util.run_cmd('ldd')

    def test_run_cmd_popen(self):
        stream = shell_util.run_cmd_popen('ls -l')
        print(stream.read())
        stream.close()
        
    def test_run_asr_script(self):
        cmd = "%s 111" % file_util.get_app_file('webapp/tool/asr/run.sh')
        stream = shell_util.run_cmd_popen(cmd)
        print(stream.read())
        stream.close()
