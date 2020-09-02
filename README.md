Step 1 - Setup git and Clone 

1) sudo yum install git
2) git init
3) git clone https://github.com/Sum123it/aws-hackathon.git
                    
---------------------
Step 2 - Intall Apache httpd and mod_wsgi (https://flask.palletsprojects.com/en/1.1.x/deploying/mod_wsgi/)

1)	sudo yum install httpd
2)	sudo yum install mod_wsgi
---------------------------


Step 3 - Configure application to run with httpd

1)	sudo cp -r ProjectBookV1 /var/www
2)	cd /var/www ; sudo mv aws-hackathon ProjectBook
3)	cd ProjectBook  ; sudo vi welcome.conf

# This configuration file enables the default "Welcome" page if there
# is no default index page present for the root URL.  To disable the
# Welcome page, comment out all the lines below.
#
# NOTE: if this file is removed, it will be restored on upgrades.
#
<VirtualHost *>
   ServerName books.com
   WSGIDaemonProcess book user=ec2-user group=ec2-user threads=5 home=/var/www/ProjectBook
    WSGIScriptAlias / /var/www/ProjectBook/book.wsgi
    LogLevel debug

    <Directory /var/www/ProjectBook>
        WSGIProcessGroup book
        WSGIApplicationGroup %{GLOBAL}
        WSGIScriptReloading On
        Order deny,allow
        Allow from all
    </Directory>
</VirtualHost>

4)	sudo vi book.wsgi

import sys
sys.path.insert(0, '/var/www/ProjectBook/')
from book import app as application
application.debug = True

5)	cp app.py book.py

6)	cp welcome.conf /etc/httpd/conf.d/


7)	pip install SQLAlchemy==1.3.1 ;pip install Flask==1.0.2 ;pip install psycopg2==2.7.7
       
8)	sudo service httpd start

-----------------------------------------------------


Step 5 :setup POSTGRESQL Database instance on Cloud (free tier)

-----------------------------------------------------------

Step 6:Create database and tables on DB instance

create database lecture;
CREATE TABLE USERDATA (FNAME VARCHAR NOT NULL , LNAME VARCHAR NOT NULL , EMAIL TEXT NOT NULL ,USERNAME VARCHAR NOT NULL UNIQUE , PASSWORD TEXT NOT NULL);
CREATE TABLE BOOKS (ISBN VARCHAR NOT NULL UNIQUE,TITLE VARCHAR NOT NULL,AUTHOR VARCHAR NOT NULL,PUBYEAR INTEGER NOT NULL);
CREATE TABLE BOOK_RATING(ISBN VARCHAR NOT NULL ,USERNAME VARCHAR NOT NULL ,RATING INTEGER NOT NULL);
CREATE TABLE BOOK_REVIEW(ISBN VARCHAR NOT NULL,USERNAME VARCHAR NOT NULL,REVIEW TEXT NOT NULL);

-----------------------------------------------------------------

Step 7:Upload Refrence data in table 'BOOKS' created in step 6

There is a file name as ‘book.csv’ in project folder you need to upload data of that csv in ‘BOOKS’ table you create in postgres

----------------------------------------------------------------


DONE!!!!!!!!







