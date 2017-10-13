from ApkInstaller import ApkInstaller
from AdbShellAdapter import AdbShellAdapter
import getopt, sys
from Log import log_e, log_d
from DeviceConnector import DeviceConnector
import Const
from AutomationExecutor import AutomationExecutor
import TestSuite

class DeviceInitialization:

    TESTER_DICT = {'tester_a': 'login.EmailLogIn#testLogIn_tester_a', 'tester_b': 'login.EmailLogIn#testLogIn_tester_b', 'tester_c': 'login.EmailLogIn#testLogIn_tester_c'}

    def __init__(self):
        self.apkInstaller = ApkInstaller()
        self.adbAdapter = AdbShellAdapter()
        self.deviceConnector = DeviceConnector()
        self.automationExecutor = AutomationExecutor()

    def do_init(self, test_account):
        if not test_account in self.TESTER_DICT :
            return False
        # Install app and test apk
        device_id, port = self.deviceConnector.get_deviceid_and_validport()
        self.apkInstaller.install_apks(device_id)

        # Auto Email login
        test_name = self.TESTER_DICT[test_account]
        test_claz = '{0}.{1}'.format(TestSuite.SOOCII_PACKGE_NAME, test_name)
        self.automationExecutor.run_automation(device_id, test_claz)

        return True


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ha:", ["account="])
    except getopt.GetoptError as err:
        # print help information and exit:
        log_e(str(err))
        print('DeviceInitialization.py -a <account>')
        sys.exit(2)

    test_account = ''
    for opt, arg in opts:
        if opt == '-h':
            print('    DeviceInitialization.py -a <account> [tester_a | tester_b | tester_c]')
            sys.exit()
        elif opt in ("-a", "--account"):
            test_account = arg

    device_init = DeviceInitialization()
    device_init.do_init(test_account)


if __name__ == '__main__':
  main()