import ipaddress
import subprocess
from Log import log_d, log_e


class AdbShellAdapter():

    def disconnect_all(self):
        try:
            command_string = 'adb disconnect'
            command_string_list = command_string.split(" ")

            adb_output = subprocess.check_output(command_string_list)
            adb_output_string = adb_output.decode("utf-8")
            log_d(adb_output_string)
        except subprocess.CalledProcessError as e:
            log_e(str(e))

    def adb_tcpip(self, device_id, port):
        try:
            command_string = 'adb -s {0} tcpip {1}'.format(device_id, port)
            command_string_list = command_string.split(" ")

            adb_output = subprocess.check_output(command_string_list)
            adb_output_string = adb_output.decode("utf-8")
            log_d(adb_output_string)
        except subprocess.CalledProcessError as e:
            log_e(str(e))

    def get_device_wifi_ip(self, device_id):
        ip_address = ""
        try:
            command = 'adb -s {0} shell ip addr show wlan0 | grep inet'.format(device_id)
            command_list = command.split(" ")

            adb_output = subprocess.check_output(command_list)
            adb_output_string = adb_output.decode("utf-8")

            adb_output_string_list = adb_output_string.split("\n")
            inet_info_list = adb_output_string_list[0].lstrip().split(" ")

            ip_address = inet_info_list[1].split("/")[0]

        except subprocess.CalledProcessError as e:
            log_e(str(e))

        log_d('defice ip: {0}'.format(ip_address))
        return ip_address

    def connect_device_via_wifi(self, device_id, ip, port):
        try:
            ip_port = "{0}:{1}".format(ip, port)
            command = 'adb -s {0} connect {1}'.format(device_id, ip_port)
            command_list = command.split(" ")

            adb_output = subprocess.check_output(command_list)
            adb_output_string = adb_output.decode("utf-8")

            adb_output_string_list = adb_output_string.split(" ")
            result = adb_output_string_list[0]
            if result == 'connected':
                return True
        except subprocess.CalledProcessError as e:
            print(e)

        return False

    def adb_devices(self):
        attached_device_list = []

        try:
            command = 'adb devices'
            command_list = command.split(" ")

            adb_output = subprocess.check_output(command_list)
            adb_output_string = adb_output.decode("utf-8")

            adb_output_string_list = adb_output_string.split("\n")
            for i, val in enumerate(adb_output_string_list):
                if i > 0 and len(val) > 0:
                    attached_device = val.split("\t")[0]
                    attached_device_list.append(attached_device)
        except subprocess.CalledProcessError as e:
            print(e)

        return attached_device_list

    def adb_push(self, device_id, src, des):
        try:
            command = 'adb -s {0} push {1} {2}'.format(device_id, src, des)
            command_list = command.split(" ")

            adb_output = subprocess.check_output(command_list)
            adb_output_string = adb_output.decode("utf-8")
            if '100%' in adb_output_string:
                log_d("Successfully push {0}!".format(des))
                return True
            else:
                return False

        except subprocess.CalledProcessError as e:
            print(e)
            return False

    def adb_install(self, device_id, path_to_device_apk):
        try:
            command = 'adb -s {0} shell pm install -r {1}'.format(device_id, path_to_device_apk)
            command_list = command.split(" ")
            adb_output = subprocess.check_output(command_list)
            adb_output_string = adb_output.decode("utf-8")
            if 'Success' in adb_output_string:
                log_d("Successfully install {0}!".format(path_to_device_apk))
                return True
            else:
                return False

        except subprocess.CalledProcessError as e:
            log_e(str(e))
            return False

    def adb_uninstall(self, device_id, pkg_name):
        try:
            command = 'adb -s {0} uninstall {1}'.format(device_id, pkg_name)
            command_list = command.split(" ")
            adb_output = subprocess.check_output(command_list)
            adb_output_string = adb_output.decode("utf-8")

        except subprocess.CalledProcessError as e:
            log_e(str(e))
            return False

    def adb_execute(self, command):
        log_d(command)
        try:
            command_list = command.split(" ")

            adb_output = subprocess.check_output(command_list)
            adb_output_string = adb_output.decode("utf-8")
            return adb_output_string
        except subprocess.CalledProcessError as e:
            print(e)
            return None


def main():
    adbShellAdapter = AdbShellAdapter()
    adbShellAdapter.adb_devices()


if __name__ == '__main__':
        main()