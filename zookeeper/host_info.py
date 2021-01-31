ZOOKEEPER_HOSTS = "zookeeper1:2181,zookeeper2:2181,zookeeper3:2181"


def get_hosts(count: int):
    return [f"zookeeper{i}" for i in range(count)]


def get_hosts_with_port(count: int):
    return [f"{host}:2181" for host in get_hosts(count)]
