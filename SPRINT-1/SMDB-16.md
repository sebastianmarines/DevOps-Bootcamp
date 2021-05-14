# Monitoring Commands

## Memmon
Memmon is a supervisor that may be subscribed to a tick event. A tick happens every _x_ seconds (60 seconds is recommended), and when memmon receives this event it checks that all the programs running under a supervisor are not exceeding a certain amount of memory.

If a process exceeds this limit, memmon will restart the process and optionally send an email.

## Htop/top
Htop is an interactive system monitor, process viewer and process manager.

The main differences between _top_ and _htop_ is that htop shows all the processes and not just the top resource consuming ones, can display processes as a tree and uses colors to provide statistics.

## Sar (sysstats)
_System Activity Report_ is a tool used to collect and save data about the CPU, memory, and read/writes to the disk

## Lsof
Shows details about files being used by all the running processes.

## Ps
(Process status) is a command that shows you the state of a process or a list of processes.

## Iostat
This command is used to monitor the system I/O, and help you visualize the system's load; it is often used to identify performance issues with storage devices.

## Pkstat
..

## Df
_Disk Free_ gives you an overview of your file system and all mounted disks.

It tells you the total disk size, space used, space available, usage percentage, and what partition the disk is mounted on.

## Du
_Disk usage_ is used to get the size of a current directory.

## Netstat
The netstat command displays networks status and protocol statistics. 

It also gives information about the ports and addresses that are being used.
