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

    set_hostname = "set system host-name " + str(hostname_serial)
    delete_eo = "delete event-options"

    cu = Config(jdev)
    cu.lock()
    cu.load(set_hostname, format="set", merge=True)
    cu.load(delete_eo, format="set", merge=True)
    cu.commit(comment="Set CPE hostname")
    cu.rescue(action="save")
    cu.unlock()

    jdev.close()

if __name__ == '__main__':
    main()

