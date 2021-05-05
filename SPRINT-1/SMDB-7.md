# File manipulation I/O
## Cat
It allows to create single or multiple files, view the content of a file, and concatenate files.

**Syntax**: `cat [OPTION] [FILE]`

- `cat /etc/passwd` Display contents of file
- `cat file1 file2` View contents of mutiple files
- `cat -n file1` Show file contents with line numbers
- `cat file1 > file2` Put contents of file1 on file2
- `cat file1 >> file2` Append contents of file1 to file2
- `cat file1 file2 file3 > file4` Create a new file containing the contents of 3 files
  
## Head
It displays the top _N_ numbers of lines of the given input. By default _N_ is 10. 
- `head file1` Displays the first 10 lines of the file
- `head -n 3 file1` Displays the first 3 lines of the file
- `ls -t | head -n 3` Displays the three most recently used files

## Tail
It works similarly to _head_ but instead displays the last lines of the given input.

## More
This command is used to display large text files one page at a time and it lets you navigate through pages to see the whole file.

`more <file>`

## Less
This command works similarly to _more_ but has more advanced features. This command is speccialy useful when opening very large files because it does not read the entire file which results in faster load times.

Basic usage: `less [OPTIONS] filename`

You can also pass the output of another command to less: `ps aux | less`

Options:
- `-N` Show line numbers
- `-X` Leave contents on screen on exit
- `+F` Watch file for content change

The movement commands are similar to _Vi_

## Touch
The touch command allows us to create empty files, as well as updating the timestamps on existing files.

Examples:
- `touch file` Create an empty file
- `touch file file1 file2` Create multiple empty files
- `touch -c file` Modify the timestamps of an existing file
- `touch -a file` Change only the access time
- `touch -m file` Change only the modification time

## Grep/ZGrep
Grep _(global regular expression print)_ searches one or more input files for lines that match a specific pattern.
- `grep bash /etc/passwd` Search for a string in a file
- `grep -v nologin /etc/passwd` Search for lines that don't include a pattern
- `ps -ef | grep www-data` Filter the output of a command
- `grep -r term /etc` Search recursively in a directory
- `grep -l term *.conf` Show only the file names 
- `grep -i Zebra words.txt` Case insensitive search
- `grep -w the words.txt` Search only full words
- `grep -n term words.txt` Display the line number 

ZGrep is similar to _Grep_ but can search on compressed files

## I/O Redirection
I/O redirections allow you to redirect the output of a command before it is executed.

You can overwrite the destination's existing contents:
- **>** standard output
- **<** standard input
- **2>** standard error

And append to existing contents:
- **>>** standard output
- **<<** standard input
- **2>>** standard error

Examples: 
- `ls > files.txt` Write the output of the ls command to the _files.txt_ file
- `ls > /dev/null` Discard the output of a command
- `mkdir '' 2> mkdir_log.txt` Write the errors of a command to a file
- `echo "Hello world" >> log.txt` Append output of command to file
- `find '' 2> stderr_log.txt` Append the error of a command to a file
- `less < /etc/passwd` Send the contents of a file as an argument to a command