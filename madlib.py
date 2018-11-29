from file_io import read_file, write_file
from textwrap import dedent
import sys


def welcome_user():
    """
    Greet the user upon application start.

    No input/output
    """
    ln_1 = 'Welcome to madlibs, Python Edition!!!'
    ln_2 = 'To start, enter the name of a madlib file.'
    ln_3 = 'You will receive a series of prompts. Follow the directions and'
    ln_4 = 'not only will your madlib be complete, the file will be saved also'
    ln_5 = 'To exit at any time, type "quit". Why would you want to do that?'

    print(dedent(f'''
    {'*' * 60}

    {'{:^60}'.format(ln_1)}

    {'{:^60}'.format(ln_2)}
    {'{:^60}'.format(ln_3)}
    {'{:^60}'.format(ln_4)}

    {'{:^60}'.format(ln_5)}

    {'*' * 60}
    '''))


def read_madlib_file():
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


def run_madlibs_template(madlibs_template):
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
        print('Here is your madlib!')


def prompt_the_user(words):
    """
    Take in a list of words and use string formatting on them.

    The input is the list of words (adjective, noun, etc)
    The output is the list of words that the user has entered.
    """
    pass


def user_output():
    """
    Take in the madlib template, prompts the user.

    This will ask if they would like to save. If the user chooses
    to do so, then they will be prompted for a filename.
    The application will then write to a file.
    """
    pass


def exit():
    """Print a simple exit message, allows for exit."""
    print('Leaving so soon?')
    sys.exit()


def run():
    """Run the application."""
    welcome_user()
    while True:
        unformatted_madlibs = read_madlib_file()
        run_madlibs_template(unformatted_madlibs)


if __name__ == "__main__":
    run()
