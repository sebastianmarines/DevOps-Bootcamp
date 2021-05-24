# Processes

Processes are running programs inside a system, and they require resources like CPU time and memory. They can be **started**, **stopped**, **interrupted**, and **killed**.

When the kernel starts it spawns an _init process_ (this process is commonly systemd) with PID 1, and it is the parent of all other processes.

The steps needed to create a process is to first _fork_ the current process that is executing and this operation will copy everything from the parent process. When you have a forked process the next step is to use the _execute_ operation to replace the current process.




