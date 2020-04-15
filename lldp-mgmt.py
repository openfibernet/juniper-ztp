#!/usr/bin/env python

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import jcs

def main():
    jdev = Device()
    jdev.open()

    rsp = jdev.rpc.get_interface_information(terse=True, interface_name='irb.*')
    search = rsp.xpath("//ifa-local")

    lldp_conf = jdev.rpc.get_config(filter_xml='protocols/lldp/management-address')
    current_mgmt_addr = lldp_conf.xpath("//management-address")
    mgmt_addr = ""
    commands = []

    if current_mgmt_addr:
        mgmt_addr = current_mgmt_addr[0].text.strip()

    if search:
        address = search[0].text.strip().split("/")[0]

        if mgmt_addr != address:
            commands.append("set protocols lldp management-address " + str(address))
    else:
        if mgmt_addr:
            commands.append("delete protocols lldp management-address")

    if len(commands) > 0:
        cu = Config(jdev)
        cu.lock()
        for cmd in commands:
            cu.load(cmd, format="set", merge=True)
        cu.commit(comment="Changing LLDP mgmt IP")
        cu.rescue(action="save")
        cu.unlock()

    jdev.close()

if __name__ == '__main__':
    main()

