#!/usr/bin/env python3

#write a python program that when given the start point in a directory
#structure, locates all C/C++ files via assuming file extensions for C/C++
#files are .C, .c, .H, .h, or .A.  For each C/C++ file located, add the base
#name of the file to a specified Berkeley database as the key, and the path
#from the start point to the file (including the file name) as the value. For
#example, call this program with "fileDatabase /home/src/game gamefiles.db"

# Add a -h (--help also) option to the last modify_header.py and
# add_to_database.py, and also display that help if incorrect parameters are
# specified

import argparse
import os
import bsddb

def add_to_database(database_filename, start_path):
    # Open the Berkeley database
    db = bsddb.hashopen(database_filename, 'c')

    # Walk the directory tree
    for dirpath, dirnames, filenames in os.walk(start_path):
        # Check each file for a C/C++ extension
        for filename in filenames:
            if filename.endswith('.c') or filename.endswith('.C') or \
               filename.endswith('.h') or filename.endswith('.H') or \
               filename.endswith('.A'):                             # JDH modify
                # Add the file to the database with its base name as the key
                key = os.path.basename(filename)
                value = os.path.join(dirpath, filename)
                db[key] = value

    # Close the database
    db.close()

def main():
    parser = argparse.ArgumentParser(description='Add C/C++ files to a Berkeley database')
    parser.add_argument('database', help='Berkeley database file to use')
    parser.add_argument('start_path', help='Starting directory to scan for files')
    args = parser.parse_args()

    if args.database == '-h' or args.start_path == '-h' or args.database == '--help' or args.start_path == '--help':
        parser.print_help()
    else:
        add_to_database(args.database, args.start_path)

if __name__ == '__main__':
    main()

# To use this program, you can save the above code to a file named
# add_to_database.py, and run it from the command line with the following
# command:

# python add_to_database.py <database_path> <directory_path>

# Where <database_path> is the path to the Berkeley database file, and
# <directory_path> is the directory to search for C/C++ files. The program
# will search for files with the extensions .c, .h, or .a, and add their base
# names as keys and paths as values to the database.
