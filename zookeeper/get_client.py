from wait_for_port import wait_for_port
from kazoo.client import KazooClient
from kazoo.retry import KazooRetry
from host_info import get_hosts


def get_client(hosts: str) -> KazooClient:
    wait_for_port(2181, get_hosts(1), 20)
    return KazooClient(hosts=hosts, connection_retry=KazooRetry(20))
