# Sudoers file
The sudoers file that specify system's permissions for users, this allows you to control who can do what things.

When a user wants to execute a command as super user, the system checks the `/etc/sudoers` file to determine if the user has permissions.

`root ALL=(ALL:ALL) ALL`
`%admin ALL=(ALL) ALL`

The first line is an example of permissions for a user, and the second one indicates the permissions for a group (because it starts with a `%`).

* The first all refers to the host, this part would become more relevant if we needed to manage a `/etc/sudoers` file for multiple machines, because if the host specified here does not match the machine's host name the rule will be ignored.
* The (ALL:ALL) part of the line is the user and the group. In the above example _root_ can execute commands as all _users_ in all _groups_ 
* The last ALL indicates the command that the user or group can execute.

The _sudoers_ file also has a feature similar to global variables called _aliases_, and there are 4 of them available:
1. User_Alias
2. Runas_Alias
3. Host_Alias
4. Cmnd_Alias

The name of the aliases should be in _UPPERCASE_ and can include numbers and underscores.

You can also specify if a user can run a command as sudo without typing a password. This can be useful if you have a script that needs to run a command with root privileges but can't type the password.
`script ALL=(root) NOPASSWD: /usr/sbin/apache2`

We can also exclude parameter in aliases, for example:
`User_Alias EXCEPT_ROOT = ALL, !root`

It is recommended to edit the sudoers file only with `visudo` because a syntax error in this file could leave us with an unusable system. _visudo_ verifies the file before saving it to avoid this errors.

