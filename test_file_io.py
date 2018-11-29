from .file_io import read_file, write_file
import pytest


def test_read_file():
    """Testing read_file for successful file read."""
    filename = 'sample'
    assert read_file(filename) == 'testfile\n'


def test_read_no_file():
    """Test read_file for file that does not exist."""
    filename = 'nothere'
    with pytest.raises(FileNotFoundError):
        read_file(filename)


def test_read_type_error():
    """Test read_file for incorrect input type."""
    filename = {}
    with pytest.raises(TypeError):
        read_file(filename)


def test_write_file():
    """Testing write_file for successful write."""
    filename = 'testfile'
    content = 'test!'

    write_file(content, filename)
    assert read_file(filename) == 'test!'


def test_incorrect_input():
    """Testing write_file for the wrong input type."""
    content = 'nope'
    filename = {}

    with pytest.raises(TypeError):
        write_file(content, filename)

    content = {}
    filename = 'nope'

    with pytest.raises(TypeError):
        write_file(content, filename)