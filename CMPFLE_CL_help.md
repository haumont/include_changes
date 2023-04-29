Sure, here are the steps to compile and run the CL program on OS/400:

1. Create a source member in a source physical file (for example, `MYLIB/QCLSRC`) with the CL code.
2. Compile the source member using the `CRTCLPGM` command. For example, if the source member is named `COMPARE_FILES`, you would use the following command:

   ```
   CRTCLPGM PGM(MYLIB/COMPARE_FILES) SRCFILE(MYLIB/QCLSRC) SRCMBR(COMPARE_FILES)
   ```

   This will create a program object named `COMPARE_FILES` in the `MYLIB` library.
3. Create a data file with a list of the files to compare. For example, you could create a physical file named `FILELIST` with the following fields:

   ```
   Field      Type    Length  Description
   FILENAME   Char    10      Name of the file to compare
   ```

   Then, add one record for each file you want to compare.
4. Run the program by calling it from a command line. For example, you could use the following command:

   ```
   CALL MYLIB/COMPARE_FILES
   ```

   This will execute the program and compare each file listed in the `FILELIST` file.

Note that you may need to adjust the library and file names in the CL code to match your environment. Also, you may need to grant appropriate authorities to the program object and data files before running the program.
