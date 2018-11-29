def read_file(filename):
    """
    Read a file and returns the output.

    The input consists of the file that you would like to be open.
    The output will be the contents of said file.
    """
    if type(filename) is not str:
        raise TypeError('the file must be a string, aka text.')

    with open('./' + filename + '.txt') as f:
        return f.read()

    try:
        with open(filename + '.txt') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError('The specified file was not found.')
    except IOError:
        raise IOError('Your file could not be read')


def write_file(content, filename):
    """
    Write a new text file.

    The input is two fold. The content, which is what you would
    like written into the file, and the filename, which is just as
    it says. The name of the resulting output.
    """
    if type(content) is not str or type(filename) is not str:
        raise TypeError('Please enter valid text and a filename.')

    try:
        with open('./' + filename + '.txt', 'w') as f:
            f.write(content)
            return ('Your file has been created')
    except IOError:
        return('Something went wrong, please try again.')


if __name__ == "__main__":
    print(read_file('sterile'))
