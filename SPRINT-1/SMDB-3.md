# What is linux?
_Linux_ is an open source operating system that was created as an alternative to _UNIX_.
It is comprised of a bootloader, the kernel, an init system, daemons, a graphical server in charge of displaying things in your monitor, an optional desktop environment, and additional applications.

# Who created linux?
Linux was created by Linus Torvalds. In 1990 he started developing an experimental kernel as an alternative to Linux. Around the same time when the first stable version of linux was released, Richard Stallman, an open-source advocate, was trying to develop a UNIX-like operating system, but he started developing the utilities that the operating system would use. Later, this GNU tools were added to the linux kernel to create GNU/Linux.

# What is the kernel of linux?
The kernel is the piece of software that serves as a communication interface between the operating system and the underlying hardware. It is in charge of managing memory, managing all the processes, control hardware, and making system calls.

# Linux directory structure
- `/` __Root directory__
	- `/bin` __Essential binaries__ 
	Contains important system programs and utilities such as bash
	- `/boot` __Static boot files__ 
	Files needed to boot the system. Ex. GRUB bootloader and the kernel.
	- `/dev` __Device files__
	This directory contains special files, including those relating to physical devices.
	These files are virtual and are not physically in the disk.
	- `/etc` __Configuration files__
	This directory contains configuration files for the system like the password file and the networking config.
	- `/usr` __User binaries and program data__
	Executable files and libraries
		- `/bin` __Basic user commands__
		- `/sbin` __Additional commands for the administrator__
		- `/lib` __System libraries__
		- `/share` __Contains documentation__
	- `/home` __User personal data__
	- `/lib` __Shared libraries__
	- `/sbin` __System binaries__ Similar to _/bin_ but the binaries stored here can only be executed by superusers.
	- `/tmp` __Temporary files__
	- `/var` __Variable data files__
	Here, programs store runtime information like logs, user tracking, caches, and other files that programs create.
	Files stored here are not deleted automatically, so this is a good place to look for information about the system's behavior.
	- `/proc` __Processes and kernel files__
	This directory contains information about running processes and kernel parameters.
	- `/opt` __Optional software__
	Used for installing third party applications that are not available from the distribution's repositories.
	- `/root` __Home directory of the root user__
	- `/media` __Mount point for removable media__
	- `/mnt` __Mount directory__ Similar to _/media_ but it is used to manually mount a volume.
	- `/srv` __Service data__ Contains data for services provided by the system.

# What is a distro in Linux?
A Linux distro is an operating system designed from the Linux kernel that includes custom software and package managers.

# What is a shell?
It is a program that takes commands from the user and gives them to the operating system to perform.

# What are the main shells that exist?
- Bash
- Zsh
- Fish
- Sh
- Csh 

# List of main commands
- `ls` List directory content
- `cd` Change directory
- `pwd` Get the path of the current directory
- `cat` Show the content of a file
- `cp` Copy files
- `mv` Move files
- `mkdir` Create a new directory
- `rmdir` Remove an empty directory
- `rm` Remove files and directories
- `touch` Create a blank file
  
# Different clouds in the market
These are the 10 biggest cloud providers ranked by size:
- AWS
- Microsoft Azure
- Google Cloud
- Alibaba Cloud
- IBM Cloud
- Oracle
- Salesforce
- SAP
- Rackspace Cloud
- VMWare

# AWS Core services
- __EC2 (Elastic Compute Cloud)__ 
Service that provides secure, resizable compute capacity in the cloud.
- __S3 (Simple Storage Service)__ 
Object storage service with 99.999999999% durability.
- __RDS (Relational Database Service)__
Service that provides relational databases that are easy to setup, operate and scale databases.
- __Lambda__ 
Run code without provisioning or managin services. You only pay for the compute time you consume.
- __Route 53__ 
Highly available DNS service. 
- __SNS (Simple Notification Service)__ 
Pub/Sub messaging and mobile notifications.
- __SQS (Simple Queue Service)__
Fully managed message queuing service.

# AWS EC2
EC2 is a service that provides scalable computing capacity in the cloud.
AWS provides virtual computing environments (instances), preconfigured templates (AMIs), various hardware configurations, persistent storage using EBS, multiple physical locations for resources, firewall rules using security groups, static IPv4 addresses, and virtual networks isolated from the rest of the AWS Cloud.
There are 4 types of instances:
- General purpose
- Compute optimized
- Memory optimized 
- Storage optimized

# S3
An S3 bucket is a container for objects and provides the mechanisms neccessary to control access to them. In a S3 bucket files are stored as objects and not as blocks. The object includes the data itself, metadata and an unique identifier. An S3 bucket can't have directories, and when you create one in the S3 console the files uploaded there have their name with the directory included in it, but everything is stored in the root of the bucket.

# RDS
RDS is a service that allows you to provision fully managed databases, without worrying about backups, upgrades, configuration, and the underlying hardware. RDS is compatible with PostgreSQL, MySQL, MariaDB, Oracle DB, and Microsoft SQL Server.
The top features about RDS are availability, as it allows you to deploy your databases on multiple availability zones; scalability, as you can add more CPU and memory to your database, but also scale horizontally adding more servers; and performance, as it includes a dashboard that helps you troubleshoot the performance of your databases, and it has two types of storage available to choose: General Purpose Storage and Provisioned IOPS Storage for faster reads.