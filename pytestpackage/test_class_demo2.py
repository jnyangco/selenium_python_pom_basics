import pytest
from pytestpackage.class_to_test import SomeClassToTest

# This will replace "test_class_demo2.py"

# Wrap up all tests into one class (TestClassDemo)
# New way use fixtures
# Use 'autouse' (not needed to add on each test methods)

# use fixture on all methods under this class
# instead of adding it to module level (i.e: test_method_a(self, onetime_setup, setup)
#                                            test_method_a(self, onetime_setup, setup)
@pytest.mark.usefixtures("onetime_setup", "set_up")
class TestClassDemo:

    # pre-requisite: class level only
    # add this fixture 'autouse' to class_setup for the test methods below can read/access "self" variable
                        # instead of adding it to module level (i.e: test_method_a(self, class_setup)
                        #                                      (i.e: test_method_b(self, class_setup)
    @pytest.fixture(autouse=True)
    def class_setup(self, onetime_setup): # need to put here "onetime_setup" to access return value
        self.class_result = SomeClassToTest(self.value) # instance of a class (with Constructor value - optional)
                                                        # self.value -> returned from conftest.py (return value / yield value)


    def test_method_a(self):
        actual_result = self.class_result.sum_numbers(2, 8)
        expected_result = 10
        print(f'result = {actual_result}')
        assert actual_result == expected_result
        print(">>> Running method A (demo2)")


    def test_method_b(self):
        print(">>> Running Method B (demo2)")
