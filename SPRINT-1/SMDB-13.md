# Hardlinks and Softlinks
A symlink is a file that points to another file in the system, and there are two types: _hard links_ and _soft links_.

## Soft links
A soft link is similar to windows' shortcuts, as they just point to where the original file is. 

Soft links just contain the path to the original file, not the contents.

If you delete the original file or directory, the soft link will not be deleted but it will not work because the file it points to no longer exists.

## Hard links
Hard links do a similar job to soft links but they have some differences:
1. They store the contents of the original files
2. They have the same permissions as the original file
3. Can't link directories
4. The link and the file needs to be in the same file system
5. If you delete the original file, the hard link will still have its contents.

