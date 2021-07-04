import os
import sys
import logging
import subprocess
import argparse
import secrets
import shutil
import requests
from typing import Tuple


INSTALLATION_COMMANDS = (
    "apt update",
    "apt upgrade -y",
    "apt install -y nginx mysql-server php-fpm php-mysql",
    "apt install -y php-curl php-gd php-intl php-mbstring php-soap php-xml php-xmlrpc php-zip",
    "systemctl restart php7.4-fpm",
)

WP_PATH = "/var/www/wordpress"


def run_command(command: str, *args):
    arg_list = command.split()
    subprocess.run([*arg_list, *args])


def setup_database(user: str, password: str) -> Tuple[str, str]:
    def _run_db_command(sql_command: str):
        run_command(f"mysql -e", sql_command)

    _user = user or "wordpressuser"
    _password = password or secrets.token_urlsafe()
    _run_db_command(
        "CREATE DATABASE wordpress DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;"
    )
    _run_db_command(f"CREATE USER '{_user}'@'localhost' IDENTIFIED BY '{_password}';")
    _run_db_command(f"GRANT ALL ON wordpress.* TO '{_user}'@'localhost';")

    return _user, _password


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s %(message)s")

    if os.getuid() != 0:
        print("This script needs to be run as root. Exiting", file=sys.stderr)
        sys.exit(os.EX_NOPERM)

    parser = argparse.ArgumentParser(
        description="WP, LEMP, and phpMyAdmin setup script."
    )
    # TODO ask password inside prompt
    parser.add_argument("wpuser", help="Wordpress admin user")
    parser.add_argument("wppassword", help="Wordpress admin password")
    parser.add_argument("--mysqluser", help="MySQL user for Wordpress")
    parser.add_argument("--mysqlpassword", help="MySQL password")

    args = parser.parse_args()

    for command in INSTALLATION_COMMANDS:
        run_command(command)

    db_user, db_password = setup_database(args.mysqluser, args.mysqlpassword)

    os.mkdir(WP_PATH)
    shutil.chown(WP_PATH, "www-data", "www-data")

    with open("/etc/nginx/sites-available/wordpress", "w") as nginx:
        config = requests.get(
            "https://raw.githubusercontent.com/sebastianmarines/DevOps-Bootcamp/master/SPRINT-3/scripts/nginx-wp.conf"
        )
        nginx.write(config.content)
    os.symlink(
        "/etc/nginx/sites-available/wordpress", "/etc/nginx/sites-enabled/wordpress"
    )
    os.unlink("/etc/nginx/sites-enabled/default")
    run_command("service nginx restart")
