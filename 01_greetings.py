# This was like the first two couple of tutorial...
# A Hello world, and then some methods.
# PyCharm does a nice job of being bossy around naming conventions
# and spacing. Two newlines after a method. Cool.
# Seems like the main thing isn't really necessary
# But I'm assuming it prevents screwing up the execution order if this thing is
# Loaded as a module.

def main():
    print('Hello, World!')
    secondary_function()


def secondary_function():
    print('This line is printed from a secondary function call within the main function')

    # some test cases for the square function
    print(square(2))  # Prints 4
    print(square(5))  # Prints 25
    print(square(8))  # prints 64
    print(square(10))  # prints 100


# this function takes
# one argument, num and
# returns num squared
def square(num):
    num_squared = num * num
    return num_squared


if __name__ == '__main__':
    main()
