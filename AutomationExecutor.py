from DeviceConnector import DeviceConnector
from AdbShellAdapter import AdbShellAdapter
from Log import log_d, log_e
from LogDump import LogDump
import Const
import TestSuite


class AutomationExecutor:

    def __init__(self):
        self.device_connector = DeviceConnector()
        self.adbAdapter = AdbShellAdapter()
        self.logDump = LogDump()

    def run_automation(self, device_id, claz):
        command = 'adb -s {0} shell am instrument -w -r   -e debug false -e class {1} {2}'.format(device_id, claz, Const.AUTOMATION_TEST_RUNNER)
        self.adbAdapter.adb_execute(command)

    def run_test_suite(self, device_id, test_suite):
        if len(test_suite) == 0:
            log_e("Empty test suite")
        for claz in test_suite:
            test_name = '{0}.{1}'.format(TestSuite.SOOCII_PACKGE_NAME, claz)
            self.run_automation(device_id, test_name)
