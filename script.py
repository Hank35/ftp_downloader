from ftplib import FTP
import os
from dotenv import load_dotenv

load_dotenv()

def login():
    """
    logs in to ftp server, put credentials here
    """
    username = os.getenv('FTP_USERNAME')
    password = os.getenv('FTP_PASSWORD')
    server_ip = os.getenv('FTP_SERVER_IP')
    ftp = FTP(server_ip)
    ftp.login(username, password)
    return ftp

def download(ftp):
    """
    downloads the world.zip file from main directory, fix file path for your needs
    """
    file = os.getenv('FTP_FILENAME')
    downloadpath = os.getenv('BACKUP_PATH') + f'/{file}'
    ftp.retrbinary('RETR ' + file ,open(downloadpath, 'wb').write)


def main():
    ftp = login()
    download(ftp)

main()
