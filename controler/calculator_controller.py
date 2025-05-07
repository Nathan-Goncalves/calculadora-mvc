from model.calculator_model import CalculatorModel

class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()

    def handle_operation(self, a, b, operation):
        try:
            if operation == '+':
                return self.model.add(a, b)
            elif operation == '-':
                return self.model.subtract(a, b)
            elif operation == '*':
                return self.model.multiply(a, b)
            elif operation == '/':
                return self.model.divide(a, b)
            else:
                raise ValueError("Operação inválida.")
        except Exception as e:
            raise e