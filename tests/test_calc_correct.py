import pytest
from app.calculator import Calculator
# импортируем из файла "calculator.py" из папки "app"

class TestCalc: # Название класса тестов
    def setup(self):    # Предварительный метод "setup" в котором мы подключаем тестируемый объект
        self.calc = Calculator

    def test_multiply_calculate_correctly(self): # Тест на проверку правильности умножения
        assert self.calc.multiply(self, 2, 2) == 4

    def test_divisio_calculate_correctly(self): # Тест на проверку правильности деления
        assert self.calc.divisio(self, 5, 2) == 3

    def test_subtraction_calculate_correctly(self): # Тест на проверку правильности умножения
        assert self.calc.subtraction(self, 7, 2) == 5

    def test_adding_calculate_correctly(self): # Тест на проверку правильности умножения
        assert self.calc.adding(self, 4, 2) == 6