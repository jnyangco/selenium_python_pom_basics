import pytest

@pytest.fixture()
def set_up():
    print("\n---------- Run before method (demo3) ----------")
    yield
    print("\nRun after method (demo3)")


def test_method_a(set_up):
    print(">>> Running method A (demo3)")


def test_method_b(set_up):
    print(">>> Running Method B (demo3)")


