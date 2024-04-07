import controller
import calculator
import logging

logging.basicConfig(level=logging.DEBUG, filename='./logs/main-log.txt',filemode='a+')

if __name__ == '__main__':
    logging.debug('__name__ == "__main__"')

    logging.debug('calc = class Calculator')
    calc = calculator.Calculator()
    logging.debug('calc made')

    logging.debug('ctrl = class Contoller')
    ctrl = controller.Controller(calc)
    logging.debug('ctrl made')

    logging.debug('Starting endless loop')
    while True:
        logging.debug('num1 = float type input')
        num1 = float(input('Введите 1-е число: '))

        logging.debug('action = string type input')
        action = input('Введите знак (+ - * /): ')

        logging.debug('num2 = float type input')
        num2 = float(input('Введите 2-е число: '))

        logging.info(f'num1={num1}; num2={num2}; action={action}')

        logging.info('Printing result from Controller count function')
        print(ctrl.count(num1, action, num2))

        logging.debug('Asking for quit the program')
        if input('Выйти из калькулятора? (y/n): ').upper() == 'Y':
            logging.info('Quitting')
            break
        else:
            logging.debug('Quit cancelled')