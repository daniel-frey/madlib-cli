from file_io import read_file, write_file
from textwrap import dedent
import re
import sys


def welcome_user():
    """Greet the user upon application start."""
    ln_1 = 'Welcome to madlibs, Python Edition!!!'
    ln_2 = 'To start, enter the name of a madlib file.'
    ln_3 = 'You will receive a series of prompts. Follow the directions and'
    ln_4 = 'not only will your madlib be complete, the file will be saved also'
    ln_5 = 'To exit at any time, type "quit". Why would you want to do that?'

    print(dedent(f'''
    {'*' * 70}

    {'{:^70}'.format(ln_1)}

    {'{:^70}'.format(ln_2)}
    {'{:^70}'.format(ln_3)}
    {'{:^70}'.format(ln_4)}

    {'{:^70}'.format(ln_5)}

    {'*' * 70}
    '''))


def read_madlib():
    """
    Take the user's input, and read the file.

    This will return a success / error message.

    There is no input required, the output will be a list,
    or an error message.
    """
    filename = input('Please choose a file: ')
    try:
        content = read_file(filename)
        if '{' in content:
            return [True, content]

        return [False, 'Incorrect file type was chosen.']
    except FileNotFoundError:
        return [False, 'Your file was not found']
    except IOError:
        return [False, 'There was an error reading this file']
    except Exception:
        return [False, 'Something else went wrong.']


def run_madlibs(madlibs_template):
    """
    Take a madlib file and use it as a template.

    input: list:
        bool, fail/pass of read
        string, madlibs template
    output: list:
        string, filled madlibs template
        list: madlibs words to prompt to the user
    """
    if madlibs_template[0] is False:
        print(madlibs_template[1])
    else:
        words = re.findall(r'\{.*?\}', madlibs_template[1])
        madlibs_template[1] = re.sub(r'\{.*?\}', '{}', madlibs_template[1])

        for i in range(len(words)):
            words[i] = words[i].strip('{}')

        user_words = prompt_the_user(words)

        print(len(tuple(user_words)))
        madlibs_template[1] = madlibs_template[1].format(*tuple(user_words))

        return madlibs_template


def prompt_the_user(words):
    """
    Take in a list of words and use string formatting on them.

    The input is the list of words (adjective, noun, etc)
    The output is the list of words that the user has entered.
    """
    print('The madlib is starting.')
    words_out = []

    for i in range(len(words)):
        user_input = input(words[i] + ': ')
        if user_input == 'exit':
            exit()

        words_out.append(user_input)

    return words_out


def user_output(madlib_output):
    """
    Take in the madlib template, prompts the user.

    This will ask if they would like to save. If the user chooses
    to do so, then they will be prompted for a filename.
    The application will then write to a file.
    """
    if madlib_output[0] is True:
        print('Your madlib:\n\n')
        print(madlib_output[1])
        user_input = input('Type "y" to save: ').lower()

        if user_input == 'exit':
            exit()
        if user_input == 'y':
            user_filename = input('Enter your filename: ')
            print(write_file(madlib_output[1], user_filename))

    else:
        print('There was a problem, please try again')


def exit():
    """Print a simple exit message, allows for exit."""
    print('Leaving so soon?')
    sys.exit()


def run():
    """Run the application."""
    welcome_user()
    while True:
        unformatted_madlibs = read_madlib()
        filled_madlibs = run_madlibs(unformatted_madlibs)
        user_output(filled_madlibs)
        user_input = input('Would you like to play again? y/n ')
        if user_input.lower() == 'y':
            continue

        exit()


if __name__ == "__main__":
    run()
