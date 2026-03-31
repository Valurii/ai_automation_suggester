import os
import sys

from aiohttp.resolver import ThreadedResolver
import homeassistant.helpers.aiohttp_client as ha_aiohttp_client
import pytest

try:
    import homeassistant.helpers.backports.aiohttp_resolver as ha_aiohttp_resolver
except ModuleNotFoundError:
    ha_aiohttp_resolver = None


class TestThreadedResolver(ThreadedResolver):
    """Use a thread-based resolver to keep HA tests deterministic across platforms."""


ha_aiohttp_client.AsyncResolver = TestThreadedResolver
if ha_aiohttp_resolver is not None:
    ha_aiohttp_resolver.AsyncResolver = TestThreadedResolver


if sys.platform == "win32":
    import pytest_socket

    if not hasattr(os, "fchmod"):
        def _noop_fchmod(_fd: int, _mode: int) -> None:
            return None

        os.fchmod = _noop_fchmod


@pytest.hookimpl(trylast=True)
def pytest_runtest_setup() -> None:
    """Keep Windows event-loop setup working while still blocking outbound network."""
    if sys.platform != "win32":
        return

    pytest_socket.enable_socket()
    pytest_socket.socket_allow_hosts(["127.0.0.1", "localhost", "::1"])


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_fixture_setup(fixturedef):
    """Allow Windows asyncio to create its loopback self-pipe during event-loop setup."""
    if sys.platform == "win32" and fixturedef.argname == "event_loop":
        pytest_socket.enable_socket()
        pytest_socket.socket_allow_hosts(["127.0.0.1", "localhost", "::1"])

    yield
