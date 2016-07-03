When backing up
===============

If you want to know if there are any files on your computer A that are not on your harddrive B
(and hence they need to be backed up) you can run `zz_ListFolderRecursive.py` on folders in A and B and then use
the txt output that lists all the files to compare A and B

`zz_compareFileLists.py` will then list all missing files searching by filename only. This is useful when you have
different directory structure on A versus B. For example:

    > python zz_compareFileLists.py -b sukaA.txt -t sukaB.txt -o whats-missing.txt

will make `whats-missing.txt` that lists all files in `sukaA.txt` (base or `-b`) that are missing in B (target or `-t`).
Those are the files you should then back up.