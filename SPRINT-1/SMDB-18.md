# Processes

Processes are running programs inside a system, and they require resources like CPU time and memory. They can be **started**, **stopped**, **interrupted**, and **killed**.

When the kernel starts it spawns an _init process_ (this process is commonly systemd) with PID 1, and it is the parent of all other processes.

The steps needed to create a process is to first _fork_ the current process that is executing and this operation will copy everything from the parent process. When you have a forked process the next step is to use the _execute_ operation to replace the current process.

- Startup time: When the process was created
- PID: A unique identifier for the process
- Process status: 
  - *D* Uninterruptible sleep
  - *R* Running
  - *S* Interruptible sleep
  - *T* Stopped
  - *Z* Defunct: Terminated but not closed by the parent process
- Load average: The average system load calculated over 1, 5, and 15 minutes
- Memory used by a process: The memory that a process is using. By default `ps` gives the memory percentage, to show it we use the command `ps -p <PROCESS_ID> -o %mem`
- CPU used by a process: `ps -p <PROCESS_ID> -o %cpu`
- PID file: This is a file that only contains the PID of a process, this type of files can be useful to stop a process because grepping the process list may return multiple instances of the same software, and using the PID file we can ensure that we are killing the process that we need to kill. It is also used by some software to ensure that there is only one instance of the same application running.
- chkconfig: This tool helps to manage services running in the operating system. It can display the service list and the run level each service executes in, allows you to deactivate services, and to add new services. _chkconfig_ was replaces by _systemctl_ in most modern systems.
- systemctl: This is a tool that helps to manage `systemd` services, it allows to start and stop services, as well to reload, restart, enable, and disable services.
