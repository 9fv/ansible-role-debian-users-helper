import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user1(host):
    u = host.user('user1')
    assert u is not None
    assert u.shell == '/bin/bash'


def test_user2(host):
    u = host.user('user2')
    assert u is not None
    assert u.shell == '/bin/sh'


# def test_user3(host):
#    u = host.user('user3')
#    assert u is None
