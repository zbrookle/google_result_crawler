from kazoo.client import KazooClient
from kazoo.retry import KazooRetry
from kazoo.recipe.party import Party
import time
import socket


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


if __name__ == "__main__":
    # args = get_args()
    port = 80
    hostname = "127.0.0.1"
    host = f"{hostname}:{port}"
    zk = KazooClient(hosts=host, connection_retry=KazooRetry(20),)
    zk.start()
    party = Party(zk, "/celery/workers", identifier=1)
    print(zk.get_children("/celery/"))
    # for member in party:
    #     print(member)
    zk.stop()
