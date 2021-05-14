# Crontab
Cron is a daemon that executes commands on a specific date and time, and it is used to schedule activities.

To schedule a command that needs to run repeatedly you use the command `cron -e` to edit your crontab file and restart the crontab deamon after you save the file.

A crontab entry is structured in the following way:

minute (0-60) hour (0-23) day of month (0-31) month (1-12) day of the week (0-6) command

There are several directories inside `/etc`: `/etc/cron.daily`, `/etc/cron.hourly`, `/etc/cron.monthly`, and `/etc/cron.weekly`, when you place a script in any of this directories it will execute daily, hourly, monthly or weekly depending on the directory name.

`/etc/cron.d` is a directory where you can put cron files and it is mostly meant to be written by scripts, whereas the `crontab` manages one file per user and is edited through a text editor.

User's crontabs are usually stored in `/var/spool/crontabs/<username>`

