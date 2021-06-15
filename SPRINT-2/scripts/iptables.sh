#!/bin/bash

if ! [ $(id -u) = 0 ]; then
   echo "The script need to be run as root." >&2
   exit 1
fi

apt install -y iptables-persistent

sudo iptables -A INPUT -p tcp --dport 22 -j DROP

iptables-save > /etc/iptables/rules.v4
ip6tables-save > /etc/iptables/rules.v6

