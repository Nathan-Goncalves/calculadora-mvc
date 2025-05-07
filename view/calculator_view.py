class CalculatorView:
    def get_input(self):
        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            operation = input("Escolha a operação (+, -, *, /): ")
            return a, b, operation
        except ValueError:
            print("Entrada inválida. Use números válidos.")
            return self.get_input()

    def display_result(self, result):
        print(f"Resultado: {result}")

    def display_error(self, message):
        print(f"Erro: {message}")