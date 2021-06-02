# Scripting

## sed

SED (Stream Editor) is a tool that allows us to search, search and replace, insert, and delete inside files; but the most commmon use case of *sed* is to modify files.

**Basic format**:

`sed [-ns] '[direction] instruction arguments'`

- **[direction]**: Optional. Could be a line number, a line range, or a regex expression. If it is not specified, sed scans every line.
- **instruction**:
  - **i**: Insert line before current line.
  - **a**: Insert line before current line.
  - **c**: Change current line.
  - **d**: Delete current line.
  - **p**: Print current line in stdout.
  - **s**: Change string in current line.
  - **r file**: Add contents of *file* to current line.
  - **w file**: Write output to file.
  - **!**: Apply action to lines not selected by the condition.
  - **q**: Stop processing the file.
- **-n**: Do not show processed lines in stdout.
- **-s**: Treat all files as separate streams.

**Examples**:
- `sed 's/String 1/String 2/g' file` Replace all occurrences of *String 1* with *String 2* in all the file.
- `sed '5,6 s/old/new/g' file` Replace occurrences of *old* in line 5 and 6 with *new*.
- `sed 's/^/   /' file` Insert 3 whitespaces at the start of every line
- `sed 10q` Show the first 10 lines in the file.
- `sed '2,4 d'` Delete the lines 2 to 4.

## awk

AWK is a pattern processing tool. It has its own scripting language where we can define variables, use arithmetic operators, flow control, and loops.

Its name derives from the initials of the authors' last names.

It can take the following options:

- **-F** to specify a separator
- **-f** to specify a file containing an awk script.
- **-v var=value** to declare a variable.

To define an awk script we use curly braces surrounded by single quotation marks:
`awk '{print "Hello world"}'`

### Variables

- **$0**: The whole line
- **$n**: Nth field

### Examples

- `awk -F: '{print $1 " home at " $6}' /etc/passwd`
- `awk -F: '$1=="root" {print}' /etc/passwd` Print the root user
- `seq 50| awk 'BEGIN {a=1; b=1} {print a; c=a+b; a=b; b=c}'` Fibonacci sequence

## Bash

Bourne Again Shell is a popular script tool for Unix systems.

It is installed by default on most systems and can help us write scripts to automate repetitive tasks.

## Sort

This tools helps us sort input lines based on some criteria.

### Options

- **-b** Ignore whitespaces.
- **-d** Sort ignoring all characters except letters, numbers, and whitespaces.
- **-f** Case insensitive.
- **-n** Sort by numerical value.
- **-r** Reverse the order.
- **-k n1,[n2]** Specify a field as the sorting key.
- **-o <FILE>** Store the output in a file.

## Shebang

The shebang specifies what interpreter should be used to execute a script. It starts with `#!`

`#!/usr/bin/bash`

If an interpreter is not specified, it fallbacks to `/bin/sh`.

## For

```bash
   for ITEM in [LIST] do
      [COMMANDS]
   done
```

## If

```bash
   if CONDITION then
     [COMMANDS]
   fi
```

## While

```bash
   while [CONDITION] do
     [COMMANDS]
   done
```

## Case

```bash
   case EXPRESSION in
     PATTERN_1)
       STATEMENTS
     ;;

     PATTERN_N)
       STATEMENTS
     ;;

     *)
       STATEMENTS
     ;;
   esac
```

## Variables

```bash
   VAR="VALUE"
   echo $VAR
```

## Reading variables from another file

*CONFIG.sh*

```bash
   URL="https://google.com"
```

*SCRIPT.sh*

```bash
   #!/usr/bin/bash
   source CONFIG.sh
   echo $url
```

```terminal
   $ ./SCRIPT.sh
   https://google.com
```

## Functions

```bash
   function_name() {
     commands
   }
```
