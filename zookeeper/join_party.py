"""
Joins a worker to the celery worker party
"""

import time
import click
from host_info import get_hosts_with_port
from get_client import get_client


@click.command()
@click.argument("znode")
@click.argument("identifier")
@click.argument("host", default=get_hosts_with_port(3))
def main(host: str, znode: str, identifier: str):
    zk = get_client(host)
    zk.start()
    party = zk.Party(znode, identifier=identifier)
    party.join()
    while True:
        time.sleep(1)
    zk.stop()


if __name__ == "__main__":
    main()
