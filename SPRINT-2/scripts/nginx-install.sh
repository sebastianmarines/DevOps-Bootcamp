#!/bin/bash

if ! [ $(id -u) = 0 ]; then
   echo "The script need to be run as root." >&2
   exit 1
fi

DIR=/tmp/nginx/

# Download necessary dependencies
mkdir -p $DIR
cd $DIR

echo "Downloading dependencies..."
wget -q https://ftp.pcre.org/pub/pcre/pcre-8.44.tar.gz && tar zxf pcre-*
wget -q http://zlib.net/zlib-1.2.11.tar.gz && tar zxf zlib-*
wget -q http://www.openssl.org/source/openssl-1.1.1g.tar.gz && tar zxf openssl-*

echo "Downloading Nginx..."
wget -q https://nginx.org/download/nginx-1.20.1.tar.gz && tar zxf nginx-*

NGINX="$DIR$(ls $DIR | grep nginx | grep -v .tar.gz)"
PCRE="$DIR$(ls $DIR | grep pcre | grep -v .tar.gz)"
ZLIB="$DIR$(ls $DIR | grep zlib | grep -v .tar.gz)"
OPENSSL="$DIR$(ls $DIR | grep openssl | grep -v .tar.gz)"

# Create user
echo "Creating Nginx user..."
addgroup nginx
adduser nginx --system --no-create-home --shell /bin/false --ingroup nginx

# Install nginx
cd $NGINX

apt install -y gcc
apt install -y libgeoip-dev

./configure --prefix=/etc/nginx  --sbin-path=/usr/local/nginx/nginx  --conf-path=/usr/local/nginx/nginx.conf  --pid-path=/usr/local/nginx/nginx.pid  --with-pcre=$PCRE  --with-zlib=$ZLIB  --with-openssl=$OPENSSL --with-http_geoip_module --user=nginx --group=nginx

make
make install

# Clean tmp directory
echo "Cleaning..."
rm -rf $DIR
