import calculator
import logging

logging.basicConfig(level=logging.DEBUG, filename='./logs/controller-log.txt',filemode='a+')

class Controller:
    def __init__(self, calculator: calculator.Calculator):
        logging.debug('Initiliazing class Contoller')
        logging.info(f'Argument "calculator" is {calculator}')
        self.calculator = calculator
        logging.debug('self.calculator is argument "calculator"')

    def count(self, num0: int | float, action: str, num1: int | float) -> int | float:
        logging.debug('Running function "add" in class Controller')
        logging.info(f'Argument num0={num0}; num1={num1}, action={action}')

        if action == '+':
            logging.info('Action is +, returning result from function "add" from self.calculator')
            return self.calculator.add(num0, num1)
        elif action == '-':
            logging.info('Action is -, returning result from function "subtract" from self.calculator')
            return self.calculator.subtract(num0, num1)
        elif action == '*':
            logging.info('Action is *, returning result from function "multiply" from self.calculator')
            return self.calculator.multiply(num0, num1)
        elif action == '/':
            logging.info('Action is /, returning result from function "divide" from self.calculator')
            return self.calculator.divide(num0, num1)
        else:
            logging.error('Unkdown action, raising ValueError')
            raise ValueError