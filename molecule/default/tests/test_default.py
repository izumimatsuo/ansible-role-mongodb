import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mongodb_is_installed(host):
    package = host.package("mongodb-org")
    assert package.is_installed
    assert package.version.startswith("3.6")


def test_mongod_running_and_enabled(host):
    service = host.service("mongod")
    assert service.is_running
    assert service.is_enabled


def test_mongod_is_listen(host):
    assert host.socket("tcp://127.0.0.1:27017").is_listening
