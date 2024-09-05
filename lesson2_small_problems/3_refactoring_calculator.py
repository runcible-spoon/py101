import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"=>{message}")

prompt(MESSAGES["lang_select"])
language = input()

while language not in ['EN', 'ES', 'FR', 'DE']:
    prompt(MESSAGES["lang_select"])
    language = input()

intl_message = MESSAGES[language]


prompt(intl_message["welcome"])

while True:
    prompt(intl_message["ask"]["number"][0])
    number1 = input()

    def invalid_number(number_str):
        try:
            float(number_str)
        except ValueError:
            return True

        return False


    while invalid_number(number1):
        prompt(intl_message["scold"]["wrong_number"])
        number1 = input()

    prompt(intl_message["ask"]["number"][1])
    number2 = input()


    while invalid_number(number2):
        prompt(intl_message["scold"]["wrong_number"])
        number2 = input()

    prompt(f'{number1} {number2}')
    prompt(intl_message["ask"]["operation"])
    operation = input()


    while operation not in ['1', '2', '3', '4']:
        prompt(intl_message["scold"]["wrong_operation"])
        operation = input()


    # Perform the operation on the two numbers.
    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)

    # print the result to the terminal.
    prompt(intl_message["result"])
    prompt(output)    

    prompt(intl_message["ask"]["repeat"])
    continue_choice = input()

    while continue_choice not in [intl_message["letter"][0], intl_message["letter"][1]]:
        prompt(intl_message["scold"]["wrong_continue"])
        continue_choice = input()
    
    if continue_choice == intl_message["letter"][0]:
            prompt(intl_message["confirmation"]["yes"])
            continue
    if continue_choice == intl_message["letter"][1]:
            prompt(intl_message["confirmation"]["no"])
            break
