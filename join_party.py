"""
Joins a worker to the celery worker party
"""

from kazoo.client import KazooClient
from kazoo.retry import KazooRetry
from kazoo.recipe.party import Party
from argparse import ArgumentParser
import time
import socket
import click


def wait_for_port(port, host="localhost", timeout=5.0):
    """Wait until a port starts accepting TCP connections.
    Args:
        port (int): Port number.
        host (str): Host address on which the port should exist.
        timeout (float): In seconds. How long to wait before raising errors.
    Raises:
        TimeoutError: The port isn't accepting connection after time specified in `timeout`.
    """
    start_time = time.perf_counter()
    while True:
        try:
            with socket.create_connection((host, port), timeout=timeout):
                break
        except OSError as ex:
            time.sleep(0.01)
            if time.perf_counter() - start_time >= timeout:
                raise TimeoutError(
                    "Waited too long for the port {} on host {} to start accepting "
                    "connections.".format(port, host)
                ) from ex


@click.command()
@click.argument("znode")
@click.argument("identifier")
@click.argument("host", default="zookeeper1:2181,zookeeper2:2181,zookeeper3:2181")
def main(host: str, znode: str, identifier: str):
    wait_for_port(2181, "zookeeper1", 20)
    zk = KazooClient(hosts=host, connection_retry=KazooRetry(20),)
    zk.start()
    party = Party(zk, znode, identifier=identifier)
    party.join()
    while True:
        time.sleep(1)
    zk.stop()


if __name__ == "__main__":
    main()
