#!/usr/bin/python3
"""
It prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    A function that prints a text with 2 lines after  .?:

    Args: the text
        raise a error if text is not string

    Return: the text and other special character assigned
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        result = []
        a = 0
        text_len = len(text)
        skip_spaces = True
        is_end = False
        is_delim = False
        for i in range(text_len):
            is_end = i == text_len - 1
            is_delim = text[i] in '.?:'
            if is_delim or is_end:
                result.append(text[a: i + 1] + ('\n\n' * is_delim))
                skip_spaces = True
                a = i + 1
            elif text[i] in ' \t\r\v' and skip_spaces:
                a += 1
            elif text[i] == '\n':
                result.append(text[a: i + 1].rstrip() + '\n')
                a += 1
                skip_spaces = True
            else:
                if skip_spaces:
                    a = i
                skip_spaces = False
        print(''.join(result), end='')
