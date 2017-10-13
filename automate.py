import getopt, sys
import argparse
from DeviceInitialization import DeviceInitialization
from DeviceConnector import DeviceConnector
from AutomationExecutor import AutomationExecutor
from AdbShellAdapter import AdbShellAdapter
import TestSuite

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', dest='init_account', help='Install and auto login [tester_a | tester_b | tester_c]', action='store')
    parser.add_argument('-w', help='Connect device via wifi', action='store_true')
    parser.add_argument('-l', help='List attached devices (IP/ID)', action='store_true')
    parser.add_argument('-t', dest='test_suite', help='Specify test suite [test_suite_01 | test_suite_02]')
    parser.add_argument('-d', dest='device_id', help='specify device ID or IP')

    parsed = parser.parse_args()

    if parsed.init_account is not None:
        test_account = parsed.init_account
        device_init = DeviceInitialization()
        device_init.do_init(test_account)
    elif parsed.w:
        device_conn = DeviceConnector()
        device_conn.connect_device_wireless()
    elif parsed.l:
        adb_adpter = AdbShellAdapter()
        print(adb_adpter.adb_devices())
    elif parsed.test_suite is not None:
        if parsed.device_id is not None:
            automation_execute = AutomationExecutor()
            test_suite = TestSuite.TEST_SUITE_DICT[parsed.test_suite]
            automation_execute.run_test_suite(parsed.device_id, test_suite)
        else:
            print("Require device id for test suite!!")


if __name__ == '__main__':
  main()