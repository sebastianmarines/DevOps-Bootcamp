# Package managers
A package manager keeps track of the software installed on your computer, allowing you to install new software, upgrade to newer versions, and remove software that you installed.
Different distros have several ways of packaging software; in particular, Debian based systems use the _.deb_ format and Red Hat based distros use _.rpm_.

## What is a package?
A package is just a particular program. Some packages depend on other packages to work correctly, so package managers need to keep track of the package you installed and its dependencies.

## What is a repository?
A repository is a central server where all packages available for a specific distribution live. You can add non-official repositories to your system to install software that is not available on the official repository.

## Package managers and their distros
- **apt/apt-get**: Debian based (Ubuntu, Mint, etc.)
- **dpkg**: _Same as apt_
- **yum**: Red Hat based (CentOS, Fedora, etc.)
- **rpm**: _Same as yum_
- **dnf**: Fedora, RHEL
- **pacman**: Arch based (Manjaro, Parabola, etc.)
- **yast**: openSUSE
- **apk**: Alpine

## How to install a package?
- **apt/apt-get**: `apt install <packagename>`
- **dpkg**: `dpkg -i package.deb`
- **yum**: `yum install <packagename>`
- **rpm**: `rpm -i package.rpm`
- **dnf**: `dnf install <packagename>`
- **pacman**: `pacman -S <packagename>`
- **yast**: `GUI`
- **apk**: `apk add <packagename>`

## How to remove a package?
- **apt/apt-get**: `apt remove <packagename>`
- **dpkg**: `dpkg --remove <packagename>`
- **yum**: `yum remove <packagename>`
- **rpm**: `rpm -e package.rpm`
- **dnf**: `dnf remove <packagename>`
- **pacman**: `pacman -R <packagename>`
- **yast**: `GUI`
- **apk**: `apk del <packagename>`

## How to list installed packages?
- **apt/apt-get**: `apt list --installed`
- **dpkg**: `dpkg-query -l`
- **yum**: `yum list --installed`
- **rpm**: `rpm -qa`
- **dnf**: `dnf list instaled`
- **pacman**: `pacman -Qe`
- **yast**: `GUI`
- **apk**: `apk info`

## How to add a repository?
- **apt/apt-get**: `add-apt-repository <repository>`
- **dpkg**: _same as apt_
- **yum**: `yum-config-manager --add-repo <repo_url>`
- **rpm**: _same as yum_
- **dnf**: `dnf --config-manager --add-repo <repo_url>`
- **pacman**: 
  ```conf
    # Edit /etc/pacman.conf

    [repo_name]
    SigLevel = Required DatabaseOptional
    Server = <repo_url>
  ```
- **yast**: `GUI`
- **apk**: 
  ```conf
  # /etc/apk/repositories
  # You just need to add the repository url to this file
  # Then run apk update
  
  https://<mirror-server>/alpine/<version>/community
  ```
  