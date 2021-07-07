#!/usr/bin/python3

import datetime
import os
import shutil
import smtplib
import tarfile
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import boto3

HOME = "/home/ubuntu"
BACKUPS = "/var/backups/home"
BUCKET = "sebastianmarines"
RECEIVER = "sebastian0marines@gmail.com"


def new_backup(path: str, name: str) -> None:
    directory = (tup for tup in os.walk(path) if ".ssh" not in tup[0]
                 if ".aws" not in tup[0] if ".git" not in tup[0])
    files = (os.path.join(li[0], file) for li in directory for file in li[2])
    with tarfile.open(os.path.join("/var/backups/home",
                                   f"{name}-Full_backup.tar.gz"),
                      mode="w:gz") as tar:
        for file in files:
            tar.add(file)


def space_available(prev_backup: str) -> bool:
    _, _, free = shutil.disk_usage("/")
    prev_backup_size = os.path.getsize(prev_backup)
    return round(prev_backup_size * 1.2) < free


def send_email(to: str, message: str):
    msg = MIMEMultipart()
    msg["From"] = "sebastian.marines@clickittech.com.mx"
    msg["To"] = to
    msg["Subject"] = "Alerta backups"
    msg.attach(MIMEText(message, "plain"))
    server = smtplib.SMTP(host="mail.clickittech.com.mx", port=587)
    server.starttls()
    server.login(msg["From"], os.environ["PASSWORD"])
    server.sendmail(msg["From"], msg["To"], msg.as_string())
    server.quit()


if __name__ == "__main__":
    S3 = boto3.client("s3")

    today = datetime.datetime.now()
    current_date = today.strftime("%Y%m%d%H%M%S")

    old_backups = os.listdir(BACKUPS)
    old_backups.sort(
        reverse=True,
        key=lambda file: datetime.datetime.strptime(
            file.split(".")[0].strip("-Full_backup.tar.gz"), "%Y%m%d%H%M%S"),
    )
    last_backup = os.path.join(BACKUPS, old_backups[0])

    if space_available(last_backup):
        S3.upload_file(last_backup, BUCKET, old_backups[0])
        os.remove(last_backup)
        new_backup(HOME, current_date)
        send_email(RECEIVER, "Backup creado con exito")
    else:
        send_email(RECEIVER, "No hay espacio suficiente")
