#!/usr/bin/bash

RECIPIENT="sebastian0marines@gmail.com"

# https://stackoverflow.com/questions/41127585/shell-how-to-check-available-space-and-exit-if-not-enough
AVAIL_SPACE=$((1024*$(df /var/backups/home/ | awk 'NR==2 { print $4 }')))
NAME="/var/backups/home/`date +'%Y%m%d%H%M%S'`-Full_backup.tar.gz"
LOGS_NAME="/var/backups/logs/`date +'%Y%m%d%H%M%S'`-logs.tar.gz"

send_email() {
        echo "Subject: $1
From: sebastian.marines@clickittech.com.mx

$2
        " | curl --ssl-reqd smtp://mail.clickittech.com.mx:587 \
        --mail-from "sebastian.marines@clickittech.com.mx" \
        --mail-rcpt $RECIPIENT \
        --upload-file /dev/stdin \
        --user "sebastian.marines@clickittech.com.mx:$PASSWORD"
}

LAST_BACKUP_SIZE=$(ls -ltc /var/backups/home/ | sed -n '2p' | awk '{print $5}')
LAST_BACKUP_NAME=$(ls -ltc /var/backups/home/ | sed -n '2p' | awk '{print $9}')
LAST_BACKUP_FULL_PATH="/var/backups/home/$LAST_BACKUP_NAME"
NEEDED_SPACE=$(echo "1.2*$LAST_BACKUP_SIZE" | bc)
NEEDED_SPACE=${NEEDED_SPACE%.*}

if [[ $NEEDED_SPACE > $AVAIL_SPACE ]]; 
then
        echo "No hay espacio suficiente"
        send_email "Alerta backups" "No hay espacio suficiente"
        exit 1
else
        sudo tar -pczf $LOGS_NAME /var/log
        aws s3 cp $LOGS_NAME s3://sebastianmarines
        sudo rm $LOGS_NAME

        sudo tar -pczf $NAME --exclude="/home/ubuntu/.ssh/*" --exclude="/home/ubuntu/.aws/*" /home/ubuntu/
        aws s3 cp $LAST_BACKUP_FULL_PATH s3://sebastianmarines
        sudo rm $LAST_BACKUP_FULL_PATH

        send_email "Alerta backups" "Backup creado con exito"

fi

