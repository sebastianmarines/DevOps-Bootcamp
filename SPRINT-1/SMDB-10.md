# U Mask
_U Mask_ is a UNIX function to set the permissions that new files created by the current process will have.
By default newly created files have **666** permissions and directories **777**.
It is not possible to set a umask to have execute permissions on files by default.

The umask will substract the permissions from the defaults. For example a umask of 077 will turn off all permissions for anyone except the owner (666-077=600 or rwx------)

A usecase for _umasks_ is preventing other users in the system from accessing your files, so we could edit the `~/.profile` file and add a umask of 007 so that all the files you create have permissions of rw-rw----
