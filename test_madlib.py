# from madlib import read_madlib, run_madlibs
# import pytest


# def test_read_madlib_file():
#     """Test madlib file read."""
#     actual_filename = 'madlib_test'
#     expected_output = 'The dog {Verb}\n'

#     assert read_madlib(actual_filename)[1] == expected_output


# def test_incorrect_madlib_file():
#     """Test a file that doesn't belong to a madlib."""
#     actual_filename = 'incorrect_file'
#     expected_output = 'This is not the correct file format.'

#     assert read_madlib(actual_filename)[1] == expected_output


# def test_madlib_file_not_found():
#     """Test for file not found."""
#     actual_filename = 'nothere'
#     expected_output = 'The specificed file does not exist.'

#     assert read_madlib(actual_filename)[1] == expected_output
