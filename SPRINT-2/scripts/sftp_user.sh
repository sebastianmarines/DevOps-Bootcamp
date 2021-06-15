#!/bin/bash

if ! [ $(id -u) = 0 ]; then
   echo "The script need to be run as root." >&2
   exit 1
fi

useradd sftp_user -m -U

echo sftp_user:admin | chpasswd

if ! grep -q "Match User sftp_user" /etc/ssh/sshd_config; then
	sh -c 'echo "
Match User sftp_user
PasswordAuthentication yes
ChrootDirectory /var/www
ForceCommand internal-sftp

" >> /etc/ssh/sshd_config'
	systemctl restart ssh
fi
