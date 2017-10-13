import time
import datetime
import Const
import os
from Log import log_e, log_d
from AdbShellAdapter import AdbShellAdapter

class LogDump:

    def dump_load(self, device_id):
        if not os.path.isdir(Const.LOG_FOLDER_NAME):
            os.mkdir(Const.LOG_FOLDER_NAME)

        adb_shell = AdbShellAdapter()
        log_path = self._get_log_name(device_id)
        log_file = open(log_path, 'w')
        command = 'adb -s {0} logcat -d -v threadtime'.format(device_id)
        log_d(command)
        log_file.write(adb_shell.adb_execute(command))

    def _get_log_name(self, device_id):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%-H%M%S')
        return '{0}/log_{1}_{2}.txt'.format(Const.LOG_FOLDER_NAME, device_id, st)
