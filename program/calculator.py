import number
import logging

logging.basicConfig(level=logging.DEBUG, filename='./logs/calculator-log.txt',filemode='a+')

class Calculator:
    def __init__(self):
        logging.debug('Initiliazing class Calculator')
        super().__init__()

    def add(self, num0: number.Number, num1: number.Number) -> int | float:

        logging.debug('Running function "add" in class Calculator')
        result = num0+num1
        logging.info(f'result = {result}')

        if result.is_integer():
            logging.debug('Result type is integer, returning integer')
            return int(result)
        else:
            logging.debug('Result type is float, returning float')
            return result

    def subtract(self, num0: number.Number, num1: number.Number) -> int | float:

        logging.debug('Running function "substract" in class Calculator')
        result = num0-num1
        logging.info(f'result = {result}')

        if result.is_integer():
            logging.debug('Result type is integer, returning integer')
            return int(result)
        else:
            logging.debug('Result type is float, returning float')
            return result

    def multiply(self, num0: number.Number, num1: number.Number) -> int | float:

        logging.debug('Running function "multiply" in class Calculator')
        result = num0*num1
        logging.info(f'result = {result}')

        if result.is_integer():
            logging.debug('Result type is integer, returning integer')
            return int(result)
        else:
            logging.debug('Result type is float, returning float')
            return result

    def divide(self, num0: number.Number, num1: number.Number) -> int | float:

        logging.debug('Running function "divide" in class Calculator')

        if num1 != 0:
            logging.debug('Second number !=0, counting')
            result = num0*num1
            logging.info(f'result = {result}')

            if result.is_integer():
                logging.debug('Result type is integer, returning integer')
                return int(result)
            else:
                logging.debug('Result type is float, returning float')
                return result
        else:
            logging.error('Second number is 0, raising ZeroDivisionError')
            raise ZeroDivisionError