import pytest

@pytest.fixture()
def set_up():
    print("\n---------- Run before method (demo2) ----------")
    yield
    print("\nRun after method (demo2)")


def test_method_a(set_up):
    print(">>> Running method A (demo2)")


def test_method_b(set_up):
    print(">>> Running Method B (demo2)")


