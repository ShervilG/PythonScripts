import os
import time

i = 1
cmd_list = ["notepad","notepad"]
string = cmd_list[0] + ' | '
string = string * 50
string += "notepad"
os.system(string)
