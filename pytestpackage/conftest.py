# Configuration Test -> common pytest method
import pytest

@pytest.fixture()
def set_up(): # method level setup (default scope)
    print("\n---------- Run before method (conftest.py) ----------")  # before method
    yield
    print("\nRun after method (conftest.py)")  # after method


# scope -> "module" (default), "class", "session" ... # module setup (i.e: Open browser > Quit browser)
@pytest.fixture(scope="class")
def onetime_setup(browser, os_type):
    print("\n========== Run one time setup (conftest.py) ==========")  # before method
    if browser.lower() == "firefox":
        print(">>> Browser = Firefox")
    else:
        print(">>> Browser = Chrome")
    yield
    print("\n========== Run one time teardown (conftest.py) ==========")  # after method


# ==================================================================
# actual usage
# --envi qa1 --browser chrome --report True --headless False
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--os_type", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--os_type")


