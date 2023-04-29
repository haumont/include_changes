PGM

/* Could you rewrite compare_files.py in CL language for OS400, but applying */
/* to a OS400 library and its library memebers?                              */

/* Declare variables */
DCL VAR(&LIBRARY) TYPE(*CHAR) LEN(10)
DCL VAR(&FILELIST) TYPE(*CHAR) LEN(5000)
DCL VAR(&FILECOUNT) TYPE(*DEC) LEN(5 0)
DCL VAR(&FILE) TYPE(*CHAR) LEN(10)
DCL VAR(&MBRLIST) TYPE(*CHAR) LEN(5000)
DCL VAR(&MBRCOUNT) TYPE(*DEC) LEN(5 0)
DCL VAR(&MBR) TYPE(*CHAR) LEN(10)
DCL VAR(&FILEFOUND) TYPE(*LGL) VALUE('0')

/* Display help message if necessary */
IF COND(&ARGV *EQ 'HELP') THEN(DO)
    /* Display help message */
    SNDPGMMSG MSG('This program compares the list of files in an OS400 library and its members with a given list of files.') MSGTYPE(*COMP)
    SNDPGMMSG MSG('Usage: COMPARE_FILES <LIBRARY> <FILELIST>') MSGTYPE(*COMP)
    SNDPGMMSG MSG('  LIBRARY   - Name of the OS400 library to compare') MSGTYPE(*COMP)
    SNDPGMMSG MSG('  FILELIST  - List of files to compare, one filename per line') MSGTYPE(*COMP)
    RETURN
END

/* Parse command line parameters */
CHGVAR VAR(&LIBRARY) VALUE(%SST(&ARGV 1 10))
CHGVAR VAR(&FILELIST) VALUE(%SST(&ARGV 11))

/* Count the number of files in the list */
CHGVAR VAR(&FILECOUNT) VALUE(%BIN(%LEN(&FILELIST) / 10))

/* Loop through the list of files */
DOFOR VAR(&I) FROM(1) TO(&FILECOUNT)
    /* Get the next file from the list */
    CHGVAR VAR(&FILE) VALUE(%SST(&FILELIST (&I * 10 - 9) 10))
    /* Initialize file found flag */
    CHGVAR VAR(&FILEFOUND) VALUE('0')
    /* List members in library */
    DSPLIB OBJ(&LIBRARY) OBJTYPE(*FILE) OUTPUT(*OUTFILE) OUTFILE(QTEMP/FILELIST)
    /* Count the number of members in the list */
    RCVF
    MONMSG MSGID(CPF0864) EXEC(GOTO CMDLBL(NOLIB))
    CHGVAR VAR(&MBRCOUNT) VALUE(%SST(&FILELIST 74 5))
    /* Loop through the list of members */
    DOFOR VAR(&J) FROM(1) TO(&MBRCOUNT)
        /* Get the next member from the list */
        CHGVAR VAR(&MBR) VALUE(%SST(&MBRLIST (&J * 10 - 9) 10))
        /* Compare the member name to the file name */
        IF COND(&MBR *EQ &FILE) THEN(DO)
            /* File found in library */
            CHGVAR VAR(&FILEFOUND) VALUE('1')
            /* Exit loop */
            GOTO CMDLBL(ENDMBR)
        END
    ENDDO
    /* Check if file was found */
    IF COND(&FILEFOUND *EQ '0') THEN(DO)
        /* File not found in library */
        SNDPGMMSG MSG('File ' *BCAT &FILE *BCAT ' not found in library ' *BCAT &LIBRARY) MSGTYPE(*ESCAPE)
    END
    /*
