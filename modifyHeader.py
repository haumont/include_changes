#!/usr/bin/env python3

# write me a python program to add a path to all includes in an inputted C or
# C++ language file.  For example, given a header file named header.h, with
# contents of only '#include "second.h" ' , and a program invocation of
# modifyHeader header.h base/header, the contents of header.h would be
# transformed to say ' #include "base/header/second.h" '   Note that most
# input files will be more complex

import os
import sys
import re

def modify_header_file(file_path, header_path):
    # Read in the contents of the input file
    with open(file_path, 'r') as file:
        contents = file.read()

    # Find all #include statements in the file and modify them
    modified_contents = re.sub(r'#include\s+["<](\S+?)["/]', r'#include "' + header_path + r'/\1"', contents)

    # Write out the modified contents to the same file
    with open(file_path, 'w') as file:
        file.write(modified_contents)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: modifyHeader <input_file> <header_path>')
        sys.exit(1)

    file_path = sys.argv[1]
    header_path = sys.argv[2]

    modify_header_file(file_path, header_path)


# To use this program, you can invoke it from the command line with the input
# file path and the header path prefix as arguments. For example, if the
# above code is saved to a file named modifyHeader.py, you could run the
# program with the following command:

# python modifyHeader.py header.h base/header

# This would modify the header.h file to include the base/header prefix before
# any included files.

