import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/tmp/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_hosts_contains_node1_host(host):
    f = host.file('/tmp/hosts')
    print(f.content)
    assert 'node1' in f.content


def test_hosts_contains_node2_host(host):
    f = host.file('/tmp/hosts')
    assert 'node2' in f.content
