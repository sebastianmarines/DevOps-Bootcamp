# Volumes
A volume is a single accessible accessible storage area within a single file system. The difference with a partition is that the partition is a logical portion of a physical storage volume.

## Format a volume
To format a volume in linux you use the _mkfs_ command.

Example:
`sudo mkfs -t ext4 /dev/sdb1` to format the partition in _/dev/sdb1_ with **ext4** file system.

## SWAP
Swap is a space in linux that is used when the amount of physical RAM memory is full. When the system runs out of RAM, inactive pages are moved from the RAM to the swap space.

## Fstab
The fstab file is used to define how partitions, devices, or remote file systems should be mounted into the file system.

The file systems definitions will be converted into systemd mount units at boot.

The `mount` command uses the fstab file to mount devices.

```
# <device>            <dir>     <type>     <options>      <dump> <fsck>
LABEL=cloudimg-rootfs   /        ext4   defaults,discard     0      1
```

- **device**: Describes the file system to be mounted
- **dir**: Where to mount it
- **type**: The file system type
- **options**: Mount options
- **dump**: Configure checking by the `dump` utility
- **fsck**: The order for filesystems check at boot time. The root device should be 1. Other partitions should be 2 or 0 to disable checking

