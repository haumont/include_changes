Yes, you can use SQL to build the `FILELIST` file on OS/400. Here's an example SQL statement that you can use:

```
INSERT INTO MYLIB/FILELIST (FILENAME)
SELECT NAME 
FROM QSYS2/SYSPARTITIONSTAT 
WHERE SYSTEM_TABLE_SCHEMA = 'MYLIB' AND SYSTEM_TABLE_NAME LIKE 'MYFILE%'
```

This will insert the names of all files in the `MYLIB` library that start with the prefix `MYFILE` into the `FILELIST` file. You can adjust the library and file name filters as needed.

Note that you will need appropriate authorities to the `SYSPARTITIONSTAT` table and the `FILELIST` file in order to run this statement. Also, make sure to create the `FILELIST` file with the correct fields before running the SQL statement.