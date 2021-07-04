# Steps

<https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-on-ubuntu-20-04>
<https://spinupwp.com/hosting-wordpress-yourself-nginx-php-mysql/>

1. apt update && apt upgrade
2. apt install nginx
3. apt install mysql-server
4. sudo apt install php-fpm php-mysql
5. Create SQL user and table <https://stackoverflow.com/questions/36631676/error-in-your-sql-syntax-check-the-manual-that-corresponds-to-your-mysql-server>
6. sudo apt install php-curl php-gd php-intl php-mbstring php-soap php-xml php-xmlrpc php-zip
7. sudo systemctl restart php7.4-fpm
8. Download WP-CLI
9. Create nginx config file
10. Download wordpress with wp-cli

## 2 attempt

1. apt update && apt upgrade -y
2. apt install -y nginx mysql-server php-fpm php-mysql
3. Create database and user
4. apt install -y php-curl php-gd php-intl php-mbstring php-soap php-xml php-xmlrpc php-zip
5. systemctl restart php7.4-fpm
6. mysql

``` SQL
CREATE DATABASE wordpress DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
CREATE USER 'wordpressuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON wordpress.* TO 'wordpressuser'@'localhost';
EXIT;
```

1. mkdir /var/www/wordpress
2. chown www-data:www-data /var/www/wordpress
3. /etc/nginx/sites-available/wordpress

``` nginx
server {
    listen 80;
    root /var/www/wordpress;

    index index.php;

    location = /favicon.ico { log_not_found off; access_log off; }
    location = /robots.txt { log_not_found off; access_log off; allow all; }
    location ~* \.(css|gif|ico|jpeg|jpg|js|png)$ {
        expires max;
        log_not_found off;
    }

    location / {
        try_files $uri $uri/ /index.php$is_args$args;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
     }

    location ~ /\.ht {
        deny all;
    }

}
```

1. sudo ln -s /etc/nginx/sites-available/wordpress /etc/nginx/sites-enabled/
2. sudo unlink /etc/nginx/sites-enabled/default
3. sudo service nginx reload
4. curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
5. chmod +x wp-cli.phar
6. sudo mv wp-cli.phar /usr/local/bin/wp
7. cd /var/www/wordpress/
8. sudo -u www-data wp core download --locale=es_ES
9. sudo -u www-data wp config create --dbname=wordpress --dbuser=wordpressuser --dbpass=password
10. sudo -u www-data wp core install --url=54.190.43.201 --title="Este es mi sitio hecho con WordPress" --admin_user=mi_usuario --admin_password=mi_contraseña --admin_email=mi@email.com