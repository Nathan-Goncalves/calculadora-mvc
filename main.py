from controller.calculator_controller import CalculatorController
from view.calculator_view import CalculatorView

def main():
    view = CalculatorView()
    controller = CalculatorController()

    while True:
        try:
            a, b, operation = view.get_input()
            result = controller.handle_operation(a, b, operation)
            view.display_result(result)
        except Exception as e:
            view.display_error(str(e))

        continue_calculation = input("Deseja continuar? (s/n): ").lower()
        if continue_calculation != 's':
            break

if __name__ == "__main__":
    main()