import pytest

@pytest.fixture()
def set_up():
    print("\n---------- Run before method (demo1) ----------")


def test_method_a(set_up):
    print(">>> Running method A (demo1)")


def test_method_b(set_up):
    print(">>> Running Method B (demo1)")


