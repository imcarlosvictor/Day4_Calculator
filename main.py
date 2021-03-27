def add(num1: int, num2: int) -> int:
    """Adds two integers and prints the equation and result."""

    total = num1 + num2
    print(f'{num1} + {num2} = {total}')


def subtract(num1: int, num2: int) -> int:
    """Subtracts two integers and prints the equation and result."""

    total = num1 - num2
    print(f'{num1} - {num2} = {total}')


def multiply(num1: int, num2: int) -> int:
    """Multiplies two integers and prints the equation and result."""
    total = num1 * num2
    print(f'{num1} * {num2} = {total}')


def divide(num1: int, num2: int) -> int:
    """Divides two integers and prints the equation and result."""
    total = num1 / num2
    print(f'{num1} / {num2} = {total}')


def main():

    calc_running = True
    while calc_running:

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

        # Prompts and validates if input is a number
        validate_num = True
        while validate_num:

            num1_input = 0

            try:
                num1_input: int = int(input('Number >>> '))
            except ValueError:
                print('Value is not a number.')
                continue

            if num1_input in numbers:
                break

        # Prompts and validates if input is an operator
        validate_operator = True
        while validate_operator:
            operators = ['+', '-', '*', '/']

            operator_input: str = input('Operator >>> ')

            if operator_input not in operators:
                print('Enter a valid operator.')
            else:
                break

        # Prompts and validates if input is a number
        validate_num = True
        while validate_num:

            num2_input = 0

            try:
                num2_input: int = int(input('Number >>> '))
            except ValueError:
                print('Value is not a number.')
                continue

            if num2_input in numbers:
                break

        # Check the operator and call the proper function
        if operator_input == '+':
            add(num1_input, num2_input)
        elif operator_input == '-':
            subtract(num1_input, num2_input)
        elif operator_input == '*':
            multiply(num1_input, num2_input)
        elif operator_input == '/':
            divide(num1_input, num2_input)

        # Place holder to try_again result
        calc_run = True

        # Ask user to go again
        try_again = True
        while try_again:
            user_continue = input('Again? (y/n): ')

            if user_continue == 'n':
                calc_run = False
                break
            elif user_continue == 'y':
                print('\nStarting...\n')
                break
            else:
                print("Enter 'y' or 'n'")

        # Exit if necessary
        if not calc_run:
            print('Ending...\n')
            break


if __name__ == '__main__':
    main()
