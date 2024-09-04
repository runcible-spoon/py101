def prompt(message):
    print(f"=>{message}")

prompt('Welcome to Calculator!')

while True:
    prompt("What's the first number?")
    number1 = input()

    def invalid_number(number_str):
        try:
            int(number_str)
        except ValueError:
            return True

        return False


    while invalid_number(number1):
        prompt("Hmm.. That doesn't look like a valid number.")
        number1 = input()

    prompt("What's the second number?")
    number2 = input()


    while invalid_number(number2):
        prompt("Hmm.. That doesn't look like a valid number.")
        number2 = input()

    prompt(f'{number1} {number2}')
    prompt('''What operation would you like to perform?\n
        1) Add 2) Subtract 3) Multiple 4) Divide''')
    operation = input()


    while operation not in ['1', '2', '3', '4']:
        prompt("You must enter 1, 2, 3, or 4.")
        operation = input()


    # Perform the operation on the two numbers.
    match operation:
        case '1':
            output = int(number1) + int(number2)
        case '2':
            output = int(number1) - int(number2)
        case '3':
            output = int(number1) * int(number2)
        case '4':
            output = int(number1) / int(number2)

    # print the result to the terminal.
    prompt(f"The result is: {output}")
    

    prompt('Perform another operation? Y / N')
    continue_choice = input()

    while continue_choice not in ['Y', 'N']:
        prompt("You must enter 'Y' or 'N'.")
        continue_choice = input()
    
    match continue_choice:
        case 'Y':
            prompt("Once more into the breach.")
            continue
        case 'N':
            prompt("Thanks for operating!")
            break
