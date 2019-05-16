#!/usr/bin/env python

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import jcs

def main():
    jdev = Device()
    jdev.open()

    rpc_call = jdev.rpc.get_chassis_inventory()
    serial_number = rpc_call.findtext('chassis/serial-number')
    hostname_serial = "CPE-" + serial_number

    commands = []
    commands.append("set system host-name " + str(hostname_serial))
    commands.append("delete event-options generate-event ztp-lic")
    commands.append("delete event-options policy ztp-lic")
    commands.append("delete event-options event-script file cpe-hostname.py")

    cu = Config(jdev)
    cu.lock()
    for cmd in commands:
        cu.load(cmd, format="set", merge=True)
    cu.commit(comment="Set CPE hostname")
    cu.rescue(action="save")
    cu.unlock()

    jdev.close()

if __name__ == '__main__':
    main()

