#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    lines = []
    line = ""

    for char in text:
        line += char
        if char in separators:
            lines.append(line.strip())
            lines.append("")
            line = ""

    if line:
        lines.append(line.strip())

    print('\n'.join(lines))


text = "This is a sample text. has some sentences? And some colons: Like this."
text_indentation(text)
