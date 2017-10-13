from AdbShellAdapter import AdbShellAdapter
import os
import Const
from Log import log_e, log_d
from DeviceConnector import DeviceConnector


class ApkInstaller:

    def __init__(self):
        self.adbAdapter = AdbShellAdapter()
        self.deviceConnector = DeviceConnector()

    def install_apk(self, device_id, apk_name):
        if not os.path.isdir(Const.APK_FOLDER_NAME):
            log_e("APK Folder not exists")
            return False
        automation_apk_path = '{0}/{1}'.format(Const.APK_FOLDER_NAME, apk_name)
        automation_apk_device_path = '{0}/{1}'.format(Const.DEVICE_FOLDER_FOR_AUTOMATION, apk_name)
        if os.path.isfile(automation_apk_path):
            if self.adbAdapter.adb_push(device_id, automation_apk_path, automation_apk_device_path):
                if self.adbAdapter.adb_install(device_id, automation_apk_device_path):
                    return True
                else:
                    log_e("Failed push {0}".format(automation_apk_path))
                    return False
            else:
                log_e("Failed push {0}".format(automation_apk_path))
                return False

    def install_apks(self, device_id):
        self.adbAdapter.adb_uninstall(device_id, Const.AUTOMATION_PACKAGE_NAME)
        self.install_apk(device_id, Const.APK_AUTOMATION_NAME)
        self.install_apk(device_id, Const.APK_AUTOMATION_TEST_NAME)


def main():
    installer = ApkInstaller()
    installer.install_apks()

if __name__ == '__main__':
        main()


