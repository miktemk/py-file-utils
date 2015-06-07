#### `zz_duplicate_with_numerals.py`

**MODE OF USE**: Drag and drop.

1. Drag a file (e.g. `abc.txt`) into it
2. Enter start index X
3. Enter end index Y
4. Will generate files named `abc_X.txt`, ... `abc_5.txt`, `abc_6.txt`, ... and `abc_Y.txt`, all copies of `abc.txt`. Notice how the the range [X..Y] is X,Y-inclusive

-----

#### `zz_rename_with_numerals.py`

**MODE OF USE**: Run in a folder

WARNING!!! Will rename all files in the folder where this script is run.

Enter prefix. Let's say you entered "newfilename". All the files will be renamed to `newfilename_1.txt`, `newfilename_2.mp3`, ... for all files in the folder, in the order of alphabet, I guess.

EXCEPTED: `.exe`, `.dll`, `.py`, `.bat`, folders

-----

#### `zz_uniquelines.py`

**MODE OF USE**: Drag and drop.

This is usually ran on dictionary files (txt) to eliminate duplicate lines. For every `file.txt` dragged in, this script creates `file.txt.unique` which has only the unique lines.

-----

#### `zz_template_as_filenames.py`

**MODE OF USE**: Drag and drop.

1. create a subfolder in the directory with your files
2. put __template.png in the subfolder + this python script
3. run this python script from the subfolder

-----

#### `zz_reverse_rename.py`

**MODE OF USE**: Drag and drop.

 - When you drag 2 files `a.txt` and `b.txt` the files are renamed, their names swapped.
 - When you drag `a.txt`, `b.txt`, `c.txt`, `a` is renamed to `c` and `c` to `a`. `b.txt` stays.
 - When 4 files are dragged in: a, b, c, d... a is renamed d, b is renamed c...
 - 5 files... you get the idea!

-----
