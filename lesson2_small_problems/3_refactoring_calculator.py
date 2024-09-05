import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"=>{message}")

prompt(MESSAGES["welcome"])

while True:
    prompt(MESSAGES["asks"]["numbers"][0])
    number1 = input()

    def invalid_number(number_str):
        try:
            int(number_str)
        except ValueError:
            return True

        return False


    while invalid_number(number1):
        prompt(MESSAGES["scolds"]["wrong_number"])
        number1 = input()

    prompt(MESSAGES["asks"]["numbers"][1])
    number2 = input()


    while invalid_number(number2):
        prompt(MESSAGES["scolds"]["wrong_number"])
        number2 = input()

    prompt(f'{number1} {number2}')
    prompt(MESSAGES["asks"]["operations"])
    operation = input()


    while operation not in ['1', '2', '3', '4']:
        prompt(MESSAGES["scolds"]["wrong_operation"])
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
    prompt(f'The result is: {output}')
    

    prompt(MESSAGES["asks"]["repeat"])
    continue_choice = input()

    while continue_choice not in ['Y', 'N']:
        prompt(MESSAGES["scolds"]["wrong_continue"])
        continue_choice = input()
    
    match continue_choice:
        case 'Y':
            prompt(MESSAGES["confirmations"]["yes"])
            continue
        case 'N':
            prompt(MESSAGES["confirmations"]["no"])
            break
