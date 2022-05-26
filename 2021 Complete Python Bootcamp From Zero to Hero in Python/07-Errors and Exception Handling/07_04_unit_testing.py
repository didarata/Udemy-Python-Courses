# # Unit Testing
# # Equally important as writing good code is writing good tests. Better to find bugs yourself than have them reported to you by end users!
# #
# # For this section we'll be working with files outside the notebook. We'll save our code to a .py file, and then save our test script to another .py file.
# # Normally we would code these files using a text editor like Brackets or Atom, or inside an IDE like Spyder or Pycharm. But, since we're here, let's
# # use Jupyter!
# #
# # Recall that with some IPython magic we can write the contents of a cell to a file using %%writefile.
# # Something we haven't seen yet; you can run terminal commands from a jupyter cell using !
#
# # Testing tools
# # There are dozens of good testing libraries out there. Most are third-party packages that require an install, such as:
# #
# # pylint
# # pyflakes
# # pep8
# # These are simple tools that merely look at your code, and they'll tell you if there are style issues or simple problems like variable names being
# # called before assignment.
# #
# # A far better way to test your code is to write tests that send sample data to your program, and compare what's returned to a desired outcome.
# # Two such tools are available from the standard library:
# #
# # unittest
# # doctest
# # Let's look at pylint first, then we'll do some heavier lifting with unittest.
# #
# # pylint
# # pylint tests for style as well as some very basic program logic.
# #
# # First, if you don't have it already (and you probably do, as it's part of the Anaconda distribution), you should install pylint.
# # Once that's done feel free to comment out the cell, you won't need it anymore.
# import pylint as pylint
# import writefile as writefile
#
# pip install pylint
#
# %%writefile simple1.py
# a = 1
# b = 2
# print(a)
# print(B)
#
# pylint simple1.py
#
# # No config file found, using default configuration
# # Pylint first lists some styling issues - it would like to see an extra newline at the end, modules and function definitions should have descriptive
# # docstrings, and single characters are a poor choice for variable names.
# #
# # More importantly, however, pylint identified an error in the program - a variable called before assignment. This needs fixing.
# #
# # Note that pylint scored our program a negative 12.5 out of 10. Let's try to improve that!
#
# %%writefile simple1.py
# """
# A very simple script.
# """
#
# def myfunc():
#     """
#     An extremely simple function.
#     """
#     first = 1
#     second = 2
#     print(first)
#     print(second)
#
# myfunc()
#
# ! pylint simple1.py
#
# # No config file found, using default configuration
# # Much better! Our score climbed to 8.33 out of 10. Unfortunately, the final newline has to do with how jupyter writes to a file, and there's not much we
# # can do about that here. Still, pylint helped us troubleshoot some of our problems. But what if the problem was more complex?
#
# %%writefile simple2.py
# """
# A very simple script.
# """
#
# def myfunc():
#     """
#     An extremely simple function.
#     """
#     first = 1
#     second = 2
#     print(first)
#     print('second')
#
# myfunc()
#
# ! pylint simple2.py
#
# # No config file found, using default configuration
# # pylint tells us there's an unused variable in line 10, but it doesn't know that we might get an unexpected output from line 12!
# # For this we need a more robust set of tools. That's where unittest comes in.
#
# # unittest
# # unittest lets you write your own test programs. The goal is to send a specific set of data to your program, and analyze the returned
# # results against an expected result.
# #
# # Let's generate a simple script that capitalizes words in a given string. We'll call it cap.py.
#
# %%writefile cap.py
# def cap_text(text):
#     return text.capitalize()
#
# # Now we'll write a test script. We can call it whatever we want, but test_cap.py seems an obvious choice.
# #
# # When writing test functions, it's best to go from simple to complex, as each function will be run in order. Here we'll test simple, one-word strings,
# # followed by a test of multiple word strings.
#
# % % writefile
# test_cap.py
# import unittest
# import cap
#
#
# class TestCap(unittest.TestCase):
#
#     def test_one_word(self):
#         text = 'python'
#         result = cap.cap_text(text)
#         self.assertEqual(result, 'Python')
#
#     def test_multiple_words(self):
#         text = 'monty python'
#         result = cap.cap_text(text)
#         self.assertEqual(result, 'Monty Python')
#
#
# if __name__ == '__main__':
#     unittest.main()
#
#
# %%writefile cap.py
# def cap_text(text):
#     return text.title()  # replace .capitalize() with .title()
#
# % % writefile
# test_cap.py
# import unittest
# import cap
#
#
# class TestCap(unittest.TestCase):
#
#     def test_one_word(self):
#         text = 'python'
#         result = cap.cap_text(text)
#         self.assertEqual(result, 'Python')
#
#     def test_multiple_words(self):
#         text = 'monty python'
#         result = cap.cap_text(text)
#         self.assertEqual(result, 'Monty Python')
#
#     def test_with_apostrophes(self):
#         text = "monty python's flying circus"
#         result = cap.cap_text(text)
#         self.assertEqual(result, "Monty Python's Flying Circus")
#
#
# if __name__ == '__main__':
#     unittest.main()