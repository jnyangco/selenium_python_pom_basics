import pytest
from pytestpackage.class_to_test import SomeClassToTest

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
    def class_setup(self):
        self.class_result = SomeClassToTest() # instance of a class (with Constructor value - optional)


    def test_method_a(self):
        result = self.class_result.sum_numbers(2, 8)
        print(f'result = {result}')
        assert result == 10
        print(">>> Running method A (demo1)")


    def test_method_b(self):
        print(">>> Running Method B (demo1)")
