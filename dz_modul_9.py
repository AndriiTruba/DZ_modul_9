
from typing import Callable, Dict


CONTACT_BOOK = {}


def input_error(func):
    def wraper(user_input):
        try:
            return func(user_input)
        except ValueError as e:
            return str(e)       
    return wraper


@input_error
def hello_handler(user_input: str):
    if user_input.strip() == 'hello':
        return 'How can I help you'
    raise ValueError('Bad input!')


@input_error
def add_handler(user_input: str):
    args = user_input.lstrip('add ')
    try:
        name, phone = args.split(' ')
    except ValueError:
        raise ValueError('Bad input! Give me name and phone please')
    if name == '' or phone == '':
        raise ValueError('Bad input! Give me name and phone please')
    if CONTACT_BOOK.get(name, None) == None:
        CONTACT_BOOK[name] = phone
        return 'Number was added!'
    raise ValueError(f'{name} alredy in contact book!')


@input_error
def change_handler(user_input: str):
    try:
        args = user_input.lstrip('change ')
        name, phone = args.split(' ')
    except ValueError:
        raise ValueError('Bad input! Give me name and phone please')
    if CONTACT_BOOK.get(name, None) == None:
        raise ValueError(f'{name} does not exists!')
    else:
        CONTACT_BOOK[name] = phone
        return 'Number was changed!'


@input_error
def phone_handler(user_input: str):
    username = user_input.lstrip('phone ')
    if username == '':
        raise ValueError("Bad input! Enter user name") 
    phone = CONTACT_BOOK.get(username, None)
    if phone != None:
        return f'{username} namber is {phone}'
    raise ValueError(f'{username} namber does not exists!')


@input_error
def show_all_handler(user_input: str):
    if user_input.strip() == 'show all':
        all_response = '\n'.join(f'{username} namber is {namber}' for (username, namber) in CONTACT_BOOK.items())
        return all_response
    raise ValueError('Bad input')


def exit_handler(user_input: str):
    for item in ['good bye', 'close', 'exit']:
        if user_input.strip() == item:
            raise SystemExit('Good bye!')
    


COMMAND_HANDLERS: Dict[str, Callable] = {
    'hello': hello_handler,
    'add': add_handler,
    'change': change_handler,
    'phone': phone_handler,
    'show all': show_all_handler,
    'good bye': exit_handler,
    'close': exit_handler,
    'exit': exit_handler
}


@input_error
def parse_user_input(user_input: str) -> set[str, str]:
    for command in COMMAND_HANDLERS.keys():  
        if user_input.startswith(command):
            parser = COMMAND_HANDLERS.get(command)
            return parser(user_input)
        else:
            continue
    raise ValueError('Unknown command')



def main():
        while True:
            user_input = input('Enter the command: ').lower()
            try:
                resalt = parse_user_input(user_input)
                print(resalt)
            except SystemExit as e:
                 print(e)
                 break


if __name__ == '__main__':
    main()

