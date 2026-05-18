# load input file
# extract function names
# concat function names with | separator
# the concatenated list of function names is used in the grammar file /syntaxes/vex.tmLanguage.json

import os
import re

filepath = "temp/functions.txt"
file =  open(filepath)

functions = []

with open(filepath) as f:
    for line in file:
        index = line.find("(")
        if index != -1:
            name = line[0:line.find('(')]
            # print(name)
            functions.append(name)

functions = set(functions)

functions_joined = []

for name in functions:
    name = "".join([name, "|"])
    # print(name)
    functions_joined.append(name)

# concat into long string

full_string = ""

for name in functions_joined:
    # print(name)
    full_string = "".join([full_string, name])

print(full_string)

with open ('function_names_regex.txt', 'w') as f:
    f.write(full_string)
