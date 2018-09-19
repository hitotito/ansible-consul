#!/usr/bin/env python
import sys
import subprocess

OK = 0
WARNING = 1
ERROR = 2

try:
    service_name = sys.argv[1]
    CMD_VERIFY = ['systemctl', 'is-active', service_name]
    (out, err) = subprocess.Popen(CMD_VERIFY, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    is_active = out.rstrip() == 'active'
    print ("service[{}] is {}".format(service_name, out))
except Exception as e:
    print ("Exception has been raised while checking for systemd active status")
    is_active = False

sys.exit( OK if is_active else ERROR)
