import argparse
import logging
import os
import secrets
import shutil
import subprocess
import sys
from typing import Tuple

import requests

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


def setup_wordpress(
    *,
    user: str,
    password: str,
    site_url: str,
    email: str,
    db_user: str,
    db_password: str,
):
    def _run_wp_command(command: str):
        run_command(f"sudo -u www-data {command}")

    os.chdir(WP_PATH)
    _run_wp_command("wp core download --locale=es_ES")
    _run_wp_command(
        f"wp config create --dbname=wordpress --dbuser={db_user} --dbpass={db_password}"
    )
    _run_wp_command(
        f'wp core install --url={site_url} --title="Este es mi sitio hecho con WordPress" --admin_user={user} --admin_password={password} --admin_email={email}'
    )


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s %(message)s")

    if os.getuid() != 0:
        print("This script needs to be run as root. Exiting", file=sys.stderr)
        sys.exit(os.EX_NOPERM)

    parser = argparse.ArgumentParser(
        description="WP, LEMP, and phpMyAdmin setup script."
    )
    # TODO ask password inside prompt
    parser.add_argument("wp_user", help="Wordpress admin user")
    parser.add_argument("wp_password", help="Wordpress admin password")
    parser.add_argument("site_url", help="Site url")
    parser.add_argument("email", help="Admin email")
    parser.add_argument("--mysql_user", help="MySQL user for Wordpress")
    parser.add_argument("--mysql_password", help="MySQL password")

    args = parser.parse_args()

    for command in INSTALLATION_COMMANDS:
        run_command(command)

    db_user, db_password = setup_database(args.mysql_user, args.mysql_password)

    os.mkdir(WP_PATH)
    shutil.chown(WP_PATH, "www-data", "www-data")

    with open("/etc/nginx/sites-available/wordpress", "wb") as nginx:
        config = requests.get(
            "https://raw.githubusercontent.com/sebastianmarines/DevOps-Bootcamp/master/SPRINT-3/scripts/nginx-wp.conf"
        )
        nginx.write(config.content)

    os.symlink(
        "/etc/nginx/sites-available/wordpress", "/etc/nginx/sites-enabled/wordpress"
    )
    os.unlink("/etc/nginx/sites-enabled/default")
    run_command("service nginx restart")

    with open("/usr/local/bin/wp", "wb") as wp_cli:
        wp = requests.get(
            "https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar"
        )
        wp_cli.write(wp.content)

    os.chmod("/usr/local/bin/wp", 0o755)

    setup_wordpress(
        user=args.wp_user,
        password=args.wp_password,
        site_url=args.site_url,
        email=args.email,
        db_user=db_user,
        db_password=db_password,
    )
