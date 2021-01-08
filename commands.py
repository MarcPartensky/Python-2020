#!/usr/bin/env python
import sys
import os
import yaml

from rich import print

if not 'commands.yml' in os.listdir():
    print(f"File [bold]commands.yml[/bold] not found in \
          [bold]{os.getcwd()}[/bold]!")
    quit()

if len(sys.argv)==1:
    print("[bold]No command[\bold] given as input.")
    quit()

with open('commands.yml') as f:
    commands = yaml.load(f, Loader=yaml.FullLoader)

command = sys.argv[1]
if not command in commands:
    print(f"Command [bold]{command}[\bold] does not exist.")
    quit()

code = commands[command]
os.system(code)
