#import pytest

from app.calculator import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator()

    def test_multiply_success(self):
        assert self.calc.multiply(-2, 50) == -100

    def test_division_success(self):
        assert self.calc.division(86, 5) == 17.2

    def test_substraction_success(self):
        assert self.calc.subtraction(890000000000, 10) == 889999999990

    def test_adding_success(self):
        assert self.calc.adding(100, 23) == 123

    def teardown_method(self):
        print("Выполнение метода Teardown")