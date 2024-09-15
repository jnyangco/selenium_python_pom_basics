# run default order -> based on code hierarchy (A, B, C, D, E, F) - not alphabetically
# pytest-ordring -> documentation (check if some functions can be used)
# https://pytest-ordering.readthedocs.io/en/develop

import pytest

# B, A, C, D, E, F
@pytest.mark.run(order=2)
def test_run_order_method_a(onetime_setup, set_up):
    print(">>> Running method A")

@pytest.mark.run(order=1)
def test_run_order_method_b(onetime_setup, set_up):
    print(">>> Running method B")

def test_run_order_method_c(onetime_setup, set_up):
    print(">>> Running method C")

def test_run_order_method_d(onetime_setup, set_up):
    print(">>> Running method D")

def test_run_order_method_e(onetime_setup, set_up):
    print(">>> Running method E")

def test_run_order_method_f(onetime_setup, set_up):
    print(">>> Running method F")

