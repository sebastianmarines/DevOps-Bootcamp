# Init levels
Init levels defines what system services are operating. A system can only be in a certain init level at any given time.

| Level number | Type                            | Description                                 |
| ------------ | ------------------------------- | ------------------------------------------- |
| 0            | Power down                      | Shut down the operating system              |
| 1            | Administrative state            | Access file system. Login disabled          |
| 2            | Multi user mode                 | Does not configure network or start daemons |
| 3            | Multi user mode with networking | Starts the system normally                  |
| 4            | Undefined                       |                                             |
| 5            | X11                             | Same as level 3 + display manager           |
| 6            | Reboot                          | Reboots the system                          |

