# Shell Variables

## Environment variables

Environment variables are a set of dynamic named values, stored within the system that are used by applications launched in shells or sub-shells.

They allow you to customize how the system works and the behavior of the applications on the system.

## Shell variables

This variables are specific to the system's shell (bash, zsh, fish, etc). They have their own set of internal variables.

## Alias & Export

The *alias* command allows you to specify an alias of a command; for example, you can create the alias `alias cd='rm -rf'` to execute `rm -rf` whenever you type `cd`.

*Export* is used to set an environment variable in the current session. An example use case of *export* is to set an environment variable for a long system path (eg. `/media/sebastian/HDD`) to `export HDD='/media/sebastian/HDD'`, and now you can do `cd HDD` instead of typing the whole path.

## Persistence

### Aliases

To persist an alias you need to save it in your shell configuration file.

To save an alias in a bash shell you need to add it to the `~/.bashrc` file.

### Variables

There are several files where you can store environment variables, and each one will affect different scopes.

- `/etc/environment` - Used to set system-wide environment variables. Entries to this file do not need to start with *export*.
  ```bash
     FOO=BAR
     VAR_TEST="Test var"
  ```
- `/etc/profile` - Variables set here will be loaded when bash login shell is entered. Entries need to start with *export*.
- `~/.bashrc`, `~/.zshrc`, etc - Per user shell configurations.

## Define and use variables and env variables in scripts


