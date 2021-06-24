# Logging

Linux logs are stored in the `/var/log` directory.

- **syslog/messages**: This files store all system activity data, including startup messages. Debian based systems use *syslog* and Red Hat based systems use *messages*.
- **auth.log/secure**: Security related events such as logins, root user actions, and PAM outputs. Debian based systems use *auth.log* and Red Hat based systems use *secure*.
- **kern.log**: Kernel events, errors, and warnings.
- **cron.log**: Logs about cronjobs.

## Syslog

Syslog is a standard for creating and transmitting logs.

It is composed of:

- **Syslog service**: Receives and processes syslog messages. It listens to events by creating a socket which applications can write to.
- **Syslog protocol**: A transport protocol that specifies how to transmit logs over a network.
- **Syslog message**: Any log formatted with the Syslog message format.

## Syslog message format

```
   Jun 4 22:14:15 server1 sshd[41458] : Failed password for root from 10.0.2.2 port 22 ssh2
```

This format includes a header with the timestamp, the name of the application that generated the event, the location in the filesystem, and the priority.

