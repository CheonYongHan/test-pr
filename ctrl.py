class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self):
        num1 = float(self.view.le1.text())  # get first number
        num2 = float(self.view.le2.text())  # get second number
        operator = self.view.cb.currentText()   # get operator

        if operator == '+':
            return f'{num1} + {num2} = {self.sum(num1, num2)}'
        elif operator == '-':
            return f'{num1} - {num2} = {self.sub(num1, num2)}'
        elif operator == '*':
            return f'{num1} * {num2} = {self.mul(num1, num2)}'
        elif operator == '/':
            return f'{num1} / {num2} = {self.div(num1, num2)}'
        else:
            return 'Invalid Operator'

    def connectSignals(self):
        self.view.btn1.clicked.connect(lambda:\
                                        self.view.setDisplay(self.calculate()))  # connect button to calculate method
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):    # 뺄셈함수 추가
        return a - b

    def mul(self, a, b):    # 곱셈함수 추가
        return a * b

    def div(self, a, b):    # 나눗셈함수 추가
        try:
            if b == 0:
                raise Exception('Divisor Error')
        except Exception as e:
            return e    

        return a / b



