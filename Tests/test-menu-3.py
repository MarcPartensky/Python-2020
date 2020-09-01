#!/usr/bin/env python3

import os
from pygments import formatters, highlight, lexers
from pygments.util import ClassNotFound
from simple_term_menu import TerminalMenu


def highlight_file(filepath):
    with open(filepath, "r") as f:
        file_content = f.read()
    try:
        lexer = lexers.get_lexer_for_filename(filepath, stripnl=False, stripall=False)
    except ClassNotFound:
        lexer = lexers.get_lexer_by_name("text", stripnl=False, stripall=False)
    formatter = formatters.TerminalFormatter(bg="dark")  # dark or light
    highlighted_file_content = highlight(file_content, lexer, formatter)
    return highlighted_file_content


def list_files(directory="."):
    return (file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file)))


def main():
    terminal_menu = TerminalMenu(list_files(), preview_command=highlight_file, preview_size=0.75)
    terminal_menu.show()


if __name__ == "__main__":
    main()
