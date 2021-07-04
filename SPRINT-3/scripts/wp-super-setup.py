import os
import sys
import logging
import subprocess
import argparse


COMMANDS = (
    "apt update",
    "apt upgrade -y",
    "apt install -y nginx mysql-server php-fpm php-mysql",
    "apt install -y php-curl php-gd php-intl php-mbstring php-soap php-xml php-xmlrpc php-zip",
    "systemctl restart php7.4-fpm",
)


def run_command(command: str):
    arg_list = command.split()
    subprocess.run(arg_list)


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s %(message)s")

    if os.getuid() != 0:
        print("This script needs to be run as root. Exiting", file=sys.stderr)
        sys.exit(os.EX_NOPERM)

    parser = argparse.ArgumentParser(
        description="WP, LEMP, and phpMyAdmin setup script."
    )
    parser.add_argument("wpuser", help="Wordpress admin user")
    parser.add_argument("wppassword", help="Wordpress admin password")
    parser.add_argument("--mysqluser", help="MySQL user for Wordpress")
    parser.add_argument("--mysqlpassword", help="MySQL password")

    args = parser.parse_args()

    print(args.wpuser)
    # for command in COMMANDS:
    #     run_command(command)
