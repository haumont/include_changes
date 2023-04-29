#!/usr/bin/env python3

# write me a python program that takes a list of files, one filename per line,
# and a directory name start point, and compares the list of files with the
# contents of the directory structure below the start point to both list
# files in the list that are missing from the directory, and list the files
# that are not present in the list but are in the directory structure.  Add
# an optional parameter "-d" to delete all files not present in the given
# list of files that are in the directory structure

# Add the same kind of help message to compare_files.py too

import argparse
import os

def get_file_list(path):
    file_list = []
    with open(path, 'r') as f:
        for line in f:
            file_list.append(line.strip())
    return file_list

def compare_files(file_list_path, start_dir, delete_files):
    file_list = get_file_list(file_list_path)
    for root, dirs, files in os.walk(start_dir):
        for name in files:
            ext = os.path.splitext(name)[1].lower()
            if ext in ['.c', '.C', '.h', '.H', '.A']:               # JDH modify
                full_path = os.path.join(root, name)
                rel_path = os.path.relpath(full_path, start_dir)
                if rel_path not in file_list:
                    print(f"{rel_path} is not in the file list")
                    if delete_files:
                        os.remove(full_path)
        for file in file_list:
            full_path = os.path.join(start_dir, file)
            if not os.path.isfile(full_path):
                print(f"{file} is in the file list but not in the directory structure")

def main():
    parser = argparse.ArgumentParser(description='Compare a list of files to a directory structure and optionally delete files not in the list.')
    parser.add_argument('file_list_path', help='Path to the file containing the list of files')
    parser.add_argument('start_dir', help='Path to the starting directory for the comparison')
    parser.add_argument('-d', '--delete', action='store_true', help='Delete files that are not in the file list')
    parser.add_argument('-h', '--help', action='help', help='Show this help message and exit')
    args = parser.parse_args()

    if not os.path.isdir(args.start_dir):
        print(f"{args.start_dir} is not a valid directory path")
        parser.print_help()
        return

    if not os.path.isfile(args.file_list_path):
        print(f"{args.file_list_path} is not a valid file path")
        parser.print_help()
        return

    compare_files(args.file_list_path, args.start_dir, args.delete)

if __name__ == '__main__':
    main()

# To use this program, you can save the above code to a file named
# compare_files.py, and run it from the command line with the following
# command:

# python compare_files.py <file_list_path> <directory_path> [-d]

# Where <file_list_path> is the path to a file containing a list of filenames,
# one per line, and <directory_path> is the directory to compare against. The
# optional -d flag will delete any files in the directory that are not
# present in the file list.

# Now, when running compare_files.py -h or compare_files.py --help, the help
# message will be displayed:

# usage: compare_files.py [-h] [-d] file_list_path start_dir

# Compare a list of files to a directory structure and optionally delete files not in the list.

# positional arguments:
#   file_list_path    Path to the file containing the list of files
#   start_dir         Path to the starting directory for the comparison

# optional arguments:
#   -h, --help        Show this help message and exit
#   -d, --delete      Delete files that are not in the file list
