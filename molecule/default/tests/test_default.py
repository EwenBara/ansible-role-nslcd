import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    assert host.package("nss-pam-ldapd").is_installed

    f = host.file('/etc/nslcd.conf')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o600

    s = host.service("nslcd")
    assert s.is_running
    assert s.is_enabled
