application_title = "test1.0" 
main_python_file = "test.py"

import sys

from cx_Freeze import setup, Executable

base = None

includes = []

setup(
        name = application_title,
        version = "1.0",
        description = "freezed test",
        options = {"build_exe" : {"includes" : includes }},
        executables = [Executable(main_python_file, base = base)])
