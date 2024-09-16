import pytest
from pytestpackage.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("onetime_setup", "set_up")
class TestClassDemoHTMLReport:

    @pytest.fixture(autouse=True)
    def class_setup(self, onetime_setup):
        self.class_result = SomeClassToTest(self.value)


    def test_method_a(self):
        actual_result = self.class_result.sum_numbers(2, 8)
        expected_result = 10
        print(f'result = {actual_result}')
        assert actual_result == expected_result
        print(">>> Running method A (demo3)")


    def test_method_b(self):
        actual_result = self.class_result.sum_numbers(2, 8)
        expected_result = 10
        print(f'result = {actual_result}')
        assert actual_result > expected_result
        print(">>> Running Method B (demo3)")
