from AdbShellAdapter import AdbShellAdapter
import ipaddress
from Log import log_d, log_e


class DeviceConnector:

    def __init__(self):
        self.adbAdapter = AdbShellAdapter()

    def connect_device_wireless(self):
        device_id, port = self.get_deviceid_and_validport()
        ip = self.adbAdapter.get_device_wifi_ip(device_id)
        if not self.is_valid_ip(ip):
            print("Please check device WiFi connection")
            return

        self.adbAdapter.adb_tcpip(device_id, port)
        if self.adbAdapter.connect_device_via_wifi(device_id, ip, port):
            print("Successfully connect to {0}".format(device_id))
            print("Remove USB connect!")
            return ip, port
        else:
            print("Failed connect to {0}".format(device_id))
            return None

    def get_deviceid_and_validport(self):

        attached_devices = self.adbAdapter.adb_devices()
        used_ports = []
        deviceIds = []
        for device in attached_devices:
            if ":" in device:
                port = int(device.split(":")[1])
                used_ports.append(port)
            else:
                deviceIds.append(device)

        valid_port = 8888
        if len(used_ports) > 0:
            used_port_max = max(used_ports)
            valid_port = used_port_max + 1
        log_d('ID:{0}, Port:{1}'.format(deviceIds[0], valid_port))
        return deviceIds[0], valid_port

    def is_valid_ip(self, ip):
        try:
            ipAddr = ipaddress.ip_address(ip)
            return True
        except ValueError as e:
            print(e)
            return False


def main():
    deviceConnector = DeviceConnector()
    deviceConnector.connect_device_wireless()

if __name__ == '__main__':
        main()