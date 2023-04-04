def main():
    # a bunch of input stuff
    name = input('What is your name?')  # input is chill
    print('Hi there,', name, '...')  # padding spaces are free..
    print(f'Well, Hello, {name.upper()}!')  # this is a bit funky with the f operating on the string
    print('Cool you came, {}?'.format(name))  # string literals be objects maybe?

    bot_name = 'ShatGPT'  # ISO wants no uppercase in functions. No botName, unlike codeacademy tellin me
    bot_age = 0  # this no semicolons is hard habit to break
    print('Thanks for asking, I\'m', bot_name, 'and I\'m', bot_age, 'years old.')  # i guess backslashes escape. Cool.


if __name__ == '__main__':  # parens are optional here
    main()


