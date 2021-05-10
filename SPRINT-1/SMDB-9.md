# Permissions

## Types of permissions
- Read
- Write
- Execute

## Managing permissions
To change the permissions for a file or directory you use the `chmod` command.

You can use the `-R` flag to recursively apply permissions to files inside a directory.

The `chmod` command can be used with symbolic and absolute forms.

### Symbolic
This method consists of at least three parts:
| Access class        | Operator             | Access Type |
| ------------------- | -------------------- | ----------- |
| u (user)            | + (add access)       | r (read)    |
| g (group)           | - (remove access)    | w (write)   |
| o (other)           | = (set exact access) | x (execute) |
| a (all: u, g and o) |                      |

Example: `chmod a+r file`

### Absolute form
You specify the permision with numbers, each number is the sum of values that specify read, write and execute permissions.

| Permission  | Number |
| ----------- | ------ |
| Read (r)    | 4      |
| Write (w)   | 2      |
| Execute (x) | 1      |

For example, `chmod 751` will grant read, write, and execute permisions to your user (4+2+1=7), read and execute permissions to users in your group (4+0+1=5), and execute permissions to others (0+0+1=1).

## Commands
- **chown**: Used to change the owner of a file or directory. Usage: `chown [-R] user file`
- **chmod**: Used to change permissions of a file or directory.
- **useradd/adduser**: Useradd is a system binary used to create users, and adduser is a wrapper script written in Perl that calls the _useradd_ binary. The difference between useradd and adduser is that adduser creates the home directory for the user by default and useradd needs the `-m` flag to create the home directory.
- **passwd**: Change the password of a user. Usage: `passwd user`
- **usermod**: User administration.
	- `usermod -g group user`: Change the primary group of a user.
	- `usermod -a -G group1,group2 user`: Add another group to a user.
	- `usermod -d /newhome/username user`: Change the home directory of a user.

## User files structure
### /etc/passwd
Each row of this files represents a user and it has 7 fields separated by a _:_ 
`ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash`

1. **Username**
2. **Password**: An _x_ that indicates that the hashed password is stored in _/etc/shadow_
3. **User ID (UID)**
4. **Group ID (GID)**
5. **User ID Info**: Extra information about the user
6. **Home directory**
7. **Command or shell**

### /etc/shadow
This file stores hashed passwords and validity information of the accounts.
`ubuntu:!:18754:0:99999:7:::`

1. **Username**
2. **Hashed password**
3. **Days elapsed since 1-1-1970 when the password was changed for the last time**
4. **Minimum number of days that need to pass before changing the password again**
5. **Maximum number of days that the account is valid**
6. **Number of thays on when the system will remind that the password is about to expire**
7. **Number of days after the password expires when the account will be deactivated**
8. **Expiration date of the account. Expressed in number of days elapsed since 1-1-1970**

### /etc/group
It stores groups information and defines the groups to which users belong to.
`adm:x:4:syslog,ubuntu`
1. **Group name**
2. **Password**
3. **Group ID (GID)**
4. **Group list**: List of users that are members of the group
