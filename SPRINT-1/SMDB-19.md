# Volumes
A volume is a single accessible accessible storage area within a single file system. The difference with a partition is that the partition is a logical portion of a physical storage volume.

## Format a volume
To format a volume in linux you use the _mkfs_ command.

Example:
`sudo mkfs -t ext4 /dev/sdb1` to format the partition in _/dev/sdb1_ with **ext4** file system.

## SWAP
Swap is a space in linux that is used when the amount of physical RAM memory is full. When the system runs out of RAM, inactive pages are moved from the RAM to the swap space.

## Fstab
