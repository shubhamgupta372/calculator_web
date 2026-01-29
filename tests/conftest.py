import pytest

def pytest_addoption(parser):
    """Add command-line option to show browser"""
    parser.addoption(
        "--show-browser",
        action="store_true",
        default=False,
        help="Run tests with visible browser window"
    )

def pytest_configure(config):
    """Store config for use in fixtures"""
    config.getoption("--show-browser")
