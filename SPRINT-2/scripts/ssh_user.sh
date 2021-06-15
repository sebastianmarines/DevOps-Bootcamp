#!/bin/bash

if ! [ $(id -u) = 0 ]; then
   echo "The script need to be run as root." >&2
   exit 1
fi

useradd ssh_user -m -U

echo ssh_user:admin | chpasswd

if ! grep -q "Match User ssh_user" /etc/ssh/sshd_config; then
	sh -c 'echo "
Match User ssh_user
PasswordAuthentication yes

" >> /etc/ssh/sshd_config'
	systemctl restart ssh
fi
