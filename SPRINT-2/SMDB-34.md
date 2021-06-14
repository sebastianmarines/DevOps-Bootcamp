# Security

## Iptables

Iptables is the most common tool used to create firewalls, and works at the kernel level.

This tool manages all IPv4 packets through tables, and each table is made up of several chains. If the packet matches all rules in the chains, the chain policy target determines the final destination of the packet.

## Security groups

A security group is a virtual firewall to control inbound and outbound traffic to your instance.

A security group can only exist in one VPC, and up to 5 security group can be attached to a single instance.
