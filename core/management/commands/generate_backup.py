import os
import time
import datetime
import pipes

from target.models import Target

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Generate Backup'

    def handle(self, *args, **kwargs):

        BACKUP_PATH = './media/backup/dbbackup'

        # Getting current DateTime to create the separate backup folder like "20180817-123433".
        DATETIME = time.strftime('%Y%m%d-%H%M%S')
        TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME

        try:
            os.stat(TODAYBACKUPPATH)
        except:
            os.mkdir(TODAYBACKUPPATH)

        targets = Target.objects.all().order_by("-priority")

        for row in targets.iterator():

            self.takebackup(row, TODAYBACKUPPATH)

        print("Backup script completed")
        print("Your backups have been created in '" +
              TODAYBACKUPPATH + "' directory")

    def takebackup(self, data, TODAYBACKUPPATH):
        DB_HOST = data.db_host
        DB_USER = data.username
        DB_USER_PASSWORD = data.password
        DB_NAME = data.database

        print('processing .... '+DB_HOST)
        # Code for checking if you want to take single database backup or assinged multiple backups in DB_NAME.
        print("checking for databases names file.")
        if os.path.exists(DB_NAME):
            file1 = open(DB_NAME)
            multi = 1
            print("Databases file found...")
            print("Starting backup of all dbs listed in file " + DB_NAME)
        else:
            print("Databases file not found...")
            print("Starting backup of database " + DB_NAME)
            multi = 0

        # Starting actual database backup process.
        if multi:
            in_file = open(DB_NAME, "r")
            flength = len(in_file.readlines())
            in_file.close()
            p = 1
            dbfile = open(DB_NAME, "r")

            while p <= flength:
                db = dbfile.readline()   # reading database name from file
                db = db[:-1]         # deletes extra line
                dumpcmd = "mysqldump -h --column-statistics=0  " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + \
                    " " + db + " > " + \
                    pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
                os.system(dumpcmd)
                gzipcmd = "gzip " + \
                    pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
                os.system(gzipcmd)
                p = p + 1
            dbfile.close()
        else:
            db = DB_NAME
            dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + \
                " " + db + " > " + \
                pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
            os.system(dumpcmd)
            gzipcmd = "gzip " + \
                pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
            os.system(gzipcmd)
            #print(" asdf")
