## zzz\_ReadmeFromHeaders.py

**MODE OF USE**: Run in a folder

Automatically generates `README.md` file from combined headers of all the scripts.
If `README.md` already exists, it will back it up with a timestamp, this way you are
spared that oops moment...

---

## zz\_collapse\_folders.py

**MODE OF USE**: Run in a folder

Will move files from every folder to this one. Effectively empties
the folders and deletes them.

- NOTE: works 1 level only.
- NOTE: look out for filename conflicts (e.g. `ch1/part1.mp3` & `ch2/part1.mp3`)

---

## zz\_collapse\_folders\_prefix.py

**MODE OF USE**: Run in a folder

Will move files from every folder to this one. Effectively empties
the folders and deletes them. The files will be renamed with the prefix
of the folder where they came from. This avoids conflicts, unlike `zz_collapse_folders.py`

- NOTE: works 1 level only.
- NOTE: Configure `PREFIX_SEPARATOR_CHAR` inside this script if you like

---

## zz\_duplicate\_with\_numerals.py

Apprends _# to each file

**MODE OF USE**: Drag and drop.

1. Drag a file (e.g. `abc.txt`) into it
2. Enter start index X
3. Enter end index Y
4. Will generate files named `abc_X.txt`, ... `abc_5.txt`, `abc_6.txt`, ... and `abc_Y.txt`, all copies of `abc.txt`. Notice how the the range [X..Y] is X,Y-inclusive

---

## zz\_ListFolder.py

**MODE OF USE**: Run in a folder

Generates `zz_fileListing.txt` with all the contents of this folder (1 level)

---

## zz\_mp3\_convert\_makeBatFile.py

**MODE OF USE**: Run in a folder (with wavs!)

Generates a batch file that converts every single wav in this folder to mp3 using
`Lame For Audacity`. Also makes the "convert" directory if it doesn't exist.
Feel free to change the path to lame if you dare...

---

## zz\_newFolder.py

**MODE OF USE**: Run in a folder

Automatically generates a new folder that begins with a date stamp (`year_month_day`)

---

## zz\_rename\_addPrefix.py

**MODE OF USE**: Run in a folder

Renames all files. Apprends `prefix_` to each filename.

---

## zz\_rename\_prefix\_with\_numerals.py

**MODE OF USE**: Run in a folder

WARNING!!! Will rename all files in the folder where this script is run.

Enter prefix. Let's say you entered "newfilename". All the files will be renamed to `newfilename_1.txt`, `newfilename_2.mp3`, ... for all files in the folder, in the order of alphabet, I guess.

EXCEPTED: `.exe`, `.dll`, `.py`, `.bat`, folders

---

## zz\_rename\_reverse.py

**MODE OF USE**: Drag and drop.

Quick

- drag up to N files into me.
- 2 files: `[1,2]` => `[2,1]` (swap)
- 3 files: `[1,2,3]` => `[3,2,1]`
- 4 files: `[1,2,3,4]` => `[4,3,2,1]`

Lengthy

- When you drag 2 files `a.txt` and `b.txt` the files are renamed, their names swapped.
- When you drag `a.txt`, `b.txt`, `c.txt`, `a` is renamed to `c` and `c` to `a`. `b.txt` stays.
- When 4 files are dragged in: a, b, c, d... a is renamed d, b is renamed c...
- 5 files... you get the idea!

---

## zz\_rename\_toLowercase.py

**MODE OF USE**: Run in a folder

Renames all files to lowercase. Works only on one level of the folder

---

## zz\_template\_as\_filenames.py

**MODE OF USE**: Drag and drop.

1. create a subfolder in the directory with your files
2. put __template.png in the subfolder + this python script
3. run this python script from the subfolder

---

## zz\_uniquelines.py

**MODE OF USE**: Drag and drop.

This is usually ran on files (txt) to eliminate duplicate lines.
For every `file.txt` dragged in, this script creates `file.txt.unique` which has only the unique lines.

---

