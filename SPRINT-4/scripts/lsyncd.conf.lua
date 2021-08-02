settings {
    maxProcesses = 1,
    logfile = "/var/log/lsyncd.log",
    insist = true,
    nodaemon = true
}

targetlist = {"ubuntu@34.223.216.121"}

for _, server in ipairs(targetlist) do
    sync {
        default.rsyncssh,
        delete = false,
        source = "/home/sebastian/DevOps-Bootcamp",
        rsync = {
            binary = "/usr/bin/rsync",
            archive = true,
            perms = true,
            owner = true,
            _extra = {"-a"},
            update = true,
            protect_args = true,
            sparse = true,
            rsh = "/usr/bin/ssh -i /home/sebastian/.ssh/SEBASTIAN.pem -o StrictHostKeyChecking=no",
            compress = true
        },
        host = server,
        targetdir = "/home/ubuntu/rsync-folder"
    }
end
